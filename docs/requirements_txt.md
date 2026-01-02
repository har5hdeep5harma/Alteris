# 📦 requirements.txt - Dependencies Documentation

> **Understanding Every Package Your Project Depends On**

---

## 📖 Table of Contents

1. [File Overview](#file-overview)
2. [What is requirements.txt?](#what-is-requirementstxt)
3. [Package-by-Package Deep Dive](#package-by-package-deep-dive)
4. [Dependency Graph](#dependency-graph)
5. [Version Management](#version-management)
6. [Alternative Packages](#alternative-packages)
7. [Interview Questions](#interview-questions)

---

## File Overview

```
streamlit
pandas
polars
plotly
openpyxl
xlsxwriter
```

| Aspect | Details |
|--------|---------|
| **Purpose** | Lists all Python packages required to run the application |
| **Usage** | `pip install -r requirements.txt` |
| **Package Count** | 6 direct dependencies |
| **Total with Transitive** | ~50+ packages (installed automatically) |

---

## What is requirements.txt?

### Purpose

The `requirements.txt` file is the standard way to declare Python project dependencies. When someone clones your repository, they can install everything needed with one command:

```bash
pip install -r requirements.txt
```

### How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEPENDENCY INSTALLATION                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  requirements.txt              pip install                       │
│  ┌─────────────┐              ┌─────────────────────┐           │
│  │ streamlit   │ ──────────►  │ Download streamlit  │           │
│  │ pandas      │              │ from PyPI           │           │
│  │ polars      │              └──────────┬──────────┘           │
│  │ plotly      │                         │                       │
│  │ openpyxl    │                         ▼                       │
│  │ xlsxwriter  │              ┌─────────────────────┐           │
│  └─────────────┘              │ Resolve transitive  │           │
│                               │ dependencies        │           │
│                               │ (numpy, pyarrow...) │           │
│                               └──────────┬──────────┘           │
│                                          │                       │
│                                          ▼                       │
│                               ┌─────────────────────┐           │
│                               │ Install all packages│           │
│                               │ to site-packages/   │           │
│                               └─────────────────────┘           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Version Specification Formats

This project uses **unpinned versions** (no version numbers). Here are all the formats you should know:

| Format | Example | Meaning |
|--------|---------|---------|
| Unpinned | `streamlit` | Latest version |
| Exact | `streamlit==1.28.0` | Exactly this version |
| Minimum | `streamlit>=1.28.0` | This version or higher |
| Compatible | `streamlit~=1.28.0` | >=1.28.0, <1.29.0 |
| Range | `streamlit>=1.25,<1.30` | Between these versions |
| Exclude | `streamlit!=1.27.0` | Not this version |

**Interview Point - Why Unpinned in This Project?**:
> "For a personal project or demo, unpinned versions ensure users get the latest features and bug fixes. For production, you'd pin exact versions to ensure reproducibility."

---

## Package-by-Package Deep Dive

### 1. Streamlit

```
streamlit
```

#### What It Is
Streamlit is an open-source Python framework that transforms Python scripts into interactive web applications. It's particularly popular for data science and machine learning demos.

#### Role in This Project
- **Primary UI Framework**: All user interface elements (file uploaders, buttons, tabs, tables, charts) are Streamlit components
- **State Management**: `st.session_state` remembers user interactions
- **Caching**: `@st.cache_data` prevents redundant computation
- **Deployment**: Streamlit Cloud provides free hosting

#### Key Concepts

**1. Execution Model**:
```python
# Streamlit re-runs the ENTIRE script on every user interaction
import streamlit as st

st.title("Counter")  # Runs every time
count = st.session_state.get('count', 0)  # Persists across runs
if st.button("Increment"):
    st.session_state.count = count + 1  # Update state
st.write(f"Count: {count}")  # Displays current value
```

**2. Widgets Return Values**:
```python
name = st.text_input("Your name")  # Returns the input value
if name:
    st.write(f"Hello, {name}!")
```

**3. Caching**:
```python
@st.cache_data  # Memoize based on function arguments
def expensive_computation(data):
    # This only runs once for each unique 'data'
    return process(data)
```

#### Transitive Dependencies (Installed Automatically)
- `altair` - For declarative visualizations
- `tornado` - Web server
- `click` - Command-line interface
- `toml` - Configuration file parsing
- `validators` - Input validation
- `watchdog` - File system monitoring (for hot reload)

#### Alternatives

| Alternative | When to Choose |
|-------------|----------------|
| **Dash** | Need more complex callback patterns, enterprise features |
| **Gradio** | ML model demos with standard interfaces |
| **Flask/FastAPI** | Need REST API, custom frontend |
| **Panel** | Already using HoloViz ecosystem |
| **Shiny for Python** | Coming from R/Shiny background |

---

### 2. Pandas

```
pandas
```

#### What It Is
Pandas is the most widely used data manipulation library in Python. It provides the `DataFrame` data structure and thousands of methods for data analysis.

#### Role in This Project
- **Excel File Reading**: `pd.read_excel()` handles `.xlsx` files
- **Data Conversion**: Bridge between file bytes and Polars DataFrame
- **Excel Writing**: `pd.DataFrame.to_excel()` creates downloadable reports
- **Styling**: `DataFrame.style.apply()` for cell highlighting

#### Why Not Use Pandas for Everything?

| Aspect | Pandas | Polars |
|--------|--------|--------|
| **Performance** | Slower (single-threaded) | 10-100x faster (multi-threaded Rust) |
| **Memory** | Higher usage | ~50% less (Arrow format) |
| **API** | More methods, larger community | Cleaner, more consistent |
| **Excel Support** | Full (read & write) | Limited (can't read from bytes) |

**Interview Point**:
> "I use Polars for the core comparison logic because performance matters for large datasets. But Pandas is still needed for Excel I/O because Polars can't read Excel files from in-memory bytes. This shows pragmatic library selection."

#### Transitive Dependencies
- `numpy` - Numerical operations
- `python-dateutil` - Date parsing
- `pytz` - Timezone handling

---

### 3. Polars

```
polars
```

#### What It Is
Polars is a modern DataFrame library written in Rust. It's designed for speed and memory efficiency, using the Apache Arrow memory format.

#### Role in This Project
- **Primary Data Engine**: All comparison logic uses Polars
- **CSV Reading**: `pl.read_csv()` for fast CSV parsing
- **Data Transformations**: Filtering, joining, aggregations
- **Schema Inspection**: `df.schema` for column metadata

#### Key Polars Concepts Used

**1. Expressions**:
```python
# Polars uses expressions for transformations
df.filter(pl.col("salary") > 50000)  # Filter rows
df.select(pl.col("name"), pl.col("salary"))  # Select columns
df.with_columns(pl.col("salary") * 1.1)  # Add/modify columns
```

**2. Lazy Evaluation** (not used in this project but important):
```python
# Lazy: Build query plan, execute once
lazy_df = pl.scan_csv("data.csv")
result = lazy_df.filter(...).select(...).collect()  # Execute

# Eager (used in this project): Execute immediately
df = pl.read_csv("data.csv")  # Reads immediately
```

**3. Joins**:
```python
df1.join(df2, on="id", how="outer")  # Database-style join
```

**4. Horizontal Operations**:
```python
pl.any_horizontal([expr1, expr2])  # Any expression true in row?
pl.concat_str([col1, col2])  # Concatenate columns
```

#### Why Polars Over Pandas?

**Performance Benchmark** (typical results):

| Operation | Pandas | Polars | Speedup |
|-----------|--------|--------|---------|
| Read 1GB CSV | 30s | 3s | 10x |
| Filter 10M rows | 500ms | 50ms | 10x |
| Join 2 tables | 2s | 200ms | 10x |
| GroupBy aggregate | 1s | 100ms | 10x |

**Interview Deep Dive**:
> "Polars achieves this speed through:
> 1. **Rust backend**: Compiled, zero-cost abstractions
> 2. **Apache Arrow**: Columnar memory format, no serialization overhead
> 3. **Multi-threading**: Automatically uses all CPU cores
> 4. **Query optimization**: Lazy mode optimizes query plans"

#### Transitive Dependencies
- `pyarrow` - Apache Arrow Python bindings

---

### 4. Plotly

```
plotly
```

#### What It Is
Plotly is a graphing library that creates interactive, publication-quality charts. Plotly Express is its high-level API for quick chart creation.

#### Role in This Project
- **Distribution Charts**: Histograms comparing base vs. current data
- **Interactive Features**: Zoom, pan, hover tooltips, export
- **Streamlit Integration**: `st.plotly_chart()` renders plots

#### How It's Used

```python
import plotly.express as px

# One-liner for histogram
fig = px.histogram(
    df,                      # Data source
    x="value",               # Column for x-axis
    color="dataset",         # Color by category
    barmode="overlay",       # Overlapping bars
    marginal="box"           # Add box plot on margin
)

st.plotly_chart(fig, use_container_width=True)
```

#### Chart Types Available

| Chart Type | Use Case | Code |
|------------|----------|------|
| Histogram | Distribution | `px.histogram(df, x="col")` |
| Bar | Categorical comparison | `px.bar(df, x="cat", y="val")` |
| Line | Time series | `px.line(df, x="date", y="val")` |
| Scatter | Correlation | `px.scatter(df, x="a", y="b")` |
| Box | Statistical summary | `px.box(df, x="cat", y="val")` |

#### Why Plotly Over Matplotlib?

| Aspect | Matplotlib | Plotly |
|--------|------------|--------|
| **Interactivity** | Static images | Zoom, pan, hover, export |
| **Syntax** | Verbose, imperative | Concise, declarative |
| **Web Integration** | Requires extra work | Native JavaScript |
| **3D Charts** | Possible but complex | Easy |
| **Customization** | Unlimited | Good but some limits |

---

### 5. Openpyxl

```
openpyxl
```

#### What It Is
Openpyxl is a Python library for reading and writing Excel 2010+ files (`.xlsx`).

#### Role in This Project
- **Excel Reading Backend**: When Pandas calls `pd.read_excel()`, it uses openpyxl as the engine
- **Not called directly**: It's a dependency of Pandas for Excel support

#### How Pandas Uses It

```python
# When you write:
pd.read_excel("file.xlsx")

# Pandas internally does:
from openpyxl import load_workbook
wb = load_workbook("file.xlsx")
# ... converts to DataFrame
```

#### Why Not Just Use Openpyxl Directly?

| Approach | Pros | Cons |
|----------|------|------|
| Via Pandas | Simple API, returns DataFrame | Less control |
| Directly | Full Excel features (formatting, formulas) | More code |

**Interview Point**:
> "Openpyxl is a transitive dependency—Pandas needs it for Excel support. I don't call it directly because Pandas' `read_excel()` provides a cleaner API. But if I needed advanced Excel features like cell formatting or formulas, I'd use openpyxl directly."

---

### 6. XlsxWriter

```
xlsxwriter
```

#### What It Is
XlsxWriter is a Python library for writing Excel files. Unlike openpyxl, it's write-only but offers more features for creating complex spreadsheets.

#### Role in This Project
- **Excel Report Generation**: Creates the downloadable multi-sheet report
- **Engine for Pandas**: Specified in `pd.ExcelWriter(..., engine='xlsxwriter')`

#### How It's Used

```python
output = io.BytesIO()
with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    df_added.to_excel(writer, sheet_name='Added', index=False)
    df_removed.to_excel(writer, sheet_name='Removed', index=False)
    df_modified.to_excel(writer, sheet_name='Modified', index=False)
return output.getvalue()  # Returns Excel file as bytes
```

#### Why XlsxWriter Over Openpyxl for Writing?

| Aspect | XlsxWriter | Openpyxl |
|--------|------------|----------|
| **Performance** | Faster for large files | Slower |
| **Memory** | Constant memory mode | Higher memory |
| **Features** | Charts, sparklines, tables | Basic formatting |
| **Read Support** | ❌ Write-only | ✅ Read & write |

---

## Dependency Graph

```
                    ┌─────────────────┐
                    │   requirements  │
                    │       .txt      │
                    └────────┬────────┘
                             │
     ┌─────────────┬─────────┼─────────┬─────────────┬─────────────┐
     │             │         │         │             │             │
     ▼             ▼         ▼         ▼             ▼             ▼
┌─────────┐  ┌─────────┐ ┌───────┐ ┌───────┐  ┌──────────┐  ┌───────────┐
│streamlit│  │ pandas  │ │polars │ │plotly │  │ openpyxl │  │xlsxwriter │
└────┬────┘  └────┬────┘ └───┬───┘ └───┬───┘  └──────────┘  └───────────┘
     │            │          │         │
     │            │          │         └──► tenacity, packaging
     │            │          │
     │            │          └──► pyarrow
     │            │
     │            └──► numpy, python-dateutil, pytz
     │
     └──► altair, tornado, click, toml, validators, watchdog, ...


LEGEND:
─────────────────────────────────────────────────────────────
→  depends on (transitive dependency)
```

---

## Version Management

### Current State: Unpinned Versions

The current `requirements.txt` uses unpinned versions:
```
streamlit
pandas
```

**Pros**:
- Always get latest features and security fixes
- No maintenance of version numbers
- Good for demos and learning

**Cons**:
- **Reproducibility**: Different users might install different versions
- **Breaking Changes**: A library update could break the app
- **Debugging**: "It worked yesterday" scenarios

### Production Best Practice: Pinned Versions

For production, you would use:
```
streamlit==1.28.0
pandas==2.1.0
polars==0.19.0
plotly==5.17.0
openpyxl==3.1.2
xlsxwriter==3.1.9
```

### Even Better: Lock Files

```bash
# Generate lock file with all transitive dependencies
pip freeze > requirements.lock

# Install exact versions
pip install -r requirements.lock
```

### Modern Alternative: Poetry or pip-tools

```bash
# Using Poetry
poetry add streamlit pandas polars plotly openpyxl xlsxwriter
# Creates pyproject.toml and poetry.lock

# Using pip-tools
pip-compile requirements.in  # Creates requirements.txt with pins
```

---

## Alternative Packages

### If You Needed to Replace Each Package

| Current | Alternative | When to Switch |
|---------|-------------|----------------|
| **Streamlit** | Dash, Gradio, Flask | Need REST API, more control |
| **Pandas** | (Keep for Excel I/O) | - |
| **Polars** | Pandas, DuckDB | Smaller data, SQL preference |
| **Plotly** | Altair, Matplotlib | Declarative style, static images |
| **Openpyxl** | xlrd (read-only) | Only reading Excel |
| **XlsxWriter** | Openpyxl | Need to read AND write |

---

## Interview Questions

### Q1: "Why are your dependencies unpinned?"

**Answer**:
> "For a demo/portfolio project, unpinned versions ensure users always get the latest features and bug fixes when they clone the repo. In production, I would pin exact versions using `pip freeze > requirements.txt` or a lock file to ensure reproducibility across environments."

### Q2: "How would you handle a dependency conflict?"

**Answer**:
> "I would:
> 1. Check `pip check` to identify conflicts
> 2. Use `pip show <package>` to see version requirements
> 3. Find a compatible version range
> 4. Consider using virtual environments to isolate dependencies
> 5. Use `pip install --upgrade-strategy eager` to resolve chains"

### Q3: "What's the difference between requirements.txt and setup.py?"

**Answer**:
> "`requirements.txt` is for applications—it lists exact packages to install. `setup.py` (or `pyproject.toml`) is for libraries—it declares abstract dependencies with flexible versions. A library might require `pandas>=1.0`, while an application pins `pandas==2.1.0`."

### Q4: "How would you add a new dependency?"

**Answer**:
> "1. Install it: `pip install new-package`
> 2. Test the application
> 3. Add to `requirements.txt`: `echo new-package >> requirements.txt`
> 4. If pinning: `pip freeze | grep new-package >> requirements.txt`
> 5. Commit both the code changes and updated requirements"

### Q5: "Why use both Pandas AND Polars?"

**Answer**:
> "Each library has strengths:
> - **Polars**: 10-100x faster for data operations, used for the core comparison
> - **Pandas**: Superior Excel file handling, needed because Polars can't read Excel from bytes
> 
> I use the right tool for each task rather than forcing one library to do everything."

### Q6: "What would happen if Streamlit released a breaking change?"

**Answer**:
> "With unpinned versions, the app could break when users install it. To prevent this:
> 1. Pin versions in production
> 2. Set up CI/CD to test against latest versions
> 3. Subscribe to release notes of critical dependencies
> 4. Use dependabot or renovate for automated update PRs"

---

## Quick Reference

### Installation Commands

```bash
# Install all dependencies
pip install -r requirements.txt

# Install with specific version
pip install streamlit==1.28.0

# Upgrade all packages
pip install --upgrade -r requirements.txt

# Generate lock file
pip freeze > requirements.lock

# Install in editable mode (for development)
pip install -e .
```

### Useful pip Commands

| Command | Purpose |
|---------|---------|
| `pip list` | Show installed packages |
| `pip show pandas` | Show package details |
| `pip check` | Verify dependency compatibility |
| `pip freeze` | Output installed versions |
| `pip uninstall streamlit` | Remove a package |

---

*This documentation explains every dependency for interview preparation.*
