# 📊 small data 2.csv - Current Dataset Documentation

> **The "After" Snapshot: Updated Employee Data for Comparison**

---

## File Overview

| Property | Value |
|----------|-------|
| **File Path** | `Sample Data/Dataset 1/small data 2.csv` |
| **Role** | Current (New) Dataset |
| **Rows** | 4 data rows + 1 header |
| **Columns** | 6 |
| **File Size** | ~280 bytes |
| **Encoding** | UTF-8 |

---

## Complete File Content

```csv
employee_id,first_name,last_name,department,salary,performance_rating
101,Alice,Smith,Engineering,90000,4.5
102,Bob,Johnson,Marketing,82000,4.2
103,Charlie,Brown,Engineering,110000,4.8
105,Eve,Adams,Sales,88000,4.1
```

---

## Schema Definition

| Column | Data Type | Nullable | Description | Example |
|--------|-----------|----------|-------------|---------|
| `employee_id` | Integer | No | **Primary Key** - Unique employee identifier | 101 |
| `first_name` | String | No | Employee's first name | Alice |
| `last_name` | String | No | Employee's last name | Smith |
| `department` | String | No | Department name (categorical) | Engineering |
| `salary` | Integer | No | Annual salary in currency units | 90000 |
| `performance_rating` | Float | No | **NEW** - Performance score (1.0-5.0) | 4.5 |

---

## Schema Changes from Base

### Columns Added
| Column | Type | Description |
|--------|------|-------------|
| `performance_rating` | Float | New performance metric (1.0-5.0 scale) |

### Columns Removed
| Column | Was Type | Reason |
|--------|----------|--------|
| `temp_badge_id` | String | Temporary data no longer needed |
| `tempui` | Integer | Development artifact removed |

**Net Change**: -1 column (7 → 6)

---

## Column-by-Column Analysis

### Column 1: employee_id

```
Type: Integer
Role: Primary Key
Values: [101, 102, 103, 105]
```

**Comparison to Base**:
- ✅ 101, 102, 103: Still exist
- ❌ 104: Removed (no longer in dataset)
- ➕ 105: New employee added

**Key Observation**: The IDs are not continuous (104 is missing), which is normal in real databases when records are deleted.

---

### Column 2: first_name

```
Type: String
Values: [Alice, Bob, Charlie, Eve]
```

**Comparison to Base**:
| employee_id | Base | Current | Change |
|-------------|------|---------|--------|
| 101 | Binod | Alice | Modified |
| 102 | Devendra | Bob | Modified |
| 103 | Amitabh | Charlie | Modified |
| 105 | - | Eve | New |

**Pattern**: All names changed to Western names (data anonymization scenario).

---

### Column 3: last_name

```
Type: String
Values: [Smith, Johnson, Brown, Adams]
```

**Comparison to Base**:
| employee_id | Base | Current | Change |
|-------------|------|---------|--------|
| 101 | Kumar | Smith | Modified |
| 102 | Singh | Johnson | Modified |
| 103 | Bachchan | Brown | Modified |
| 105 | - | Adams | New |

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

**Comparison to Base**: No changes to department assignments for existing employees.

---

### Column 5: salary

```
Type: Integer
Values: [90000, 82000, 110000, 88000]
Statistics:
  - Min: 82,000
  - Max: 110,000
  - Mean: 92,500
  - Std Dev: 11,958
```

**Comparison to Base**:
| employee_id | Base | Current | Change |
|-------------|------|---------|--------|
| 101 | 90,000 | 90,000 | Unchanged |
| 102 | 75,000 | 82,000 | +9.3% increase |
| 103 | 110,000 | 110,000 | Unchanged |
| 105 | - | 88,000 | New |

**Observation**: Only employee 102 received a salary increase (from 75,000 to 82,000).

---

### Column 6: performance_rating (NEW)

```
Type: Float
Values: [4.5, 4.2, 4.8, 4.1]
Statistics:
  - Min: 4.1
  - Max: 4.8
  - Mean: 4.4
  - Std Dev: 0.29
```

**Purpose**: New column added to track employee performance on a 1.0-5.0 scale.

**Rating Distribution**:
```
Rating | Employee | Interpretation
4.8    | 103      | Excellent
4.5    | 101      | Very Good
4.2    | 102      | Good
4.1    | 105      | Good
```

**Interview Point - Why Float for Ratings?**:
> "Float allows for decimal ratings (4.5, 4.2) which provide more granularity than integers. This enables:
> - More nuanced performance distinctions
> - Averaging across categories
> - Calculated ratings from multiple reviewers"

---

## Row-by-Row Analysis

### Row 1: Employee 101 (Modified)
```csv
101,Alice,Smith,Engineering,90000,4.5
```

**Changes from Base**:
| Field | Base Value | Current Value | Changed? |
|-------|------------|---------------|----------|
| employee_id | 101 | 101 | ❌ (Key) |
| first_name | Binod | Alice | ✅ |
| last_name | Kumar | Smith | ✅ |
| department | Engineering | Engineering | ❌ |
| salary | 90000 | 90000 | ❌ |
| performance_rating | - | 4.5 | ➕ New |

---

### Row 2: Employee 102 (Modified)
```csv
102,Bob,Johnson,Marketing,82000,4.2
```

**Changes from Base**:
| Field | Base Value | Current Value | Changed? |
|-------|------------|---------------|----------|
| employee_id | 102 | 102 | ❌ (Key) |
| first_name | Devendra | Bob | ✅ |
| last_name | Singh | Johnson | ✅ |
| department | Marketing | Marketing | ❌ |
| salary | 75000 | 82000 | ✅ (+9.3%) |
| performance_rating | - | 4.2 | ➕ New |

**Note**: This is the most changed row with 3 modified fields.

---

### Row 3: Employee 103 (Modified)
```csv
103,Charlie,Brown,Engineering,110000,4.8
```

**Changes from Base**:
| Field | Base Value | Current Value | Changed? |
|-------|------------|---------------|----------|
| employee_id | 103 | 103 | ❌ (Key) |
| first_name | Amitabh | Charlie | ✅ |
| last_name | Bachchan | Brown | ✅ |
| department | Engineering | Engineering | ❌ |
| salary | 110000 | 110000 | ❌ |
| performance_rating | - | 4.8 | ➕ New |

---

### Row 4: Employee 105 (Added)
```csv
105,Eve,Adams,Sales,88000,4.1
```

**Status**: This is a completely new row.

**Analysis**:
- New hire in Sales department
- Salary of 88,000 (above average for the dataset)
- Performance rating of 4.1 (lowest in this dataset, normal for new hire)

---

## Comparison Summary

### Visual Diff

```
BASE (small data 1.csv)              CURRENT (small data 2.csv)
──────────────────────────────────    ──────────────────────────────────
employee_id,first_name,last_name,    employee_id,first_name,last_name,
department,salary,temp_badge_id,     department,salary,performance_rating
tempui
                                      ↑ Columns changed!

101,Binod,Kumar,Engineering,         101,Alice,Smith,Engineering,
90000,T101,1                         90000,4.5
     ↑↑↑   ↑↑↑                            ↑↑↑  ↑↑↑  ↑↑
     Modified                             Modified + New col

102,Devendra,Singh,Marketing,        102,Bob,Johnson,Marketing,
75000,T102,2                         82000,4.2
     ↑↑↑      ↑↑↑         ↑↑↑↑           ↑↑  ↑↑↑    ↑↑↑↑↑  ↑↑
     Modified       Modified              Modified

103,Amitabh,Bachchan,Engineering,    103,Charlie,Brown,Engineering,
110000,T103,3                        110000,4.8
      ↑↑↑    ↑↑↑                          ↑↑↑   ↑↑↑

104,Bhupendra,Jogi,Sales,            (REMOVED)
85000,T104,4

                                     105,Eve,Adams,Sales,88000,4.1
                                          (ADDED)
```

---

## Statistics Comparison

### Salary Distribution

| Metric | Base | Current | Change |
|--------|------|---------|--------|
| Count | 4 | 4 | Same |
| Min | 75,000 | 82,000 | +7,000 |
| Max | 110,000 | 110,000 | Same |
| Mean | 90,000 | 92,500 | +2,500 |
| Total | 360,000 | 370,000 | +10,000 |

**Insight**: Overall payroll increased by ~2.8% (new hire + raise for 102).

### Department Distribution

| Department | Base | Current | Change |
|------------|------|---------|--------|
| Engineering | 2 | 2 | Same |
| Marketing | 1 | 1 | Same |
| Sales | 1 | 1 | Same (but different person) |

---

## How Alteris Processes This

### The Comparison Algorithm

```
Step 1: Outer Join on employee_id
────────────────────────────────────────────────────────────────────

BASE                          CURRENT                       JOINED
┌─────┬─────────┬────────┐   ┌─────┬─────────┬────────┐   ┌─────┬─────────┬─────────────────┐
│ 101 │ Binod   │ 90000  │   │ 101 │ Alice   │ 90000  │   │ 101 │ Binod   │ Alice   (MATCH) │
│ 102 │ Devendra│ 75000  │   │ 102 │ Bob     │ 82000  │   │ 102 │ Devendra│ Bob     (MATCH) │
│ 103 │ Amitabh │ 110000 │   │ 103 │ Charlie │ 110000 │   │ 103 │ Amitabh │ Charlie (MATCH) │
│ 104 │ Bhupendra│85000  │   │ 105 │ Eve     │ 88000  │   │ 104 │ Bhupendra│ NULL   (REMOVED)│
└─────┴─────────┴────────┘   └─────┴─────────┴────────┘   │ 105 │ NULL    │ Eve     (ADDED) │
                                                          └─────┴─────────┴─────────────────┘

Step 2: Classify Rows
────────────────────────────────────────────────────────────────────

REMOVED: Rows where current columns are NULL (id=104)
ADDED:   Rows where base columns are NULL (id=105)
MATCHED: Rows where both have values (ids=101,102,103)

Step 3: Find Modifications in Matched Rows
────────────────────────────────────────────────────────────────────

For each matched row, compare each column:
- id=101: first_name ≠, last_name ≠ → MODIFIED
- id=102: first_name ≠, last_name ≠, salary ≠ → MODIFIED
- id=103: first_name ≠, last_name ≠ → MODIFIED
```

---

## Interview Points

### Q: "How does Alteris handle the new column (performance_rating)?"

**Answer**:
> "Schema comparison detects the new column and reports it separately. For row-level comparison, we only compare columns that exist in BOTH datasets. The new column is shown in added/modified rows but isn't flagged as a 'change' since there's nothing to compare to."

### Q: "What if the new column has nulls?"

**Answer**:
> "Polars handles nulls correctly:
> - Null count is shown in column profiling
> - Nulls compare as equal to other nulls
> - `is_null()` predicates work correctly
> 
> The profiling tab would show 'Nulls: 0' for this column since all rows have values."

### Q: "How would you handle a dataset with millions of rows?"

**Answer**:
> "For large datasets:
> 1. Use Polars' lazy evaluation (`scan_csv` instead of `read_csv`)
> 2. Streaming aggregations
> 3. Sample data for visualizations
> 4. Add progress indicators
> 5. Consider chunked processing
> 
> The current implementation reads everything into memory, which is fine for files under ~1GB on most machines."

---

## Related Files

| File | Relationship | Purpose |
|------|--------------|---------|
| [small data 1.csv](small_data_1_csv.md) | Compare With | The "before" version |
| [app.py](../../app_py.md) | Processed By | Main application |
| [README.md](README.md) | Overview | Sample data documentation |

---

*This documentation provides complete understanding of the current dataset.*
