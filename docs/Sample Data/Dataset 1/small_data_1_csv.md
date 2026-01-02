# 📊 small data 1.csv - Base Dataset Documentation

> **The "Before" Snapshot: Employee Data for Comparison**

---

## File Overview

| Property | Value |
|----------|-------|
| **File Path** | `Sample Data/Dataset 1/small data 1.csv` |
| **Role** | Base (Old) Dataset |
| **Rows** | 4 data rows + 1 header |
| **Columns** | 7 |
| **File Size** | ~350 bytes |
| **Encoding** | UTF-8 |

---

## Complete File Content

```csv
employee_id,first_name,last_name,department,salary,temp_badge_id,tempui
101,Binod,Kumar,Engineering,90000,T101,1
102,Devendra,Singh,Marketing,75000,T102,2
103,Amitabh,Bachchan,Engineering,110000,T103,3
104,Bhupendra,Jogi,Sales,85000,T104,4
```

---

## Schema Definition

| Column | Data Type | Nullable | Description | Example |
|--------|-----------|----------|-------------|---------|
| `employee_id` | Integer | No | **Primary Key** - Unique employee identifier | 101 |
| `first_name` | String | No | Employee's first name | Binod |
| `last_name` | String | No | Employee's last name | Kumar |
| `department` | String | No | Department name (categorical) | Engineering |
| `salary` | Integer | No | Annual salary in currency units | 90000 |
| `temp_badge_id` | String | No | Temporary badge identifier | T101 |
| `tempui` | Integer | No | Temporary UI flag | 1 |

---

## Column-by-Column Analysis

### Column 1: employee_id

```
Type: Integer
Role: Primary Key (Unique Identifier)
Values: [101, 102, 103, 104]
```

**Purpose**: Uniquely identifies each employee record. This is the column you select as the "key column" when comparing datasets in Alteris.

**Why Integer IDs?**:
- Sequential and predictable
- Efficient for database indexing
- Easy to reference in logs and errors

**Alternative Approaches**:
| Type | Example | Pros | Cons |
|------|---------|------|------|
| Integer | 101, 102 | Simple, fast | Predictable, limited scale |
| UUID | `a1b2c3d4-...` | Global uniqueness | Longer, harder to debug |
| Natural Key | "EMP-KUMAR-001" | Human-readable | Can change, duplicates |

---

### Column 2: first_name

```
Type: String
Values: [Binod, Devendra, Amitabh, Bhupendra]
Unique: 4 (all unique)
```

**Data Pattern**: Indian first names (likely representing the developer's region)

**Note for Comparison**: In `small data 2.csv`, these are completely replaced with Western names (Alice, Bob, Charlie, Eve). This simulates data anonymization or a complete data refresh.

---

### Column 3: last_name

```
Type: String
Values: [Kumar, Singh, Bachchan, Jogi]
Unique: 4 (all unique)
```

**Data Pattern**: Indian last names

**Note for Comparison**: Also completely replaced in the "current" version.

---

### Column 4: department

```
Type: String (Categorical)
Values: [Engineering, Marketing, Sales]
Distribution:
  - Engineering: 2 (50%)
  - Marketing: 1 (25%)
  - Sales: 1 (25%)
```

**Purpose**: Categorizes employees by their organizational unit.

**Interview Point - Categorical Data**:
> "Categorical columns have a limited set of distinct values. For analytics, we might encode these as integers or use one-hot encoding for machine learning."

---

### Column 5: salary

```
Type: Integer
Values: [90000, 75000, 110000, 85000]
Statistics:
  - Min: 75,000
  - Max: 110,000
  - Mean: 90,000
  - Std Dev: 14,719.6
```

**Purpose**: Annual compensation in currency units (assumed USD).

**Note for Comparison**: Employee 102's salary increases from 75,000 → 82,000 in the "current" version.

---

### Column 6: temp_badge_id

```
Type: String
Values: [T101, T102, T103, T104]
Pattern: "T" + employee_id
```

**Purpose**: Temporary security badge identifier.

**Why "temp"?**: The column name suggests this is transitional data. In `small data 2.csv`, this column is **removed entirely**. This demonstrates schema changes (column removal) in Alteris.

---

### Column 7: tempui

```
Type: Integer
Values: [1, 2, 3, 4]
Pattern: Sequential
```

**Purpose**: Temporary UI-related flag (possibly display order or testing).

**Note**: Also **removed** in the "current" version, demonstrating column removal.

---

## Row-by-Row Analysis

### Row 1: Employee 101
```csv
101,Binod,Kumar,Engineering,90000,T101,1
```

**In Current Version**:
- ✏️ first_name: Binod → Alice
- ✏️ last_name: Kumar → Smith
- ➡️ salary: 90000 (unchanged)
- ➡️ department: Engineering (unchanged)

**Change Type**: Modified (name change only)

---

### Row 2: Employee 102
```csv
102,Devendra,Singh,Marketing,75000,T102,2
```

**In Current Version**:
- ✏️ first_name: Devendra → Bob
- ✏️ last_name: Singh → Johnson
- ✏️ salary: 75000 → 82000 (+9.3% increase)
- ➡️ department: Marketing (unchanged)

**Change Type**: Modified (name + salary change)

---

### Row 3: Employee 103
```csv
103,Amitabh,Bachchan,Engineering,110000,T103,3
```

**In Current Version**:
- ✏️ first_name: Amitabh → Charlie
- ✏️ last_name: Bachchan → Brown
- ➡️ salary: 110000 (unchanged)
- ➡️ department: Engineering (unchanged)

**Change Type**: Modified (name change only)

---

### Row 4: Employee 104
```csv
104,Bhupendra,Jogi,Sales,85000,T104,4
```

**In Current Version**: 
- ❌ This row is **completely removed**

**Change Type**: Removed

---

## Statistics Summary

### Numeric Columns

| Statistic | employee_id | salary | tempui |
|-----------|-------------|--------|--------|
| Count | 4 | 4 | 4 |
| Min | 101 | 75,000 | 1 |
| Max | 104 | 110,000 | 4 |
| Mean | 102.5 | 90,000 | 2.5 |
| Std Dev | 1.29 | 14,719 | 1.29 |

### String Columns

| Column | Unique Values | Most Common |
|--------|---------------|-------------|
| first_name | 4 | - (all unique) |
| last_name | 4 | - (all unique) |
| department | 3 | Engineering (2) |
| temp_badge_id | 4 | - (all unique) |

---

## How This File Is Used

### In Alteris Workflow

```
┌────────────────────────────────────────────────────────────┐
│                    ALTERIS WORKFLOW                         │
├────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Upload "small data 1.csv" as Base Dataset               │
│     └─► This file                                           │
│                                                              │
│  2. Upload "small data 2.csv" as Current Dataset            │
│     └─► The "after" version                                 │
│                                                              │
│  3. Select Key Column: "employee_id"                        │
│     └─► How to match rows between files                     │
│                                                              │
│  4. Click "Generate Difference Report"                      │
│                                                              │
│  5. View Results:                                           │
│     • Schema: temp_badge_id & tempui removed                │
│     • Schema: performance_rating added                      │
│     • Rows: Employee 105 added                              │
│     • Rows: Employee 104 removed                            │
│     • Rows: Employees 101-103 modified                      │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

---

## Interview Points

### Q: "What makes employee_id a good primary key?"

**Answer**:
> "A good primary key should be:
> 1. **Unique**: No duplicates (employee_id is unique per employee)
> 2. **Immutable**: Never changes (employee IDs are permanent)
> 3. **Non-null**: Always has a value
> 4. **Simple**: Single column when possible
> 
> Employee IDs fit all these criteria, making them ideal for matching rows between datasets."

### Q: "Why are there temporary columns (temp_badge_id, tempui)?"

**Answer**:
> "These likely represent development artifacts or transitional data:
> - **temp_badge_id**: Possibly a placeholder during system migration
> - **tempui**: Maybe a UI ordering field for testing
> 
> In the 'current' version, these are removed, demonstrating that our app correctly detects schema changes (column removal)."

### Q: "How would you handle nulls in this data?"

**Answer**:
> "This sample has no nulls, but in real data:
> 1. **Detection**: Polars shows null counts in profiling
> 2. **Comparison**: Nulls compare as equal to nulls, not to values
> 3. **Display**: We'd show null counts in the statistics table
> 4. **Filtering**: Users might want to filter to only null changes"

---

## Related Files

| File | Relationship | Purpose |
|------|--------------|---------|
| [small data 2.csv](small_data_2_csv.md) | Compare With | The "after" version |
| [app.py](../../app_py.md) | Processed By | Main application |
| [README.md](README.md) | Overview | Sample data documentation |

---

*This documentation provides complete understanding of the base dataset.*
