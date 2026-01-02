# 📄 app.py - Complete Code Documentation

> **The Heart of Alteris: Every Line Explained for Interview Mastery**

---

## 📖 Table of Contents

1. [File Overview](#file-overview)
2. [Imports Section](#imports-section-lines-1-6)
3. [Page Configuration](#page-configuration-lines-8-13)
4. [UI Header Section](#ui-header-section-lines-15-24)
5. [Function: load_dataframe](#function-load_dataframe-lines-26-38)
6. [Function: compare_schemas](#function-compare_schemas-lines-40-62)
7. [Function: compare_data](#function-compare_data-lines-64-107)
8. [Function: to_excel](#function-to_excel-lines-109-118)
9. [Session State Management](#session-state-management-lines-120-125)
10. [File Upload UI](#file-upload-ui-lines-127-133)
11. [Main Application Logic](#main-application-logic-lines-135-250)
12. [Key Algorithms Explained](#key-algorithms-explained)
13. [Design Patterns Used](#design-patterns-used)
14. [Interview Deep Dives](#interview-deep-dives)

---

## File Overview

| Aspect | Details |
|--------|---------|
| **Purpose** | Main application file containing all UI and business logic |
| **Lines of Code** | ~250 lines |
| **Architecture** | Monolithic (single-file application) |
| **Framework** | Streamlit |
| **Key Libraries** | Polars, Pandas, Plotly |

### Execution Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        APPLICATION FLOW                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────┐    ┌──────────────┐    ┌─────────────────┐               │
│   │  Imports │───►│ Page Config  │───►│ Title & Header  │               │
│   └──────────┘    └──────────────┘    └────────┬────────┘               │
│                                                 │                        │
│                                                 ▼                        │
│   ┌──────────────────────────────────────────────────────────┐          │
│   │              File Upload (Base + Current)                 │          │
│   └──────────────────────────┬───────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│   ┌──────────────────────────────────────────────────────────┐          │
│   │            load_dataframe() [CACHED]                      │          │
│   │            Converts uploaded bytes to Polars DataFrame    │          │
│   └──────────────────────────┬───────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│   ┌──────────────────────────────────────────────────────────┐          │
│   │            Key Column Selection                           │          │
│   │            User selects unique identifier columns         │          │
│   └──────────────────────────┬───────────────────────────────┘          │
│                              │                                           │
│                              ▼                                           │
│   ┌──────────────────────────────────────────────────────────┐          │
│   │            "Generate Report" Button Clicked               │          │
│   └──────────────────────────┬───────────────────────────────┘          │
│                              │                                           │
│          ┌───────────────────┼───────────────────┐                      │
│          ▼                   ▼                   ▼                       │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                 │
│   │ compare_    │    │ compare_    │    │  to_excel   │                 │
│   │ schemas()   │    │ data()      │    │  ()         │                 │
│   │ [CACHED]    │    │ [CACHED]    │    │  [CACHED]   │                 │
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘                 │
│          │                  │                  │                         │
│          └──────────────────┼──────────────────┘                         │
│                             ▼                                            │
│   ┌──────────────────────────────────────────────────────────┐          │
│   │                  REPORT DISPLAY                           │          │
│   │  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐    │          │
│   │  │ Summary  │  │ Schema   │  │ Column Profiling     │    │          │
│   │  │ Metrics  │  │ Changes  │  │ & Distributions      │    │          │
│   │  └──────────┘  └──────────┘  └──────────────────────┘    │          │
│   └──────────────────────────────────────────────────────────┘          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Imports Section (Lines 1-6)

```python
import streamlit as st
import polars as pl
import pandas as pd
import plotly.express as px
from typing import List, Dict, Any
import io
```

### Line-by-Line Explanation

#### Line 1: `import streamlit as st`

**What it does**: Imports the Streamlit library with alias `st`.

**Why `st` alias?**: Convention in the Streamlit community. Makes code more readable: `st.button()` instead of `streamlit.button()`.

**What is Streamlit?**: 
- Open-source Python framework for building web apps
- Turns Python scripts into interactive web applications
- No HTML/CSS/JavaScript required
- Reactive: re-runs the script from top to bottom on every user interaction

**Interview Point - Streamlit Execution Model**:
> "Streamlit re-runs the entire script whenever a user interacts with a widget. This is why caching is crucial - without `@st.cache_data`, we'd re-read the uploaded files on every button click or dropdown change."

**Alternatives to Streamlit**:

| Alternative | When to Choose Instead |
|-------------|----------------------|
| Flask/FastAPI | Need a REST API, fine-grained control |
| Dash | Need more complex callback patterns |
| Gradio | Building ML model demos |
| Django | Need full web framework with ORM, auth, etc. |

---

#### Line 2: `import polars as pl`

**What it does**: Imports Polars, a high-performance DataFrame library.

**Why `pl` alias?**: Standard convention (similar to `pd` for pandas).

**What is Polars?**:
- Modern DataFrame library written in Rust
- Uses Apache Arrow memory format
- 10-100x faster than Pandas for most operations
- Multi-threaded by default
- Supports lazy evaluation

**Key Polars Concepts Used in This Project**:

| Concept | Explanation | Where Used |
|---------|-------------|------------|
| **Eager Execution** | Operations execute immediately | `pl.read_csv()` |
| **Expressions** | Chainable operations | `pl.col("x").filter()` |
| **Lazy Evaluation** | Delay execution for optimization | Not used here (could be added) |
| **Schema** | Column name → data type mapping | `df.schema` |

**Interview Deep Dive - Why Polars Over Pandas?**:

```
┌───────────────────┬─────────────────────────────────────────────────────┐
│ Aspect            │ Comparison                                          │
├───────────────────┼─────────────────────────────────────────────────────┤
│ Performance       │ Polars is 10-100x faster (Rust, multi-threaded)     │
│ Memory            │ Polars uses ~50% less memory (Arrow format)         │
│ API               │ Polars is more consistent and expressive            │
│ Community         │ Pandas has larger community (established 2008)      │
│ Ecosystem         │ Pandas integrates with more libraries               │
│ Learning Curve    │ Pandas documentation is more extensive              │
└───────────────────┴─────────────────────────────────────────────────────┘
```

---

#### Line 3: `import pandas as pd`

**What it does**: Imports Pandas with standard alias.

**Why still use Pandas when we have Polars?**:
> "Polars cannot read Excel files directly from bytes in memory. Pandas can, so I use it as a bridge: `pd.read_excel()` → `pl.from_pandas()`."

**This is a common pattern**: Use the right tool for each job, even if it means mixing libraries.

---

#### Line 4: `import plotly.express as px`

**What it does**: Imports Plotly Express for data visualization.

**What is Plotly Express?**:
- High-level interface to Plotly.js
- One-line functions for common chart types
- Interactive by default (zoom, pan, hover, export)
- Works natively with Streamlit via `st.plotly_chart()`

**Why Plotly Over Matplotlib/Seaborn?**:

| Library | Pros | Cons |
|---------|------|------|
| **Plotly** | Interactive, beautiful defaults, web-ready | Larger bundle size |
| **Matplotlib** | Full control, publication-quality | Static images, verbose |
| **Seaborn** | Statistical plots, good defaults | Static, limited interactivity |
| **Altair** | Declarative, good for Streamlit | Less flexible than Plotly |

---

#### Line 5: `from typing import List, Dict, Any`

**What it does**: Imports type hints from Python's typing module.

**What are Type Hints?**:
```python
# Without type hints
def compare_schemas(df_base, df_current):
    pass

# With type hints
def compare_schemas(df_base: pl.DataFrame, df_current: pl.DataFrame) -> Dict[str, Any]:
    pass
```

**Benefits of Type Hints**:
1. **Documentation**: Self-documenting code
2. **IDE Support**: Autocompletion, error detection
3. **Maintainability**: Easier to refactor
4. **Static Analysis**: Tools like `mypy` can catch bugs before runtime

**Interview Point**:
> "I use type hints because they make the code self-documenting and help catch bugs early. IDEs like VS Code can use them to provide better autocompletion and error detection."

---

#### Line 6: `import io`

**What it does**: Imports Python's built-in `io` module for handling streams.

**How it's used**:
1. `io.BytesIO()` - Creates in-memory binary streams for Excel reading/writing
2. Uploaded files come as bytes; `BytesIO` makes them look like file objects

**Example**:
```python
# Uploaded file content is bytes
uploaded_content = uploaded_file.getvalue()  # bytes

# BytesIO wraps it to look like a file object
file_like_object = io.BytesIO(uploaded_content)

# Now Pandas can read it as if it were a file
pd.read_excel(file_like_object)
```

---

## Page Configuration (Lines 8-13)

```python
st.set_page_config(
    page_title="Alteris",
    page_icon="⛃",
    layout="wide",
    initial_sidebar_state="collapsed",
)
```

### Line-by-Line Explanation

**`st.set_page_config()`**: Must be the first Streamlit command in the script. Configures the browser tab and page layout.

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `page_title` | "Alteris" | Browser tab title |
| `page_icon` | "⛃" | Favicon (cylinder emoji representing database) |
| `layout` | "wide" | Uses full browser width instead of centered column |
| `initial_sidebar_state` | "collapsed" | Sidebar starts hidden |

**Why `layout="wide"`?**:
> "Data comparison needs horizontal space. Tables with many columns would be cramped in the default centered layout. Wide layout gives users more room to see their data."

**Alternative Layout Options**:
- `"centered"` - Default, content in center column (~70% width)
- `"wide"` - Full browser width

---

## UI Header Section (Lines 15-24)

```python
st.title("📄 Alteris")
st.markdown("> *When numbers drift and tables sway, we light the path and show the way.*")
st.markdown("""
    **Compare two datasets and instantly find the differences.**

    Upload a "base" (old) and a "current" (new) dataset to generate a detailed, interactive report. 
    It provides cell-level highlighting for modified rows and allows you to export the full report.

    *Built with the blazing-fast Polars library.*
""")
```

### UI Elements Used

| Function | Purpose | Markdown Support |
|----------|---------|-----------------|
| `st.title()` | Largest header (H1) | ✅ Emojis work |
| `st.markdown()` | Renders Markdown text | ✅ Full Markdown |

**Why Markdown?**:
- Rich formatting without HTML
- Supports bold, italic, links, code blocks
- Cleaner than multiple `st.write()` calls

**UX Principle - Clear Value Proposition**:
The header immediately tells users:
1. What the app does ("Compare two datasets")
2. How to use it ("Upload base and current")
3. What they get ("detailed, interactive report")
4. Technical differentiator ("blazing-fast Polars")

---

## Function: load_dataframe (Lines 26-38)

```python
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
```

### Complete Breakdown

#### The Decorator: `@st.cache_data`

**What it does**: Memoizes (caches) the function result based on input parameters.

**How caching works**:

```
┌─────────────────────────────────────────────────────────────┐
│                  CACHING MECHANISM                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   First Call: load_dataframe(bytes_123, "data.csv")         │
│   ┌──────────────────────────────────────────────┐          │
│   │ 1. Hash the arguments: hash(bytes_123, "data.csv")      │
│   │ 2. Check cache: Key not found                           │
│   │ 3. Execute function: Read CSV, create DataFrame         │
│   │ 4. Store in cache: {hash_key: DataFrame}                │
│   │ 5. Return DataFrame                                     │
│   └──────────────────────────────────────────────┘          │
│                                                              │
│   Second Call: load_dataframe(bytes_123, "data.csv")        │
│   ┌──────────────────────────────────────────────┐          │
│   │ 1. Hash the arguments: hash(bytes_123, "data.csv")      │
│   │ 2. Check cache: Key FOUND!                              │
│   │ 3. Return cached DataFrame (skip execution)             │
│   └──────────────────────────────────────────────┘          │
│                                                              │
│   Third Call: load_dataframe(bytes_456, "other.csv")        │
│   ┌──────────────────────────────────────────────┐          │
│   │ 1. Hash the arguments: Different hash!                  │
│   │ 2. Check cache: Key not found                           │
│   │ 3. Execute function again                               │
│   └──────────────────────────────────────────────┘          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Why is caching crucial here?**:
> "Streamlit re-runs the entire script on every user interaction. Without caching, uploading a 50MB CSV would mean re-parsing it every time the user selects a dropdown option. With caching, we parse once and reuse."

**Performance Impact**:
| Without Cache | With Cache |
|---------------|------------|
| Re-read file on every interaction | Read once, reuse |
| 50MB CSV: ~2-3 seconds per interaction | 50MB CSV: ~2-3 seconds first time, milliseconds after |

---

#### Function Signature

```python
def load_dataframe(uploaded_file_content: bytes, file_name: str) -> pl.DataFrame:
```

| Parameter | Type | Purpose |
|-----------|------|---------|
| `uploaded_file_content` | `bytes` | Raw file bytes from upload |
| `file_name` | `str` | Original filename (used to detect format) |
| **Returns** | `pl.DataFrame` | Polars DataFrame or None on error |

**Why bytes instead of file object?**:
> "Bytes are hashable (can be cached). Streamlit's UploadedFile objects are not directly hashable, so we extract `.getvalue()` before caching."

---

#### File Format Detection

```python
if file_name.endswith('.csv'):
    return pl.read_csv(uploaded_file_content)
elif file_name.endswith(('.xls', '.xlsx')):
    pd_df = pd.read_excel(io.BytesIO(uploaded_file_content))
    return pl.from_pandas(pd_df)
```

**Logic**:

```
                    ┌──────────────────┐
                    │ Check extension  │
                    └────────┬─────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
     ┌──────────┐     ┌──────────┐     ┌──────────┐
     │  .csv    │     │.xls/.xlsx│     │  Other   │
     └────┬─────┘     └────┬─────┘     └────┬─────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────┐ ┌────────────────┐ ┌─────────────┐
│ pl.read_csv()   │ │ pd.read_excel()│ │ st.error()  │
│                 │ │       ↓        │ │ return None │
│                 │ │ pl.from_pandas │ │             │
└─────────────────┘ └────────────────┘ └─────────────┘
```

**Interview Point - Why the Pandas Detour for Excel?**:
> "Polars can read Excel files from disk paths, but not from in-memory bytes. Since Streamlit file uploads are in-memory, I use Pandas as a bridge. This is a pragmatic choice: use the right tool for each limitation."

---

#### Error Handling

```python
try:
    # ... file reading logic
except Exception as e:
    st.error(f"Error loading file {file_name}: {e}")
    return None
```

**Why broad exception handling?**:
File reading can fail for many reasons:
- Corrupted file
- Encoding issues
- Malformed CSV (uneven columns)
- Password-protected Excel
- Unsupported Excel features

**User Experience Consideration**:
> "Instead of crashing, we show a user-friendly error message and return None. The calling code checks for None and handles it gracefully."

---

## Function: compare_schemas (Lines 40-62)

```python
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
```

### Algorithm Visualization

```
BASE SCHEMA                          CURRENT SCHEMA
┌─────────────────┐                  ┌─────────────────┐
│ id: Int64       │                  │ id: Int64       │
│ name: Utf8      │                  │ name: Utf8      │
│ age: Int64      │ ◄── REMOVED      │ age: Utf8       │ ◄── TYPE CHANGED!
│ temp: Float64   │ ◄── REMOVED      │ email: Utf8     │ ◄── ADDED
└─────────────────┘                  │ status: Boolean │ ◄── ADDED
                                     └─────────────────┘

RESULT:
{
    "added": ["email", "status"],
    "removed": ["temp"],
    "type_changes": [
        {"column": "age", "base_type": "Int64", "current_type": "Utf8"}
    ]
}
```

### Line-by-Line Breakdown

#### Getting Schemas

```python
schema_base = df_base.schema
schema_current = df_current.schema
```

**What is a schema?**:
In Polars, `df.schema` returns an ordered dictionary: `{column_name: data_type, ...}`

Example:
```python
>>> df.schema
{'id': Int64, 'name': Utf8, 'salary': Float64}
```

---

#### Set Operations for Column Detection

```python
cols_base = set(schema_base.keys())      # {'id', 'name', 'age', 'temp'}
cols_current = set(schema_current.keys()) # {'id', 'name', 'age', 'email', 'status'}

added_cols = list(cols_current - cols_base)     # {'email', 'status'}
removed_cols = list(cols_base - cols_current)   # {'temp'}
common_cols = list(cols_base.intersection(cols_current))  # {'id', 'name', 'age'}
```

**Set Operations Explained**:

| Operation | Symbol | Result |
|-----------|--------|--------|
| Difference | `A - B` | Elements in A but not in B |
| Intersection | `A.intersection(B)` | Elements in both A and B |
| Union | `A.union(B)` | All elements from both |

**Interview Point - Why Sets?**:
> "Sets provide O(1) average-case lookup and efficient set operations. Converting lists to sets for comparison is a common pattern for finding additions/removals."

---

#### Type Change Detection

```python
for col in common_cols:
    if schema_base[col] != schema_current[col]:
        type_changes.append({
            "column": col,
            "base_type": str(schema_base[col]),
            "current_type": str(schema_current[col])
        })
```

**Logic**: For columns that exist in both DataFrames, compare their data types.

**Real-World Example**: 
A column might change from `Int64` to `Utf8` (String) if:
- Data was exported differently
- Nulls were introduced (some systems convert to strings)
- A bug in the source system

---

## Function: compare_data (Lines 64-107)

This is the **core algorithm** of the application. Understanding this thoroughly is critical for interviews.

```python
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
```

### Algorithm Visualization - The Outer Join Approach

```
STEP 1: PREPARE DATA
═══════════════════════════════════════════════════════════════════════

BASE DataFrame (df_base)           CURRENT DataFrame (df_current)
┌────────┬────────┬────────┐      ┌────────┬────────┬────────┐
│ id     │ name   │ salary │      │ id     │ name   │ salary │
├────────┼────────┼────────┤      ├────────┼────────┼────────┤
│ 101    │ Alice  │ 90000  │      │ 101    │ Alice  │ 95000  │  ◄── MODIFIED
│ 102    │ Bob    │ 75000  │      │ 102    │ Bob    │ 75000  │
│ 103    │ Carol  │ 80000  │      │ 104    │ Dave   │ 85000  │  ◄── ADDED
└────────┴────────┴────────┘      └────────┴────────┴────────┘
    ▲                                   │
    │                                   │ 103 removed!
    │                                   │
    └───────────────────────────────────┘


STEP 2: RENAME CURRENT COLUMNS (avoid collision)
═══════════════════════════════════════════════════════════════════════

df_current_renamed:
┌────────┬────────────────┬────────────────┐
│ id     │ name_current   │ salary_current │
├────────┼────────────────┼────────────────┤
│ 101    │ Alice          │ 95000          │
│ 102    │ Bob            │ 75000          │
│ 104    │ Dave           │ 85000          │
└────────┴────────────────┴────────────────┘


STEP 3: OUTER JOIN ON KEY COLUMN(S)
═══════════════════════════════════════════════════════════════════════

joined_df = df_base.join(df_current_renamed, on='id', how='outer')

┌────────┬────────┬────────┬────────────────┬────────────────┐
│ id     │ name   │ salary │ name_current   │ salary_current │
├────────┼────────┼────────┼────────────────┼────────────────┤
│ 101    │ Alice  │ 90000  │ Alice          │ 95000          │  ◄── EXISTS IN BOTH
│ 102    │ Bob    │ 75000  │ Bob            │ 75000          │  ◄── EXISTS IN BOTH (unchanged)
│ 103    │ Carol  │ 80000  │ NULL           │ NULL           │  ◄── REMOVED (current is NULL)
│ 104    │ NULL   │ NULL   │ Dave           │ 85000          │  ◄── ADDED (base is NULL)
└────────┴────────┴────────┴────────────────┴────────────────┘


STEP 4: FILTER BY NULL PATTERNS
═══════════════════════════════════════════════════════════════════════

REMOVED ROWS: Where current columns are NULL
┌────────┬────────┬────────┐
│ id     │ name   │ salary │
├────────┼────────┼────────┤
│ 103    │ Carol  │ 80000  │
└────────┴────────┴────────┘

ADDED ROWS: Where base columns are NULL
┌────────┬────────┬────────┐
│ id     │ name   │ salary │
├────────┼────────┼────────┤
│ 104    │ Dave   │ 85000  │
└────────┴────────┴────────┘

COMMON ROWS: No NULLs (rows that exist in both)
┌────────┬────────┬────────┬────────────────┬────────────────┐
│ id     │ name   │ salary │ name_current   │ salary_current │
├────────┼────────┼────────┼────────────────┼────────────────┤
│ 101    │ Alice  │ 90000  │ Alice          │ 95000          │
│ 102    │ Bob    │ 75000  │ Bob            │ 75000          │
└────────┴────────┴────────┴────────────────┴────────────────┘


STEP 5: DETECT MODIFICATIONS IN COMMON ROWS
═══════════════════════════════════════════════════════════════════════

For each common column, check: base_value != current_value

Row 101: name == name_current? ✓   salary == salary_current? ✗ (90000 ≠ 95000)
Row 102: name == name_current? ✓   salary == salary_current? ✓

MODIFIED ROWS (at least one column differs):
┌────────┬────────┬────────┬────────────────┬────────────────┬────────────────┐
│ id     │ name   │ salary │ name_current   │ salary_current │ changed_fields │
├────────┼────────┼────────┼────────────────┼────────────────┼────────────────┤
│ 101    │ Alice  │ 90000  │ Alice          │ 95000          │ salary         │
└────────┴────────┴────────┴────────────────┴────────────────┴────────────────┘
```

### Key Code Sections Explained

#### Column Renaming Strategy

```python
suffix = "_current"
current_renamed_cols = {col: f"{col}{suffix}" for col in df_current.columns if col not in keys}
df_current_renamed = df_current.rename(current_renamed_cols)
```

**Why rename?**:
> "When joining two DataFrames with the same column names, we need to distinguish them. By adding `_current` suffix to the current DataFrame's non-key columns, we can tell which value came from which dataset."

**Dictionary Comprehension Explained**:
```python
# Input:  columns = ['id', 'name', 'salary'], keys = ['id']
# Output: {'name': 'name_current', 'salary': 'salary_current'}
```

---

#### The Outer Join

```python
joined_df = df_base.join(df_current_renamed, on=keys, how='outer')
```

**Join Types Reference**:

| Join Type | Description | Use Case |
|-----------|-------------|----------|
| `inner` | Only matching keys | Find common rows |
| `left` | All from left, matching from right | Keep all base rows |
| `right` | All from right, matching from left | Keep all current rows |
| `outer` | All from both | **Find all differences** |

**Interview Point - Why Outer Join?**:
> "An outer join includes ALL rows from both DataFrames. Rows only in the base will have NULL for current columns (removed), and rows only in current will have NULL for base columns (added). Rows in both can be compared for modifications."

---

#### Detecting Removed Rows

```python
removed_rows = joined_df.filter(pl.col(current_check_col).is_null()).drop(list(df_current_renamed.columns))
```

**Logic**:
1. Filter: Where current-side column is NULL (row doesn't exist in current)
2. Drop: Remove the current-side columns (they're all NULL anyway)

---

#### Detecting Added Rows

```python
added_rows = joined_df.filter(pl.col(base_check_col).is_null()).drop(list(df_base.columns)).rename({v:k for k,v in current_renamed_cols.items()})
```

**Logic**:
1. Filter: Where base-side column is NULL (row doesn't exist in base)
2. Drop: Remove the base-side columns (they're all NULL)
3. Rename: Remove `_current` suffix to restore original column names

---

#### Detecting Modified Rows (The Complex Part)

```python
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
```

**Breaking it down**:

1. **Create comparison expressions**:
```python
# If columns are ['name', 'salary']:
modification_exprs = [
    (pl.col('name') != pl.col('name_current')),
    (pl.col('salary') != pl.col('salary_current'))
]
```

2. **Filter with `pl.any_horizontal()`**:
```python
# Keep row if ANY column differs
pl.any_horizontal(modification_exprs)
# This is like: (name ≠ name_current) OR (salary ≠ salary_current)
```

3. **Track which fields changed**:
```python
# Build a string like "salary, " for each changed field
pl.when(pl.col(c) != pl.col(f"{c}{suffix}")).then(pl.lit(f"{c}, ")).otherwise(pl.lit(""))
# Then concatenate: "" + "salary, " = "salary, "
```

4. **Clean up trailing comma**:
```python
# "salary, " → "salary"
pl.col("changed_fields").str.slice(0, pl.col("changed_fields").str.len_chars() - 2)
```

**Interview Deep Dive - `pl.any_horizontal()` vs `pl.any()`**:
> "`pl.any_horizontal()` checks across columns in a single row (horizontal). `pl.any()` without horizontal checks down a column (vertical). For row-wise comparisons, we need horizontal."

---

## Function: to_excel (Lines 109-118)

```python
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
```

### Complete Breakdown

**Purpose**: Convert the comparison results to a downloadable Excel file with multiple sheets.

**Step-by-Step**:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Create in-memory buffer: io.BytesIO()                    │
├─────────────────────────────────────────────────────────────┤
│ 2. Create Excel writer with XlsxWriter engine               │
├─────────────────────────────────────────────────────────────┤
│ 3. For each result type (modified, added, removed):         │
│    - Convert Polars DataFrame to Pandas                     │
│    - Write to a separate sheet                              │
├─────────────────────────────────────────────────────────────┤
│ 4. Return bytes for download                                │
└─────────────────────────────────────────────────────────────┘
```

**Why XlsxWriter?**:

| Engine | Pros | Cons |
|--------|------|------|
| `xlsxwriter` | Feature-rich, good performance | Can only write (not read) |
| `openpyxl` | Read and write | Slower for large files |

**Why convert to Pandas first?**:
> "Polars' `to_excel()` is less mature than Pandas'. Using `to_pandas().to_excel()` ensures compatibility and access to all Excel writing features."

**Context Manager (`with` statement)**:
```python
with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    # ... write sheets ...
# File is automatically finalized when exiting the `with` block
```

---

## Session State Management (Lines 120-125)

```python
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False

def reset_report_state():
    """Callback to reset the report state when a new file is uploaded."""
    st.session_state.report_generated = False
```

### What is Session State?

**Problem**: Streamlit re-runs the entire script on every interaction. How do we remember that the user already clicked "Generate Report"?

**Solution**: `st.session_state` - a dictionary that persists across reruns for the current user session.

```
SCRIPT RUN 1 (page load):
┌──────────────────────────────────────────────────────────────┐
│ session_state = {}                                           │
│ if 'report_generated' not in session_state:                  │
│     session_state['report_generated'] = False  ◄── Initialize │
└──────────────────────────────────────────────────────────────┘

SCRIPT RUN 2 (button clicked):
┌──────────────────────────────────────────────────────────────┐
│ session_state = {'report_generated': False}  ◄── Persisted!  │
│ if 'report_generated' not in session_state:                  │
│     (skip - already exists)                                  │
│                                                              │
│ ... later in code ...                                        │
│ session_state['report_generated'] = True                     │
└──────────────────────────────────────────────────────────────┘

SCRIPT RUN 3 (dropdown changed):
┌──────────────────────────────────────────────────────────────┐
│ session_state = {'report_generated': True}  ◄── Still True!  │
│ Report is still displayed because we check this flag         │
└──────────────────────────────────────────────────────────────┘
```

**The Callback Pattern**:
```python
def reset_report_state():
    st.session_state.report_generated = False

st.file_uploader(..., on_change=reset_report_state)
```

**Why a callback?**: When the user uploads a new file, we want to clear the old report. The `on_change` callback runs before the script reruns, ensuring state is reset.

---

## File Upload UI (Lines 127-133)

```python
col1, col2 = st.columns(2)
with col1:
    uploaded_file_base = st.file_uploader("📤 Upload Base Dataset (Old)", type=['csv', 'xlsx'], on_change=reset_report_state)
with col2:
    uploaded_file_current = st.file_uploader("📥 Upload Current Dataset (New)", type=['csv', 'xlsx'], on_change=reset_report_state)
```

### Layout: Columns

```python
col1, col2 = st.columns(2)
```

**What this creates**:
```
┌─────────────────────────────────────────────────────────────┐
│                    BROWSER WINDOW                            │
│  ┌─────────────────────────┬─────────────────────────────┐  │
│  │         col1            │          col2               │  │
│  │                         │                             │  │
│  │  [📤 Upload Base...]    │  [📥 Upload Current...]     │  │
│  │                         │                             │  │
│  └─────────────────────────┴─────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Column Proportions**:
```python
st.columns(2)           # Equal width: [50%, 50%]
st.columns([1, 2])      # Proportional: [33%, 66%]
st.columns([1, 2, 1])   # Three columns: [25%, 50%, 25%]
```

### File Uploader Widget

```python
st.file_uploader(
    "📤 Upload Base Dataset (Old)",  # Label
    type=['csv', 'xlsx'],             # Allowed extensions
    on_change=reset_report_state      # Callback when file changes
)
```

**What it returns**:
- `None` if no file uploaded
- `UploadedFile` object if file uploaded (has `.name`, `.getvalue()`, etc.)

**Security Note**:
> "Streamlit's file uploader only accepts files of specified types. The `type` parameter acts as a basic filter, but server-side validation (checking the actual content) is always recommended for production."

---

## Main Application Logic (Lines 135-250)

### Structure Overview

```python
if uploaded_file_base and uploaded_file_current:
    # Load DataFrames
    # Show key column selector
    
    if st.button("Generate Report"):
        st.session_state.report_generated = True
    
    if st.session_state.report_generated:
        # Run comparison
        # Display results in tabs
```

### Key UI Components

#### The Key Column Selector

```python
common_columns = sorted(list(set(df_base.columns) & set(df_current.columns)))
key_columns = st.multiselect("Select key columns:", options=common_columns)
```

**UX Decision - Why Multiselect?**:
> "Some datasets have composite keys (multiple columns together form a unique identifier). For example, `(order_id, product_id)` in an order line items table. Multiselect allows users to select one or more key columns."

---

#### Metrics Display

```python
summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)
with summary_col1:
    st.metric("➕ Rows Added", value=f"{len(data_diff.get('added', [])):,}")
```

**The `:,` format specifier**:
```python
f"{12345:,}"  # Output: "12,345" (comma-separated thousands)
```

---

#### Tabbed Interface

```python
tab_rows, tab_schema, tab_profile = st.tabs(["📝 Row-level Changes", "🏛️ Schema Changes", "📈 Column Profiling"])

with tab_rows:
    # Row-level changes content
    
with tab_schema:
    # Schema changes content
    
with tab_profile:
    # Profiling content
```

**UX Principle - Progressive Disclosure**:
> "Tabs hide complexity. Users see the most important info first (summary metrics), then can drill down into details (row changes, schema changes, profiling) without being overwhelmed."

---

#### Cell-Level Highlighting

```python
def highlight_diff(row):
    styles = ['' for _ in row.index]
    changed_fields = str(row.get('changed_fields', '')).split(', ')
    for field in changed_fields:
        if field and field in row.index and f'{field}_current' in row.index:
            styles[row.index.get_loc(field)] = 'background-color: #FFF9C4; color: #795548;' 
            styles[row.index.get_loc(f'{field}_current')] = 'background-color: #E3F2FD; color: #1E88E5;' 
    return styles

st.dataframe(df_modified_pd.style.apply(highlight_diff, axis=1), ...)
```

**How Pandas Styler Works**:

```
┌─────────────────────────────────────────────────────────────┐
│  Original DataFrame                                          │
│  ┌────────┬────────┬────────────────┐                        │
│  │ salary │ ...    │ salary_current │                        │
│  ├────────┼────────┼────────────────┤                        │
│  │ 90000  │ ...    │ 95000          │                        │
│  └────────┴────────┴────────────────┘                        │
│                      │                                        │
│                      ▼                                        │
│  Apply highlight_diff to each row (axis=1)                   │
│                      │                                        │
│                      ▼                                        │
│  Styled DataFrame                                            │
│  ┌────────┬────────┬────────────────┐                        │
│  │ 90000  │ ...    │ 95000          │                        │
│  │ 🟨     │        │ 🟦             │                        │
│  └────────┴────────┴────────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

**Color Choices**:
- Yellow (`#FFF9C4`): Old value (warm = past)
- Blue (`#E3F2FD`): New value (cool = present)

---

#### Column Profiling

```python
if base_series.dtype.is_numeric():
    stats_data = {
        "Metric": ["Mean", "Std Dev", "Min", "Max", "Nulls", "Distinct Values"],
        "Base": [base_series.mean(), base_series.std(), ...],
        "Current": [current_series.mean(), current_series.std(), ...]
    }
```

**Statistics Explained**:

| Metric | What It Tells You | Use Case |
|--------|-------------------|----------|
| **Mean** | Average value | Detect overall shifts |
| **Std Dev** | Spread of values | Detect volatility changes |
| **Min/Max** | Range | Detect outliers or data truncation |
| **Nulls** | Missing values | Detect data quality issues |
| **Distinct** | Unique values | Detect normalization issues |

---

#### Distribution Visualization

```python
combined_df_for_plot = pl.concat([
    df_base.select(pl.col(profile_col).alias("value"), pl.lit("Base").alias("dataset")),
    df_current.select(pl.col(profile_col).alias("value"), pl.lit("Current").alias("dataset"))
])

fig = px.histogram(combined_df_for_plot.to_pandas(), x="value", color="dataset", ...)
st.plotly_chart(fig, use_container_width=True)
```

**Data Transformation for Plotting**:

```
BASE                           CURRENT
┌─────────┐                   ┌─────────┐
│ salary  │                   │ salary  │
├─────────┤                   ├─────────┤
│ 90000   │                   │ 95000   │
│ 75000   │                   │ 82000   │
└─────────┘                   └─────────┘
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
            COMBINED FOR PLOT
            ┌─────────┬─────────┐
            │ value   │ dataset │
            ├─────────┼─────────┤
            │ 90000   │ Base    │
            │ 75000   │ Base    │
            │ 95000   │ Current │
            │ 82000   │ Current │
            └─────────┴─────────┘
```

**Why this transformation?**:
> "Plotly Express's `color` parameter expects a categorical column to separate data series. By stacking the DataFrames and adding a 'dataset' column, we can plot both distributions on the same chart with different colors."

---

## Key Algorithms Explained

### 1. Outer Join for Data Diffing

**Time Complexity**: O(n + m) where n and m are the row counts of the two DataFrames (hash join).

**Space Complexity**: O(n + m) for the joined result.

**Why this algorithm?**:
> "Outer joins are a standard database operation optimized over decades. Polars implements this using hash joins, which are highly efficient for equality-based comparisons."

**Alternative Approaches**:

| Approach | Pros | Cons |
|----------|------|------|
| **Outer Join** (used) | Efficient, handles all cases | Requires key columns |
| **Row-by-row comparison** | Simple to understand | O(n*m) complexity, very slow |
| **Hashing entire rows** | Detects any change | Doesn't identify which cells changed |
| **Set difference** | Very fast for simple cases | Loses row identity |

---

### 2. Horizontal Any for Modification Detection

```python
pl.any_horizontal(modification_exprs)
```

**What it does**: Returns `True` if ANY of the expressions in the list evaluates to `True` for a given row.

**Time Complexity**: O(n * k) where n is row count and k is number of columns.

---

## Design Patterns Used

### 1. Functional Decomposition

The code separates concerns into distinct functions:
- `load_dataframe()` - I/O
- `compare_schemas()` - Schema comparison
- `compare_data()` - Data comparison
- `to_excel()` - Export

**Benefit**: Each function can be tested, cached, and modified independently.

---

### 2. Memoization (Caching)

All heavy functions use `@st.cache_data`.

**Benefit**: Repeated calls with same inputs are instant.

---

### 3. Strategy Pattern (Implicit)

The file format detection implements a simple strategy:
```python
if file_name.endswith('.csv'):
    # CSV strategy
elif file_name.endswith('.xlsx'):
    # Excel strategy
```

**Could be improved with**:
```python
loaders = {
    '.csv': load_csv,
    '.xlsx': load_excel,
    '.parquet': load_parquet  # Easy to extend
}
```

---

### 4. Null Object Pattern

```python
data_diff.get('added', pl.DataFrame())  # Returns empty DataFrame if 'added' doesn't exist
```

**Benefit**: Avoids `None` checks throughout the code.

---

## Interview Deep Dives

### Q: "Walk me through what happens when a user uploads a file"

**Answer**:
1. User drops file onto the file uploader widget
2. Streamlit receives the file and stores it in memory as bytes
3. The `on_change` callback (`reset_report_state`) fires, clearing any previous report
4. Streamlit reruns the entire script from top to bottom
5. The `uploaded_file_base` variable now contains the `UploadedFile` object
6. We extract the raw bytes with `.getvalue()`
7. `load_dataframe()` is called with the bytes and filename
8. Since this is the first call with these exact bytes, the function executes:
   - Detects file format from extension
   - Parses the file into a Polars DataFrame
   - Stores result in cache
   - Returns the DataFrame
9. The DataFrame is now available for the rest of the script

---

### Q: "How would you handle a file with 10 million rows?"

**Answer**:
1. **Lazy Loading**: Use `pl.scan_csv()` instead of `pl.read_csv()` for lazy evaluation
2. **Streaming**: Process in chunks using Polars' streaming mode
3. **Sampling**: For visualizations, sample the data
4. **Progress Bars**: Add `st.progress()` for user feedback
5. **Async Processing**: Use Streamlit's experimental async features
6. **Backend Separation**: Move heavy computation to a separate service

---

### Q: "What's the biggest limitation of this application?"

**Answer**:
1. **Memory**: Both DataFrames must fit in memory
2. **Single User Focus**: No multi-user session isolation
3. **No Persistence**: Results are lost when the browser closes
4. **Key Requirement**: Cannot compare without a key column
5. **Type Sensitivity**: Comparison might fail if the same data has different types

---

### Q: "How would you add authentication?"

**Answer**:
```python
import streamlit as st
from streamlit_authenticator import Authenticate

# Use Streamlit-Authenticator library
authenticator = Authenticate(...)
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # Show the main app
elif authentication_status == False:
    st.error('Username/password is incorrect')
```

Or use Streamlit Cloud's built-in authentication for deployed apps.

---

## Quick Reference

### All Functions at a Glance

| Function | Input | Output | Purpose |
|----------|-------|--------|---------|
| `load_dataframe(bytes, str)` | File bytes, filename | `pl.DataFrame` | Load any supported file |
| `compare_schemas(df, df)` | Two DataFrames | `Dict` | Find column differences |
| `compare_data(df, df, keys)` | Two DataFrames, key columns | `Dict[str, DataFrame]` | Find row differences |
| `to_excel(dict)` | Diff results | `bytes` | Create Excel report |
| `reset_report_state()` | None | None | Clear session state |
| `highlight_diff(row)` | Pandas row | List of styles | Color-code changes |

---

*This documentation covers every aspect of app.py for interview preparation.*
