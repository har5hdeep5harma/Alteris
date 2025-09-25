import streamlit as st
import polars as pl
import pandas as pd
import plotly.express as px
from typing import List, Dict, Any
import io

st.set_page_config(
    page_title="Alteris",
    page_icon="⛃",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("📄 Alteris")
st.markdown("> *When numbers drift and tables sway, we light the path and show the way.*")
st.markdown("""
    **Compare two datasets and instantly find the differences.**

    Upload a "base" (old) and a "current" (new) dataset to generate a detailed, interactive report. 
    It provides cell-level highlighting for modified rows and allows you to export the full report.

    *Built with the blazing-fast Polars library.*
""")

@st.cache_data
def load_dataframe(uploaded_file_content: bytes, file_name: str) -> pl.DataFrame:
    """Loads file content into a Polars DataFrame for efficient caching."""
    try:
        if file_name.endswith('.csv'):
            return pl.read_csv(uploaded_file_content)
        elif file_name.endswith(('.xls', '.xlsx')):
            # Polars can't read directly from bytes for Excel, so pandas is used as an intermediary
            pd_df = pd.read_excel(io.BytesIO(uploaded_file_content))
            return pl.from_pandas(pd_df)
        else:
            st.error(f"Unsupported file type: {file_name}")
            return None
    except Exception as e:
        st.error(f"Error loading file {file_name}: {e}")
        return None

@st.cache_data
def compare_schemas(df_base: pl.DataFrame, df_current: pl.DataFrame) -> Dict[str, Any]:
    """Compares the schemas of two DataFrames."""
    schema_base = df_base.schema
    schema_current = df_current.schema

    cols_base = set(schema_base.keys())
    cols_current = set(schema_current.keys())

    added_cols = list(cols_current - cols_base)
    removed_cols = list(cols_base - cols_current)

    common_cols = list(cols_base.intersection(cols_current))
    type_changes = []
    for col in common_cols:
        if schema_base[col] != schema_current[col]:
            type_changes.append({
                "column": col,
                "base_type": str(schema_base[col]),
                "current_type": str(schema_current[col])
            })
    return {
        "added": added_cols,
        "removed": removed_cols,
        "type_changes": type_changes
    }

@st.cache_data
def compare_data(df_base: pl.DataFrame, df_current: pl.DataFrame, keys: List[str]) -> Dict[str, pl.DataFrame]:
    """Performs the core data comparison (diffing) logic."""
    if not keys:
        return {}

    suffix = "_current"
    current_renamed_cols = {col: f"{col}{suffix}" for col in df_current.columns if col not in keys}
    df_current_renamed = df_current.rename(current_renamed_cols)

    joined_df = df_base.join(df_current_renamed, on=keys, how='outer')

    base_check_col = next((col for col in df_base.columns if col not in keys), None)
    current_check_col = next((f"{col}{suffix}" for col in df_current.columns if col not in keys), None)

    if not base_check_col or not current_check_col:
         st.warning("Cannot perform difference: at least one non-key column is required in both datasets.")
         return {}

    removed_rows = joined_df.filter(pl.col(current_check_col).is_null()).drop(list(df_current_renamed.columns))
    added_rows = joined_df.filter(pl.col(base_check_col).is_null()).drop(list(df_base.columns)).rename({v:k for k,v in current_renamed_cols.items()})

    common_rows = joined_df.drop_nulls()
    
    common_cols_to_compare = [
        col for col in df_base.columns if col in df_current.columns and col not in keys
    ]

    if not common_cols_to_compare:
         return {"added": added_rows, "removed": removed_rows, "modified": pl.DataFrame()}

    modification_exprs = [(pl.col(c) != pl.col(f"{c}{suffix}")) for c in common_cols_to_compare]

    modified_rows = common_rows.filter(
        pl.any_horizontal(modification_exprs)
    ).with_columns(
        changed_fields=pl.concat_str([
            pl.when(pl.col(c) != pl.col(f"{c}{suffix}")).then(pl.lit(f"{c}, ")).otherwise(pl.lit(""))
            for c in common_cols_to_compare
        ])
    ).with_columns(
        pl.col("changed_fields").str.slice(0, pl.col("changed_fields").str.len_chars() - 2)
    )

    return {"added": added_rows, "removed": removed_rows, "modified": modified_rows}

@st.cache_data
def to_excel(diff_results: dict) -> bytes:
    """Converts the difference report into a downloadable Excel file."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        sheet_order = ['modified', 'added', 'removed']
        for name in sheet_order:
            if name in diff_results and not diff_results[name].is_empty():
                diff_results[name].to_pandas().to_excel(writer, sheet_name=name.capitalize(), index=False)
    return output.getvalue()


if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False

def reset_report_state():
    """Callback to reset the report state when a new file is uploaded."""
    st.session_state.report_generated = False

col1, col2 = st.columns(2)
with col1:
    uploaded_file_base = st.file_uploader("📤 Upload Base Dataset (Old)", type=['csv', 'xlsx'], on_change=reset_report_state)
with col2:
    uploaded_file_current = st.file_uploader("📥 Upload Current Dataset (New)", type=['csv', 'xlsx'], on_change=reset_report_state)

if uploaded_file_base and uploaded_file_current:
    base_content = uploaded_file_base.getvalue()
    current_content = uploaded_file_current.getvalue()
    df_base = load_dataframe(base_content, uploaded_file_base.name)
    df_current = load_dataframe(current_content, uploaded_file_current.name)

    if df_base is not None and df_current is not None:
        st.subheader("Select Key Column(s) for Comparison")
        st.info("Choose the column(s) that uniquely identify a row (e.g., an ID). This is crucial for matching rows between the two datasets.", icon="💡")

        common_columns = sorted(list(set(df_base.columns) & set(df_current.columns)))

        if not common_columns:
            st.error("No common columns found between the two datasets. Cannot perform comparison.")
        else:
            key_columns = st.multiselect("Select key columns:", options=common_columns)

            if st.button("Generate Difference Report", use_container_width=True, type="primary"):
                if not key_columns:
                    st.warning("Please select at least one key column to proceed.")
                else:
                    st.session_state.report_generated = True
                    st.session_state.key_columns = key_columns
            
            if st.session_state.report_generated:
                keys = st.session_state.get('key_columns', [])
                if not keys:
                     st.error("Error: Key columns were not found. Please try generating the report again.")
                else:
                    with st.spinner("Analyzing differences... This may take a moment."):
                        schema_diff = compare_schemas(df_base, df_current)
                        data_diff = compare_data(df_base, df_current, keys)

                        st.header("Difference Report", divider="rainbow")

                        st.subheader("High-Level Summary")
                        summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)
                        with summary_col1:
                            st.metric("➕ Rows Added", value=f"{len(data_diff.get('added', [])):,}")
                        with summary_col2:
                            st.metric("➖ Rows Removed", value=f"{len(data_diff.get('removed', [])):,}")
                        with summary_col3:
                            st.metric("✏️ Rows Modified", value=f"{len(data_diff.get('modified', [])):,}")
                        with summary_col4:
                            st.download_button(
                                label="⬇️ Download Report (Excel)",
                                data=to_excel(data_diff),
                                file_name="alteris_report.xlsx",
                                mime="application/vnd.ms-excel",
                                use_container_width=True,
                            )
                        st.markdown("---")

                        tab_rows, tab_schema, tab_profile = st.tabs(["📝 **Row-level Changes**", "🏛️ **Schema Changes**", "📈 **Column Profiling**"])

                        with tab_rows:
                             if not any(not df.is_empty() for df in data_diff.values()):
                                 st.success("No row-level changes detected.")

                             if not data_diff.get("added", pl.DataFrame()).is_empty():
                                with st.expander(f"➕ Added Rows ({len(data_diff['added'])})", expanded=True):
                                    st.dataframe(data_diff['added'], use_container_width=True)

                             if not data_diff.get("removed", pl.DataFrame()).is_empty():
                                with st.expander(f"➖ Removed Rows ({len(data_diff['removed'])})", expanded=True):
                                    st.dataframe(data_diff['removed'], use_container_width=True)

                             if not data_diff.get("modified", pl.DataFrame()).is_empty():
                                with st.expander(f"✏️ Modified Rows ({len(data_diff['modified'])})", expanded=True):
                                    st.info("The table below highlights changes: **🟨 Old Value** vs. **🟦 New Value**. The `_current` suffix indicates the new value.", icon="📄")
                                    
                                    df_modified_pd = data_diff['modified'].to_pandas()
                                    
                                    def highlight_diff(row):
                                        styles = ['' for _ in row.index]
                                        changed_fields = str(row.get('changed_fields', '')).split(', ')
                                        for field in changed_fields:
                                            if field and field in row.index and f'{field}_current' in row.index:
                                                styles[row.index.get_loc(field)] = 'background-color: #FFF9C4; color: #795548;' 
                                                styles[row.index.get_loc(f'{field}_current')] = 'background-color: #E3F2FD; color: #1E88E5;' 
                                        return styles

                                    st.dataframe(df_modified_pd.style.apply(highlight_diff, axis=1), use_container_width=True, height=(min(len(df_modified_pd), 20) * 35) + 38)
                        
                        with tab_schema:
                            if not any(schema_diff.values()):
                                st.success("No schema changes detected.")
                            else:
                                if schema_diff["added"]:
                                    st.warning(f"Columns Added: `{', '.join(schema_diff['added'])}`")
                                if schema_diff["removed"]:
                                    st.error(f"Columns Removed: `{', '.join(schema_diff['removed'])}`")
                                if schema_diff["type_changes"]:
                                    st.info("Columns with Data Type Changes:")
                                    st.table(pd.DataFrame(schema_diff["type_changes"]))

                        with tab_profile:
                            st.subheader("Column Profiling & Distribution Shifts")
                            profile_common_cols = sorted(list(set(df_base.columns) & set(df_current.columns)))
                            profile_col = st.selectbox("Select a column to profile:", options=["-"] + profile_common_cols)

                            if profile_col != "-":
                                base_series = df_base.select(profile_col).to_series()
                                current_series = df_current.select(profile_col).to_series()
                                
                                if base_series.dtype.is_numeric():
                                    stats_data = {
                                        "Metric": ["Mean", "Std Dev", "Min", "Max", "Nulls", "Distinct Values"],
                                        "Base": [base_series.mean(), base_series.std(), base_series.min(), base_series.max(), base_series.null_count(), base_series.n_unique()],
                                        "Current": [current_series.mean(), current_series.std(), current_series.min(), current_series.max(), current_series.null_count(), current_series.n_unique()]
                                    }
                                else: 
                                    stats_data = {
                                        "Metric": ["Mean", "Std Dev", "Min", "Max", "Nulls", "Distinct Values"],
                                        "Base": [
                                            "N/A", "N/A", 
                                            str(base_series.min()), str(base_series.max()), 
                                            str(base_series.null_count()), str(base_series.n_unique())
                                        ],
                                        "Current": [
                                            "N/A", "N/A", 
                                            str(current_series.min()), str(current_series.max()), 
                                            str(current_series.null_count()), str(current_series.n_unique())
                                        ]
                                    }

                                stats_df = pl.DataFrame(stats_data)
                                
                                if "Base" in stats_df.columns and "Current" in stats_df.columns:
                                    if stats_df["Base"].dtype.is_numeric() and stats_df["Current"].dtype.is_numeric():
                                        stats_df = stats_df.with_columns(
                                            pl.col(["Base", "Current"]).round(2)
                                        )
                                
                                st.table(stats_df)

                                st.write("#### Distribution Comparison")
                                combined_df_for_plot = pl.concat([
                                    df_base.select(pl.col(profile_col).alias("value"), pl.lit("Base").alias("dataset")),
                                    df_current.select(pl.col(profile_col).alias("value"), pl.lit("Current").alias("dataset"))
                                ])
                                
                                if base_series.dtype in [pl.Categorical, pl.Utf8, pl.Boolean]:
                                    fig = px.histogram(combined_df_for_plot.to_pandas(), x="value", color="dataset", barmode="group", title=f"Distribution of '{profile_col}'")
                                else:
                                    fig = px.histogram(combined_df_for_plot.to_pandas(), x="value", color="dataset", marginal="box", barmode="overlay", title=f"Distribution of '{profile_col}'")
                                st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("Project by Harshdeep Sharma")