# 📁 Sample Data Documentation

> **Understanding the Test Datasets Used for Demonstration**

---

## 📖 Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Purpose of Sample Data](#purpose-of-sample-data)
4. [Dataset 1: Employee Data (Small)](#dataset-1-employee-data-small)
5. [Dataset 2: Transaction Data (Large)](#dataset-2-transaction-data-large)
6. [Testing Scenarios](#testing-scenarios)
7. [Interview Points](#interview-points)

---

## Overview

The `Sample Data/` folder contains pre-made datasets for testing and demonstrating the Alteris application. These files serve multiple purposes:

1. **Quick Demo**: Users can immediately test the app without preparing their own data
2. **Edge Case Testing**: Datasets are designed to trigger various comparison scenarios
3. **Documentation**: Show potential users what kinds of data the app can handle

---

## Directory Structure

```
Sample Data/
├── Dataset 1/                    # Small, simple datasets (5 rows)
│   ├── small data 1.csv          # Base dataset (old version)
│   └── small data 2.csv          # Current dataset (new version)
└── Dataset 2/                    # Larger, realistic datasets (25 rows)
    ├── lenghthy data 1.csv       # Base dataset
    └── lenghthy data 2.csv       # Current dataset
```

---

## Purpose of Sample Data

### Why Include Sample Data?

| Reason | Explanation |
|--------|-------------|
| **Onboarding** | New users can test immediately without preparing data |
| **Validation** | Developers can verify the app works after changes |
| **Demo** | Showcase features during presentations |
| **Testing** | Cover different comparison scenarios |

### Design Principles

The sample datasets are designed to demonstrate:
- ✅ Added rows
- ✅ Removed rows  
- ✅ Modified rows (changed values)
- ✅ Schema changes (added/removed columns)
- ✅ Different data types (numeric, string)

---

## Dataset 1: Employee Data (Small)

### File: small data 1.csv (Base)

```csv
employee_id,first_name,last_name,department,salary,temp_badge_id,tempui
101,Binod,Kumar,Engineering,90000,T101,1
102,Devendra,Singh,Marketing,75000,T102,2
103,Amitabh,Bachchan,Engineering,110000,T103,3
104,Bhupendra,Jogi,Sales,85000,T104,4
```

#### Schema Analysis

| Column | Data Type | Purpose | Notes |
|--------|-----------|---------|-------|
| `employee_id` | Integer | **Primary Key** | Unique identifier for each employee |
| `first_name` | String | First name | |
| `last_name` | String | Last name | |
| `department` | String | Department | Categorical |
| `salary` | Integer | Annual salary | Numeric for calculations |
| `temp_badge_id` | String | Temporary badge | **Will be removed in v2** |
| `tempui` | Integer | Temporary UI flag | **Will be removed in v2** |

---

### File: small data 2.csv (Current)

```csv
employee_id,first_name,last_name,department,salary,performance_rating
101,Alice,Smith,Engineering,90000,4.5
102,Bob,Johnson,Marketing,82000,4.2
103,Charlie,Brown,Engineering,110000,4.8
105,Eve,Adams,Sales,88000,4.1
```

#### Schema Analysis

| Column | Data Type | Purpose | Notes |
|--------|-----------|---------|-------|
| `employee_id` | Integer | **Primary Key** | Same as base |
| `first_name` | String | First name | **Values changed** |
| `last_name` | String | Last name | **Values changed** |
| `department` | String | Department | Same structure |
| `salary` | Integer | Annual salary | **Some values changed** |
| `performance_rating` | Float | Rating 1-5 | **NEW column** |

---

### Comparison Results (Dataset 1)

When comparing these two files with `employee_id` as the key:

#### Schema Changes
```
┌─────────────────────────────────────────────────────────────┐
│ SCHEMA COMPARISON RESULTS                                   │
├─────────────────────────────────────────────────────────────┤
│ ➕ Columns Added:    [performance_rating]                    │
│ ➖ Columns Removed:  [temp_badge_id, tempui]                 │
│ 🔄 Type Changes:     None                                    │
└─────────────────────────────────────────────────────────────┘
```

#### Row-Level Changes
```
┌─────────────────────────────────────────────────────────────┐
│ ROW COMPARISON RESULTS                                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ➕ ADDED ROWS (1):                                           │
│    employee_id=105 (Eve Adams, Sales, $88000)               │
│                                                              │
│ ➖ REMOVED ROWS (1):                                         │
│    employee_id=104 (Bhupendra Jogi, Sales, $85000)          │
│                                                              │
│ ✏️ MODIFIED ROWS (3):                                        │
│    employee_id=101: first_name, last_name changed           │
│    employee_id=102: first_name, last_name, salary changed   │
│    employee_id=103: first_name, last_name changed           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### Detailed Change Breakdown

| employee_id | Change Type | What Changed |
|-------------|-------------|--------------|
| 101 | Modified | Binod Kumar → Alice Smith |
| 102 | Modified | Devendra Singh → Bob Johnson, salary 75000 → 82000 |
| 103 | Modified | Amitabh Bachchan → Charlie Brown |
| 104 | Removed | Entire row deleted |
| 105 | Added | New employee (Eve Adams) |

---

## Dataset 2: Transaction Data (Large)

### File: lenghthy data 1.csv & lenghthy data 2.csv

Both files contain **25 identical rows** of e-commerce transaction data.

#### Sample Row
```csv
transaction_id,product_id,product_name,category,quantity,unit_price,total_price,customer_id,customer_region,salesperson_id,transaction_date,payment_method,discount_applied,shipping_status,legacy_order_ref
d8e8b79a-720c-4b53-9a3d-2b7e9b0a1c6a,P1001,Quantum Laptop,Electronics,1,1200.00,1200.00,C5001,North,S101,2025-04-15,Credit Card,0.00,Shipped,LGC-88720
```

#### Schema Analysis

| Column | Data Type | Purpose | Notes |
|--------|-----------|---------|-------|
| `transaction_id` | UUID | **Primary Key** | Globally unique identifier |
| `product_id` | String | Product code | References product catalog |
| `product_name` | String | Product name | Denormalized for convenience |
| `category` | String | Product category | Electronics, Accessories, Gaming, etc. |
| `quantity` | Integer | Items purchased | |
| `unit_price` | Float | Price per unit | In USD |
| `total_price` | Float | Line total | `quantity * unit_price * (1 - discount)` |
| `customer_id` | String | Customer code | References customer table |
| `customer_region` | String | Geographic region | North, South, East, West |
| `salesperson_id` | String | Sales rep code | References employee table |
| `transaction_date` | Date | Sale date | YYYY-MM-DD format |
| `payment_method` | String | Payment type | Credit Card, PayPal |
| `discount_applied` | Float | Discount rate | 0.00 to 0.05 (0% to 5%) |
| `shipping_status` | String | Delivery status | Shipped, Processing |
| `legacy_order_ref` | String | Old system reference | Migration artifact |

---

### Data Distribution

#### By Category
```
Category      | Count | Total Revenue
──────────────┼───────┼──────────────
Electronics   |   9   | $9,582.50
Accessories   |   8   | $527.50
Gaming        |   4   | $2,000.00
Audio         |   2   | $300.00
Mobile        |   2   | $1,560.00
Networking    |   1   | $120.00
Storage       |   1   | $190.00
```

#### By Region
```
Region | Transactions | Top Product
───────┼──────────────┼─────────────
North  |      7       | Quantum Laptop
West   |      6       | Orion Monitor
East   |      5       | Eclipse VR Headset
South  |      7       | Starlight Mouse
```

---

### Why These Files Are Identical

Dataset 2 files (`lenghthy data 1.csv` and `lenghthy data 2.csv`) contain identical data. This demonstrates:

1. **No Changes Scenario**: Shows how the app behaves when data hasn't changed
2. **Performance Testing**: Larger dataset tests processing speed
3. **Realistic Data**: Shows typical e-commerce transaction structure

**Expected Output**: 
- 0 Added Rows
- 0 Removed Rows  
- 0 Modified Rows
- "No row-level changes detected" message

---

## Testing Scenarios

### Scenario 1: Basic Diff (Dataset 1)
**Files**: `small data 1.csv` → `small data 2.csv`
**Key Column**: `employee_id`
**Tests**:
- ✅ Added rows detection
- ✅ Removed rows detection
- ✅ Modified rows with cell highlighting
- ✅ Schema change detection (new/removed columns)

### Scenario 2: No Changes (Dataset 2)
**Files**: `lenghthy data 1.csv` → `lenghthy data 2.csv`
**Key Column**: `transaction_id`
**Tests**:
- ✅ Identical file handling
- ✅ "No changes" message display
- ✅ Performance with 25 rows

### Scenario 3: Composite Key
**Files**: `lenghthy data 1.csv` → `lenghthy data 2.csv`
**Key Columns**: `transaction_id, product_id` (multi-select)
**Tests**:
- ✅ Multi-column key handling
- ✅ Join on multiple columns

### Scenario 4: Column Profiling
**File**: Any file
**Test Column**: `unit_price` or `total_price`
**Tests**:
- ✅ Numeric statistics (mean, std, min, max)
- ✅ Distribution histogram
- ✅ Comparison visualization

---

## Data Quality Observations

### Dataset 1 Observations

| Observation | Column | Details |
|-------------|--------|---------|
| **Temporary columns** | `temp_badge_id`, `tempui` | Likely development artifacts removed in v2 |
| **Complete name change** | `first_name`, `last_name` | Suggests data anonymization |
| **Employee turnover** | - | 1 removed, 1 added |
| **Salary increase** | `salary` (102) | 75000 → 82000 (+9.3%) |

### Dataset 2 Observations

| Observation | Column | Details |
|-------------|--------|---------|
| **UUID keys** | `transaction_id` | Best practice for distributed systems |
| **Denormalization** | `product_name` | Stored with transaction for query performance |
| **Legacy reference** | `legacy_order_ref` | Indicates system migration |
| **Date range** | `transaction_date` | Apr 15 - Jun 28, 2025 |

---

## Interview Points

### Q: "Why did you include sample data in your project?"

**Answer**:
> "Sample data serves multiple purposes:
> 1. **User Experience**: New users can test immediately without data preparation
> 2. **Documentation**: Shows what kinds of data the app can handle
> 3. **Testing**: Allows me to verify the app works after code changes
> 4. **Demo**: Essential for presentations and interviews like this one"

### Q: "How did you design the sample datasets?"

**Answer**:
> "I designed them to trigger all major features:
> - Dataset 1 has rows that are added, removed, and modified, plus schema changes
> - Dataset 2 has realistic e-commerce data with various data types
> - The first dataset is small (5 rows) for quick demos
> - The second is larger (25 rows) to show the app handles more data"

### Q: "Why use UUIDs for transaction_id?"

**Answer**:
> "UUIDs (Universally Unique Identifiers) are ideal for:
> - **Distributed systems**: Can be generated anywhere without collision
> - **Security**: Unpredictable, can't be guessed or enumerated
> - **Merging data**: No conflicts when combining datasets from different sources
> 
> The format `d8e8b79a-720c-4b53-9a3d-2b7e9b0a1c6a` is UUID v4 (random)."

### Q: "What's the purpose of the legacy_order_ref column?"

**Answer**:
> "It represents a common real-world scenario: system migration. When companies switch from an old system to a new one, they often keep a reference to the old ID for:
> - **Auditing**: Trace back to original records
> - **Customer support**: Handle queries about old orders
> - **Data reconciliation**: Compare new and old systems during transition"

### Q: "Why is product_name stored with each transaction?"

**Answer**:
> "This is **denormalization** - storing redundant data for query performance. In a normalized design, you'd only store `product_id` and join to a products table. But:
> - Joins are expensive for reporting
> - Product names might change, but historical transactions should reflect the original name
> - For analytics, you often want the name without joining
> 
> The trade-off is increased storage for faster reads."

---

## CSV File Format Details

### Common CSV Properties

| Property | Value | Standard |
|----------|-------|----------|
| **Encoding** | UTF-8 | Universal character support |
| **Delimiter** | Comma (`,`) | RFC 4180 standard |
| **Header** | First row | Column names |
| **Line Ending** | CRLF or LF | Platform-dependent |
| **Quoting** | Double quotes when needed | For values with commas |

### Why CSV for Sample Data?

| Format | Pros | Cons | Why Not |
|--------|------|------|---------|
| **CSV** ✓ | Universal, readable, small | No types | Chosen |
| **Excel** | Rich formatting | Larger, binary | Overkill for samples |
| **Parquet** | Efficient, typed | Not human-readable | Too technical |
| **JSON** | Web-friendly | Verbose for tabular data | Poor fit |

---

*This documentation explains the sample data structure for interview preparation.*
