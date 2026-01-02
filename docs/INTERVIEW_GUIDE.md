# 🎯 Interview Mastery Guide - Alteris Project

> **Everything You Need to Ace Any Interview About This Project**

---

## 📖 Table of Contents

1. [Quick Elevator Pitch](#quick-elevator-pitch)
2. [Technical Concepts Deep Dive](#technical-concepts-deep-dive)
3. [50 Interview Questions & Answers](#50-interview-questions--answers)
4. [Live Coding Scenarios](#live-coding-scenarios)
5. [How to Modify the Project](#how-to-modify-the-project)
6. [Common Follow-Up Challenges](#common-follow-up-challenges)
7. [Talking Points by Experience Level](#talking-points-by-experience-level)

---

## Quick Elevator Pitch

### 30-Second Version
> "Alteris is a web-based data comparison tool I built with Python. Users upload two datasets - like an old and new version of an Excel file - and it instantly shows what changed: new rows, deleted rows, and modified values with cell-level highlighting. I used Streamlit for the UI, Polars for blazing-fast data processing, and Plotly for visualizations. The core algorithm uses database-style outer joins to efficiently detect differences."

### 60-Second Version
> "I built Alteris to solve a common problem: comparing two versions of a dataset. Think of it as GitHub Diff, but for data files.
> 
> **The problem**: Data teams often need to compare spreadsheets to find what changed - maybe after a data migration, a daily refresh, or an ETL pipeline run. Doing this manually is tedious and error-prone.
> 
> **My solution**: Upload a 'before' and 'after' CSV or Excel file, select a key column like 'employee_id', and get an instant interactive report. It shows added rows, removed rows, and modified rows with color-coded cell highlighting.
> 
> **Technical choices**: I used Polars instead of Pandas because it's 10x faster for large datasets. The comparison algorithm uses outer joins - the same technique databases use. Everything is cached for performance, and the UI is built with Streamlit for rapid development."

---

## Technical Concepts Deep Dive

### 1. Outer Join Algorithm

**What is an Outer Join?**

An outer join combines two tables, keeping ALL rows from both tables. Where keys don't match, NULLs are filled in.

```
TABLE A (Base)              TABLE B (Current)           OUTER JOIN RESULT
┌────┬───────┐              ┌────┬───────┐              ┌────┬─────────┬─────────┐
│ ID │ Name  │              │ ID │ Name  │              │ ID │ Name_A  │ Name_B  │
├────┼───────┤              ├────┼───────┤              ├────┼─────────┼─────────┤
│ 1  │ Alice │              │ 1  │ Alice │              │ 1  │ Alice   │ Alice   │ ← Match
│ 2  │ Bob   │              │ 3  │ Carol │              │ 2  │ Bob     │ NULL    │ ← Removed
└────┴───────┘              └────┴───────┘              │ 3  │ NULL    │ Carol   │ ← Added
                                                        └────┴─────────┴─────────┘
```

**Why this algorithm?**
- Hash-based joins are O(n + m) - very efficient
- Handles all three cases (add/remove/modify) in one pass
- Uses optimized database techniques

---

### 2. Memoization with @st.cache_data

**What is Memoization?**
Storing the results of expensive function calls and returning the cached result when the same inputs occur again.

```python
@st.cache_data
def load_dataframe(file_bytes, filename):
    # This only executes if inputs are new
    return pl.read_csv(file_bytes)
```

**How it works**:
```
Call 1: load_dataframe(bytes_A, "data.csv")
  → Hash inputs → Not in cache → Execute → Store → Return

Call 2: load_dataframe(bytes_A, "data.csv")  
  → Hash inputs → Found in cache! → Return cached result (skip execution)

Call 3: load_dataframe(bytes_B, "other.csv")
  → Hash inputs → Not in cache → Execute → Store → Return
```

---

### 3. Polars vs Pandas

| Feature | Pandas | Polars |
|---------|--------|--------|
| **Language** | Python/C | Rust |
| **Threading** | Single-threaded | Multi-threaded |
| **Memory Format** | NumPy arrays | Apache Arrow |
| **Speed** | Baseline | 10-100x faster |
| **Memory Usage** | Higher | ~50% less |
| **API Style** | Imperative | Expression-based |

**Why I used both**:
- Polars for speed-critical operations (comparison, filtering)
- Pandas for Excel I/O (Polars can't read Excel from bytes)

---

### 4. Session State in Streamlit

**Problem**: Streamlit re-runs the entire script on every interaction.

**Solution**: `st.session_state` persists data across reruns.

```python
# Initialize once
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Update on button click
if st.button("Increment"):
    st.session_state.counter += 1

# Display persisted value
st.write(st.session_state.counter)
```

---

### 5. Type Hints in Python

```python
def compare_data(
    df_base: pl.DataFrame, 
    df_current: pl.DataFrame, 
    keys: List[str]
) -> Dict[str, pl.DataFrame]:
```

**Benefits**:
- Self-documenting code
- IDE autocomplete
- Static analysis with mypy
- Catch bugs before runtime

---

### 6. Context Managers (with statement)

```python
with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Data')
# File is automatically closed and finalized here
```

**Why use context managers?**
- Automatic resource cleanup
- Exception-safe
- Cleaner code

---

### 7. Method Chaining in Polars

```python
result = (
    df
    .filter(pl.col("salary") > 50000)
    .select(["name", "salary"])
    .sort("salary", descending=True)
    .head(10)
)
```

**Benefits**:
- Readable, fluent API
- No intermediate variables
- Query optimization (in lazy mode)

---

### 8. Horizontal Operations

```python
# Check if ANY column differs (across columns, not down rows)
pl.any_horizontal([
    pl.col("name") != pl.col("name_current"),
    pl.col("salary") != pl.col("salary_current")
])
```

**Key distinction**:
- `any()` - down a column (vertical)
- `any_horizontal()` - across columns in a row (horizontal)

---

## 50 Interview Questions & Answers

### Architecture & Design (1-10)

**Q1: Why did you choose a monolithic architecture?**
> "For a focused tool like this, monolithic is appropriate because:
> 1. Streamlit apps are designed as single-file applications
> 2. The scope is limited - one clear purpose
> 3. Easier to deploy and debug
> 4. No inter-service communication overhead
> 
> I'd consider microservices if we needed separate scaling, multiple teams, or an API."

**Q2: How would you scale this for enterprise use?**
> "Several approaches:
> 1. **Horizontal scaling**: Deploy on Kubernetes with multiple replicas
> 2. **Caching layer**: Redis for shared session state
> 3. **Async processing**: Celery for background jobs
> 4. **Database backend**: Store comparisons for audit
> 5. **Authentication**: Add OAuth/SAML integration"

**Q3: What's the single responsibility of each function?**
> - `load_dataframe()`: File I/O only
> - `compare_schemas()`: Schema comparison only
> - `compare_data()`: Row-level comparison only
> - `to_excel()`: Export only
> - `highlight_diff()`: Styling only

**Q4: Why separate schema and data comparison?**
> "Schema changes are a different type of issue than data changes. A user might want to know if columns changed before diving into row changes. Also, schema comparison is O(number of columns), while data comparison is O(number of rows) - separating them allows independent caching."

**Q5: How do you handle file format detection?**
> "I use file extension detection (`file_name.endswith('.csv')`). This is simple and works for standard use cases. For more robust detection, I could use the `python-magic` library to inspect file headers."

**Q6: What design patterns did you use?**
> 1. **Memoization** (caching)
> 2. **Functional decomposition** (separate functions)
> 3. **Strategy pattern** (implicit in file format handling)
> 4. **Null Object pattern** (return empty DataFrames instead of None)

**Q7: How does data flow through the application?**
> ```
> Upload → load_dataframe() → Key Selection → compare_*() → Display
> ```
> Each step is cached, so re-running later steps doesn't re-execute earlier ones.

**Q8: Why use callbacks for file upload state reset?**
> "The `on_change` callback fires BEFORE the script re-runs, ensuring state is reset before the new file is processed. This prevents stale report data from being displayed."

**Q9: How would you add undo/redo functionality?**
> "Store comparison history in session state:
> ```python
> if 'history' not in st.session_state:
>     st.session_state.history = []
> st.session_state.history.append(current_comparison)
> ```
> Then provide navigation buttons."

**Q10: What's the trade-off with caching file content?**
> "Trade-off: Memory vs. Speed. Large files consume memory when cached. For very large files, I might:
> 1. Limit cache size with `max_entries` parameter
> 2. Use disk-based caching
> 3. Implement cache eviction policies"

---

### Data Processing (11-20)

**Q11: Explain the outer join algorithm step by step.**
> "1. Rename current columns to avoid collision
> 2. Outer join on key columns - keeps all rows from both
> 3. Rows with NULL current values = Removed
> 4. Rows with NULL base values = Added
> 5. Rows with no NULLs = Need modification check
> 6. Compare each column in matched rows for changes"

**Q12: Why do you rename columns before joining?**
> "Both DataFrames have the same column names. After joining, we need to distinguish which value came from which DataFrame. Adding `_current` suffix to current DataFrame columns makes this clear."

**Q13: How do you detect which specific fields changed?**
> ```python
> pl.concat_str([
>     pl.when(pl.col(c) != pl.col(f"{c}_current"))
>       .then(pl.lit(f"{c}, "))
>       .otherwise(pl.lit(""))
>     for c in columns
> ])
> ```
> "For each column, conditionally append its name if values differ, then concatenate all."

**Q14: What's the time complexity of your comparison?**
> "O(n + m) for the hash-based outer join, where n and m are row counts. Then O(k) per matched row for column comparison, where k is number of columns. Overall: O((n + m) × k)."

**Q15: How do you handle NULL values in comparisons?**
> "Polars treats NULL == NULL as True (unlike SQL where NULL != NULL). This means if both base and current have NULL for a column, it's not flagged as a change. This is usually the desired behavior."

**Q16: Why use sets for schema comparison?**
> "Sets provide O(1) average-case lookup and efficient set operations:
> - `set1 - set2`: Added columns
> - `set2 - set1`: Removed columns
> - `set1 & set2`: Common columns (for type comparison)"

**Q17: How would you handle case-insensitive column matching?**
> "Normalize column names before comparison:
> ```python
> cols_base = {c.lower() for c in schema_base.keys()}
> cols_current = {c.lower() for c in schema_current.keys()}
> ```"

**Q18: What if the key column has duplicates?**
> "This would cause incorrect results. The algorithm assumes keys are unique. I'd add validation:
> ```python
> if df.select(keys).is_duplicated().any():
>     st.error('Key columns must uniquely identify rows')
> ```"

**Q19: How do you handle large files that don't fit in memory?**
> "For very large files:
> 1. Use Polars' lazy mode: `pl.scan_csv()` instead of `pl.read_csv()`
> 2. Process in chunks
> 3. Use streaming aggregations
> 4. Sample for visualizations"

**Q20: Why convert to Pandas for Excel writing?**
> "Polars' Excel support is less mature. Pandas' `to_excel()` with XlsxWriter engine provides:
> - Multi-sheet support
> - Better formatting options
> - More reliable output"

---

### Streamlit & UI (21-30)

**Q21: Explain Streamlit's execution model.**
> "Streamlit re-runs the ENTIRE script from top to bottom on every user interaction. This is why caching is crucial - it prevents redundant computation. Session state persists data across reruns."

**Q22: Why use columns for layout?**
> "Columns place elements side by side. For file uploaders, this saves vertical space and implies the parallel nature of 'base' and 'current' datasets."

**Q23: How does `st.file_uploader` work?**
> "Returns an `UploadedFile` object when a file is uploaded, or `None` otherwise. The object has methods like `.getvalue()` (returns bytes) and `.name` (filename)."

**Q24: Why tabs instead of multiple pages?**
> "Tabs keep related information together without page navigation. Users can quickly switch between row changes, schema changes, and profiling without losing context."

**Q25: How does the download button work?**
> "```python
> st.download_button(
>     label='Download',
>     data=bytes,  # The file content
>     file_name='report.xlsx',
>     mime='application/vnd.ms-excel'
> )
> ```
> When clicked, it triggers a browser download of the provided bytes."

**Q26: Why use `use_container_width=True`?**
> "Makes charts and tables expand to fill available horizontal space, creating a responsive layout that works on different screen sizes."

**Q27: How would you add a progress bar for large files?**
> "```python
> progress = st.progress(0)
> for i, chunk in enumerate(chunks):
>     process(chunk)
>     progress.progress((i + 1) / total_chunks)
> ```"

**Q28: Why reset state on new file upload?**
> "Without resetting, the old report would still show after uploading a new file. The `on_change` callback ensures state is cleared before processing new data."

**Q29: How does `st.spinner` work?**
> "```python
> with st.spinner('Processing...'):
>     heavy_computation()
> ```
> Shows a loading indicator while the code inside executes."

**Q30: How would you add dark mode support?**
> "Streamlit's theming system:
> ```toml
> # .streamlit/config.toml
> [theme]
> primaryColor = '#FF4B4B'
> backgroundColor = '#0E1117'
> ```
> Or use `st.set_page_config(theme=...)` (limited options)."

---

### Performance (31-40)

**Q31: How does caching improve performance?**
> "Without cache: 50MB CSV takes 3 seconds to parse on EVERY interaction.
> With cache: 3 seconds on first upload, then instant.
> 
> For 10 interactions, this is 30 seconds vs 3 seconds."

**Q32: Why is Polars faster than Pandas?**
> "1. **Rust backend**: Compiled, zero-cost abstractions
> 2. **Multi-threading**: Uses all CPU cores
> 3. **Apache Arrow**: Columnar memory format
> 4. **SIMD**: Vectorized operations
> 5. **Query optimization**: In lazy mode"

**Q33: What's the bottleneck in your application?**
> "File parsing (reading CSV/Excel) is typically the bottleneck. Once data is in memory, comparisons are fast. This is why caching the loaded DataFrames is so impactful."

**Q34: How would you profile performance issues?**
> "```python
> import time
> start = time.perf_counter()
> result = load_dataframe(bytes, 'file.csv')
> print(f'Load time: {time.perf_counter() - start:.2f}s')
> ```
> Or use `cProfile` for detailed analysis."

**Q35: What's lazy evaluation and why didn't you use it?**
> "Lazy evaluation defers computation until `.collect()` is called, allowing query optimization. I used eager mode for simplicity since file sizes are typically manageable. For larger files, I'd switch to `pl.scan_csv()`."

**Q36: How does caching work with mutable objects?**
> "Streamlit serializes cached values. DataFrames are serialized/deserialized, which is safe. For mutable objects like Python dicts, the cache stores a copy, not a reference."

**Q37: What's the memory footprint of your app?**
> "Approximately 2x the size of the files (base + current DataFrames in memory). With the joined result, it could be 3x. For a 100MB file, expect ~300MB memory usage."

**Q38: How would you reduce memory usage?**
> "1. Use Polars' lazy mode
> 2. Select only needed columns
> 3. Filter early to reduce row count
> 4. Use smaller data types where possible
> 5. Clear intermediate results"

**Q39: Why not process chunks in parallel?**
> "For comparison, we need matching keys to be in the same process. Parallel processing would complicate key matching. Sequential processing with a fast library (Polars) is typically sufficient."

**Q40: How does the browser handle large result tables?**
> "Streamlit's `st.dataframe` uses pagination and virtualization. Only visible rows are rendered. For very large results, I limit height: `st.dataframe(df, height=600)`."

---

### Edge Cases & Error Handling (41-50)

**Q41: What happens if columns have the same name in base and current?**
> "That's expected! The algorithm renames current columns with `_current` suffix before joining to distinguish them."

**Q42: What if the file is empty?**
> "Polars would return an empty DataFrame. The comparison would show 'No changes detected' because both are empty. I could add validation for this edge case."

**Q43: How do you handle encoding issues?**
> "Currently, I rely on Polars' auto-detection. For problematic files:
> ```python
> pl.read_csv(bytes, encoding='latin1')
> ```"

**Q44: What if someone uploads a malicious file?**
> "Streamlit's file uploader provides some protection. Additionally:
> - File type is restricted to CSV/XLSX
> - Files are processed in memory, not saved to disk
> - Data is displayed, not executed
> For production, I'd add file size limits and content validation."

**Q45: How do you handle data type mismatches?**
> "The schema comparison detects type changes. For actual comparison, Polars handles type coercion automatically. I display type changes in the Schema tab."

**Q46: What if the key column is missing from one file?**
> "The key selector only shows columns present in BOTH files (`set1 & set2`). If a key column is missing, it won't be an option."

**Q47: How do you handle very long column names?**
> "Streamlit's dataframe display handles this with horizontal scrolling. For very long names, I could truncate in the display."

**Q48: What if there's a network error during file upload?**
> "Streamlit handles this at the framework level. The upload widget shows an error if the upload fails. The app waits until upload is complete."

**Q49: How do you handle concurrent users?**
> "Each Streamlit session is independent. Session state is per-user. Multiple users can use the app simultaneously without interference."

**Q50: What if comparison takes too long?**
> "I could add:
> 1. Timeout with user notification
> 2. Progress indication
> 3. Option to cancel
> 4. File size warning before processing"

---

## Live Coding Scenarios

### Scenario 1: "Add support for JSON files"

```python
def load_dataframe(uploaded_file_content: bytes, file_name: str) -> pl.DataFrame:
    try:
        if file_name.endswith('.csv'):
            return pl.read_csv(uploaded_file_content)
        elif file_name.endswith(('.xls', '.xlsx')):
            pd_df = pd.read_excel(io.BytesIO(uploaded_file_content))
            return pl.from_pandas(pd_df)
        # ADD THIS:
        elif file_name.endswith('.json'):
            return pl.read_json(uploaded_file_content)
        else:
            st.error(f"Unsupported file type: {file_name}")
            return None
    except Exception as e:
        st.error(f"Error loading file {file_name}: {e}")
        return None

# Also update file uploader:
st.file_uploader("...", type=['csv', 'xlsx', 'json'])
```

---

### Scenario 2: "Add row count validation"

```python
if df_base is not None and df_current is not None:
    # ADD THIS VALIDATION:
    MAX_ROWS = 100000
    if len(df_base) > MAX_ROWS or len(df_current) > MAX_ROWS:
        st.error(f"Files must have fewer than {MAX_ROWS:,} rows for performance reasons.")
        st.stop()
    
    # Continue with existing logic...
```

---

### Scenario 3: "Add duplicate key detection"

```python
if st.button("Generate Difference Report"):
    if not key_columns:
        st.warning("Please select at least one key column.")
    else:
        # ADD THIS VALIDATION:
        base_duplicates = df_base.select(key_columns).is_duplicated().sum()
        current_duplicates = df_current.select(key_columns).is_duplicated().sum()
        
        if base_duplicates > 0:
            st.error(f"Base dataset has {base_duplicates} duplicate keys. Keys must be unique.")
            st.stop()
        if current_duplicates > 0:
            st.error(f"Current dataset has {current_duplicates} duplicate keys. Keys must be unique.")
            st.stop()
        
        # Continue with comparison...
```

---

### Scenario 4: "Add percentage change for numeric columns"

```python
def calculate_change_stats(df_base, df_current, numeric_col):
    base_mean = df_base.select(pl.col(numeric_col).mean()).item()
    current_mean = df_current.select(pl.col(numeric_col).mean()).item()
    
    if base_mean != 0:
        pct_change = ((current_mean - base_mean) / base_mean) * 100
        return pct_change
    return None

# Use in profiling tab:
if base_series.dtype.is_numeric():
    pct = calculate_change_stats(df_base, df_current, profile_col)
    if pct is not None:
        st.metric("Mean Change", f"{pct:+.1f}%")
```

---

## How to Modify the Project

### Adding a New Feature

1. **Identify where it fits**: UI change? New comparison logic? Export format?
2. **Add to appropriate function** or create new function
3. **Add caching** if computationally expensive
4. **Update UI** to expose the feature
5. **Add error handling**
6. **Test with sample data**

### Common Modifications

| Modification | Where to Change | Difficulty |
|--------------|-----------------|------------|
| Support new file format | `load_dataframe()` | Easy |
| Add new export format | New function + download button | Easy |
| Change UI layout | Main script, use `st.columns`, `st.tabs` | Easy |
| Add authentication | Wrap app in auth check | Medium |
| Add database storage | New functions + connection | Medium |
| Support very large files | Switch to lazy mode | Hard |

---

## Common Follow-Up Challenges

### "Make it handle 10 million rows"

**Solution**:
1. Switch to Polars lazy mode: `pl.scan_csv()`
2. Use streaming aggregations
3. Sample data for visualizations
4. Add progress bars
5. Consider chunked processing

### "Add version history"

**Solution**:
1. Store comparisons in database with timestamps
2. Add UI to select historical comparisons
3. Allow re-running comparisons

### "Make it an API"

**Solution**:
1. Extract comparison logic into separate module
2. Create FastAPI endpoints
3. Return JSON results
4. Keep Streamlit as optional frontend

### "Add scheduled comparisons"

**Solution**:
1. Use Celery or APScheduler for background jobs
2. Configure data sources (databases, cloud storage)
3. Send notifications on changes
4. Store results for review

---

## Talking Points by Experience Level

### For Junior Developer Interviews

- Focus on: Python basics, Pandas/Polars syntax, basic algorithms
- Highlight: You understand the code, can make simple modifications
- Prepare: Explain any function in detail

### For Mid-Level Interviews

- Focus on: Design decisions, performance considerations, trade-offs
- Highlight: Why you chose specific libraries, alternatives considered
- Prepare: How you'd add complex features

### For Senior/Lead Interviews

- Focus on: Architecture, scalability, production readiness
- Highlight: How you'd evolve this to enterprise scale
- Prepare: Discuss testing, deployment, monitoring

---

## Final Checklist Before Interview

- [ ] Can explain what the app does in 30 seconds
- [ ] Know the purpose of each library
- [ ] Understand the outer join algorithm
- [ ] Can explain caching and why it matters
- [ ] Know at least 3 alternatives for each technology choice
- [ ] Can draw the data flow diagram
- [ ] Ready to make simple modifications live
- [ ] Prepared answers for top 10 questions
- [ ] Ran the app locally to refresh memory

---

*Good luck with your interview! You've got this.* 🚀
