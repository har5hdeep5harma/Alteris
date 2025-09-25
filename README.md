<iframe src="https://drive.google.com/file/d/14YuMQWmUeFQgXmurgmWKjXYr85IcMUCq/preview" width="640" height="480" allow="autoplay"></iframe>

# Alteris 🕵️

> **When numbers drift and tables sway, we light the path and show the way.**

---

**Alteris** is a high-performance, interactive web application designed to find the difference between two datasets.  
Think of it as a **"GitHub Diff" for your data files**.

It automates the tedious and error-prone task of manually comparing spreadsheets or CSVs, providing a clear, detailed, and actionable report on every change that occurred between a **"base" (old)** and a **"current" (new)** version of your data.

---

## ✨ Key Features

### 🏛️ Schema Comparison  
- Instantly detect structural changes to your data.
- **Columns Added/Removed**: Get a clear list of columns that have been added or removed.
- **Data Type Changes**: Identify columns where the data type has changed (e.g., from Integer to String).

### 📝 Comprehensive Row-Level Diffing  
- Understand exactly which records have changed.
- **Added Rows**: View all the new rows in a clean table.  
- **Removed Rows**: Isolate the rows that have been deleted.  
- **Modified Rows**: See a complete list of rows that were updated.

### 🎨 Cell-Level Highlighting  
The "Modified Rows" view is enhanced with intuitive color-coding, making it effortless to spot the exact changes:  
- 🟨 **Old values** are highlighted in yellow.  
- 🟦 **New values** are highlighted in blue.

### 📈 Column Profiling & Distribution Analysis  
Go beyond simple diffing to understand statistical shifts:  
- **Summary Statistics**: Compare metrics like mean, standard deviation, min, max, and null counts for any column.  
- **Interactive Visualizations**: View overlaid histograms to visually compare the distribution of data between the two datasets.

### 📤 Export to Excel  
Download the complete, detailed diff report (Added, Removed, and Modified rows) as a multi-sheet Excel file with a single click.

### 📁 Broad File Support  
Upload your data easily, with support for both `.csv` and `.xlsx` (Excel) files.

---

## 🚀 The Technology Stack  

Alteris is built with a modern, high-performance Python stack:

- **Frontend**: [Streamlit](https://streamlit.io) – For creating the beautiful and interactive web user interface.  
- **Backend Engine**: [Polars](https://www.pola.rs/) – For blazing-fast, memory-efficient data manipulation and comparison logic.  
- **File Handling**: [Pandas](https://pandas.pydata.org/) & [Openpyxl](https://openpyxl.readthedocs.io/) – For robustly handling Excel file uploads.  
- **Visualizations**: [Plotly](https://plotly.com/python/) – For generating the interactive distribution charts.  
- **Excel Export**: [XlsxWriter](https://xlsxwriter.readthedocs.io/) – For creating the downloadable Excel reports.

---

## ⚙️ Getting Started  

### Prerequisites  
- Python 3.9 or higher  
- `pip` and `venv`  

### Installation & Launch  

1. **Clone the repository:**

   ```bash
   git clone https://github.com/har5hdeep5harma/Alteris
   cd alteris

2. **Create and activate a virtual environment:**

    On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```


## 📖 How to Use

1. Upload Base File:
Use the left-hand uploader to select the "base" (old) version of your dataset.

2. Upload Current File:
Use the right-hand uploader to select the "current" (new) version of your dataset.

3. Select Key Column(s):
From the dropdown menu, choose the column(s) that uniquely identify each row (e.g., transaction_id, employee_id). This is crucial for matching rows.

4. Generate Report:
Click the "🚀 Generate Diff Report" button.

5. Explore Results:
Investigate the detailed changes in the report tabs and download the Excel file if needed.

📄 License
---

This project is licensed under the MIT License. See the LICENSE file for details.

---
### Happy Diffing!