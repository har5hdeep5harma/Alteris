# 🗂️ Alteris - Complete Project Documentation

> **Master Documentation Hub - Your Guide to Understanding, Explaining, and Defending Every Aspect of This Project**

---

## 📖 Table of Contents

1. [Project Summary](#project-summary)
2. [Architecture Overview](#architecture-overview)
3. [Technology Stack Deep Dive](#technology-stack-deep-dive)
4. [File Structure & Connections](#file-structure--connections)
5. [Key Concepts Implemented](#key-concepts-implemented)
6. [Interview Preparation Guide](#interview-preparation-guide)
7. [Common Interview Questions & Answers](#common-interview-questions--answers)

---

## Project Summary

**Alteris** is a web-based data comparison tool that allows users to upload two datasets (a "base" and a "current" version) and generates a comprehensive difference report. Think of it as **"GitHub Diff for Data"**.

### What Problem Does It Solve?

In the real world, data analysts, QA engineers, and database administrators often need to:
- Compare two versions of a CSV/Excel export to find what changed
- Audit data migrations to ensure nothing was lost or corrupted
- Track changes in reports over time
- Validate ETL (Extract, Transform, Load) pipelines

**Without Alteris**: They would manually scan rows/columns in Excel, use complex VLOOKUPs, or write custom scripts.

**With Alteris**: Upload two files, select a key column, and get an instant, interactive report with cell-level highlighting.

---

## Architecture Overview

### Monolithic Architecture

This project uses a **Monolithic Architecture** pattern, meaning:

```
┌─────────────────────────────────────────────────────────────────┐
│                         app.py                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │   UI Layer  │  │  Business   │  │      Data Access        │  │
│  │  (Streamlit │◄─┤   Logic     │◄─┤  (Polars DataFrames)    │  │
│  │  Components)│  │  (Diffing)  │  │                         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Why Monolithic for This Project?**

| Reason | Explanation |
|--------|-------------|
| **Simplicity** | Single file is easier to deploy, debug, and understand |
| **Streamlit's Nature** | Streamlit apps are typically single-file applications |
| **Small Scope** | For a focused tool like this, microservices would be overkill |
| **Rapid Prototyping** | Faster development cycle without managing multiple services |

**When Would You Choose Microservices Instead?**

- If you needed to scale the comparison engine independently
- If multiple frontends (web, mobile, API) needed to access the same logic
- If you had separate teams working on different features
- If the application grew to include user authentication, scheduling, etc.

---

## Technology Stack Deep Dive

### Why These Libraries Were Chosen

| Library | Purpose | Why This Over Alternatives? |
|---------|---------|----------------------------|
| **Streamlit** | Web UI Framework | Fastest way to build data apps in Python. No HTML/CSS/JS needed. |
| **Polars** | Data Processing | 10-100x faster than Pandas for large datasets. Memory efficient. |
| **Pandas** | Excel File Reading | Polars can't read Excel from bytes directly; Pandas bridges this gap. |
| **Plotly** | Visualizations | Interactive charts that work out-of-the-box with Streamlit. |
| **Openpyxl** | Excel Reading | Required by Pandas to read `.xlsx` files. |
| **XlsxWriter** | Excel Writing | Creates the downloadable Excel report with multiple sheets. |

### Alternative Technologies Comparison

#### For UI Framework (Instead of Streamlit)

| Alternative | Pros | Cons | Why Not Chosen |
|-------------|------|------|----------------|
| **Flask/Django** | Full control, REST APIs | Requires frontend knowledge (React/Vue) | Too complex for this use case |
| **Dash** | Good for dashboards | Steeper learning curve than Streamlit | Streamlit is simpler |
| **Gradio** | Great for ML demos | Less flexible for data apps | Not optimized for data comparison |

#### For Data Processing (Instead of Polars)

| Alternative | Pros | Cons | Why Not Chosen |
|-------------|------|------|----------------|
| **Pandas** | Industry standard, huge community | Slow for large datasets, memory hog | Performance is critical for big files |
| **Dask** | Parallel processing | Complex setup, overhead for small data | Overkill for this use case |
| **PySpark** | Enterprise-grade big data | Requires cluster setup | Way too complex |

---

## File Structure & Connections

```
Alteris/
├── app.py                    # 🧠 Main application (ALL logic lives here)
├── requirements.txt          # 📦 Dependencies list
├── README.md                 # 📄 Project documentation
├── LICENSE                   # ⚖️ MIT License
├── Sample Data/              # 📁 Example datasets for testing
│   ├── Dataset 1/            # Small test data (5 rows each)
│   │   ├── small data 1.csv  # Base dataset
│   │   └── small data 2.csv  # Current dataset
│   └── Dataset 2/            # Larger test data (25 rows each)
│       ├── lenghthy data 1.csv
│       └── lenghthy data 2.csv
└── docs/                     # 📚 This documentation folder
    ├── PROJECT_OVERVIEW.md   # You are here
    ├── app_py.md             # Detailed app.py documentation
    ├── requirements_txt.md   # Dependencies documentation
    └── Sample Data/          # Sample data documentation
        ├── Dataset 1/
        │   ├── small_data_1_csv.md
        │   └── small_data_2_csv.md
        └── Dataset 2/
            ├── lenghthy_data_1_csv.md
            └── lenghthy_data_2_csv.md
```

### How Files Connect

```
┌─────────────────┐
│ requirements.txt│ ─── Lists packages that app.py imports
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│     app.py      │◄────│   Sample Data/  │
│                 │     │ (Test datasets) │
│ Uses libraries: │     └─────────────────┘
│ - streamlit     │
│ - polars        │
│ - pandas        │
│ - plotly        │
└─────────────────┘
```

---

## Key Concepts Implemented

### 1. **Caching with Decorators** (`@st.cache_data`)
The `@st.cache_data` decorator stores function results in memory, preventing redundant computation when the same inputs are provided again.

### 2. **Type Hints** (`List[str]`, `Dict[str, Any]`)
Python type hints improve code readability and enable IDE autocompletion and error checking.

### 3. **Outer Join Algorithm**
The core comparison uses a database-style outer join to find added, removed, and modified rows.

### 4. **Session State Management**
Streamlit's `st.session_state` persists data across user interactions (button clicks, file uploads).

### 5. **Lazy Evaluation with Polars**
Polars uses lazy evaluation for efficient query execution, computing only what's needed.

### 6. **Method Chaining**
The code uses method chaining (e.g., `df.filter().with_columns().select()`) for readable, efficient transformations.

### 7. **Data Styling with Pandas Styler**
The `highlight_diff` function uses Pandas' `Styler` API to apply conditional formatting.

---

## Interview Preparation Guide

### Key Topics You Must Know

1. **Data Structures**: DataFrames, Dictionaries, Lists, Sets
2. **Algorithms**: Outer Join, Set Operations (intersection, difference)
3. **Web Frameworks**: How Streamlit's execution model works
4. **Performance**: Caching, Lazy Evaluation, Memory Efficiency
5. **File I/O**: Reading/Writing CSV and Excel files
6. **Data Visualization**: Histograms, Box Plots, Interactive Charts

### Be Ready to Explain

- Why you chose Polars over Pandas
- How the caching mechanism improves performance
- The algorithm for detecting modified rows
- How you handle schema differences (added/removed columns)
- Why you used session state instead of global variables

---

## Common Interview Questions & Answers

### Q1: "Why did you choose Polars over Pandas?"

**Answer**: 
"Polars is a modern DataFrame library built in Rust that offers 10-100x faster performance than Pandas for most operations. For a data comparison tool where users might upload large datasets, performance is critical. Polars also has better memory efficiency because it uses Apache Arrow format internally and supports lazy evaluation, meaning it only computes what's needed. However, I still use Pandas for Excel file reading because Polars can't read Excel files directly from bytes in memory."

### Q2: "How does your diffing algorithm work?"

**Answer**:
"The algorithm uses an outer join on the key columns selected by the user. Here's the logic:
1. Join the base and current DataFrames on the key columns
2. Rows where current-side columns are NULL = Removed rows
3. Rows where base-side columns are NULL = Added rows
4. Rows where both sides exist but values differ = Modified rows

I use horizontal any (`pl.any_horizontal`) to check if ANY column value changed across the row, then track which specific columns changed."

### Q3: "What is `@st.cache_data` and why did you use it?"

**Answer**:
"It's a Streamlit decorator that memoizes function results. When you call a cached function with the same arguments, Streamlit returns the stored result instead of re-executing the function. This is crucial for file processing because re-reading and re-parsing files on every UI interaction would be extremely slow. The cache is invalidated when function arguments change or when the user uploads a new file."

### Q4: "Why is this a monolithic application? When would you split it?"

**Answer**:
"A monolithic architecture makes sense here because:
1. Streamlit is designed for single-file apps
2. The scope is focused - it does one thing well
3. Easier to deploy (one file to `streamlit run`)

I would consider splitting if:
- Multiple teams needed to work on different features
- We needed an API for programmatic access
- We wanted to scale the comparison engine independently
- We added authentication, scheduling, or other complex features"

### Q5: "How do you handle different file formats?"

**Answer**:
"The `load_dataframe` function checks the file extension:
- For `.csv` files: Polars reads directly from bytes using `pl.read_csv()`
- For `.xlsx` files: Since Polars can't read Excel from bytes, I use Pandas as an intermediary with `pd.read_excel()`, then convert to Polars with `pl.from_pandas()`

This shows I understand each library's limitations and can bridge them effectively."

### Q6: "What happens if someone uploads a 10GB file?"

**Answer**:
"There are several considerations:
1. **Streamlit's limit**: By default, Streamlit limits uploads to 200MB (configurable)
2. **Memory**: The file needs to fit in memory twice (base + current)
3. **Browser timeout**: Large uploads might timeout

To handle larger files, I could:
- Implement chunked processing with Polars' `scan_csv()` for lazy reading
- Add a progress bar for user feedback
- Use a distributed processing framework like Dask or PySpark
- Stream results instead of loading everything at once"

---

## Quick Reference Card

### Key Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py

# Run with custom port
streamlit run app.py --server.port 8080
```

### Key Functions at a Glance

| Function | Purpose | Key Technique |
|----------|---------|---------------|
| `load_dataframe()` | Load CSV/Excel files | Caching, Format detection |
| `compare_schemas()` | Find column changes | Set operations |
| `compare_data()` | Find row changes | Outer join, Filtering |
| `to_excel()` | Export report | Multi-sheet Excel |
| `highlight_diff()` | Color-code changes | Pandas Styler |

---

## Next Steps

📁 **Navigate to individual file documentation:**

- [app.py Documentation](app_py.md) - Complete code walkthrough
- [requirements.txt Documentation](requirements_txt.md) - Dependencies explained
- [Sample Data Documentation](Sample%20Data/) - Understanding test datasets

---

*Generated for interview preparation and project understanding.*
