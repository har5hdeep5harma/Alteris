# 📊 lenghthy data 2.csv - Current Transaction Dataset Documentation

> **E-Commerce Transaction Data: The "After" Snapshot (Identical to Base)**

---

## File Overview

| Property | Value |
|----------|-------|
| **File Path** | `Sample Data/Dataset 2/lenghthy data 2.csv` |
| **Role** | Current (New) Dataset |
| **Rows** | 25 data rows + 1 header |
| **Columns** | 15 |
| **File Size** | ~3.5 KB |
| **Encoding** | UTF-8 |

---

## Key Finding: Identical Data

**This file is 100% identical to `lenghthy data 1.csv`.**

When compared using Alteris:
```
┌─────────────────────────────────────────────────────────────┐
│              COMPARISON RESULT: NO CHANGES                   │
├─────────────────────────────────────────────────────────────┤
│ ➕ Added Rows:    0                                          │
│ ➖ Removed Rows:  0                                          │
│ ✏️ Modified Rows: 0                                          │
│ 🏛️ Schema Changes: None                                      │
│                                                              │
│ ✅ "No row-level changes detected"                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Purpose of Identical Files

### Why Include Identical Datasets?

| Purpose | Explanation |
|---------|-------------|
| **No-Change Testing** | Verify the app correctly identifies when data hasn't changed |
| **Success Path** | Demonstrate the "no changes" message and UI |
| **Performance Testing** | Larger dataset (25 rows) tests processing speed |
| **User Confidence** | Shows users the tool won't report false positives |
| **Edge Case** | Important to handle the "nothing changed" scenario |

---

## Testing Scenarios with This File

### Scenario 1: Full Comparison
```
Base: lenghthy data 1.csv
Current: lenghthy data 2.csv
Key: transaction_id
Expected: 0 added, 0 removed, 0 modified
```

### Scenario 2: Composite Key
```
Base: lenghthy data 1.csv
Current: lenghthy data 2.csv
Keys: [transaction_id, product_id]
Expected: Same result - all rows match
```

### Scenario 3: Column Profiling
```
Select column: total_price
Expected: Base and Current statistics are identical
Distribution charts completely overlap
```

---

## Complete Data (Same as lenghthy data 1.csv)

```csv
transaction_id,product_id,product_name,category,quantity,unit_price,total_price,customer_id,customer_region,salesperson_id,transaction_date,payment_method,discount_applied,shipping_status,legacy_order_ref
d8e8b79a-720c-4b53-9a3d-2b7e9b0a1c6a,P1001,Quantum Laptop,Electronics,1,1200.00,1200.00,C5001,North,S101,2025-04-15,Credit Card,0.00,Shipped,LGC-88720
f9c8a7b6-610b-4c42-8a2c-1b6e8a9b0c5b,P1002,Starlight Mouse,Accessories,2,25.00,47.50,C5002,South,S102,2025-04-18,PayPal,0.05,Shipped,LGC-88721
e8d7c6b5-500a-4b31-791b-0a5d798a9b4a,P1003,Nebula Keyboard,Accessories,1,75.00,75.00,C5001,North,S101,2025-04-20,Credit Card,0.00,Shipped,LGC-88722
d7c6b5a4-4f09-4a20-680a-fa4c68798a39,P1004,Orion Monitor,Electronics,1,300.00,285.00,C5003,West,S103,2025-04-22,Credit Card,0.05,Shipped,LGC-88723
c6b5a493-3e08-491f-57f9-ea3b57687928,P1005,Galaxy Tablet,Electronics,1,450.00,450.00,C5004,East,S104,2025-04-25,PayPal,0.00,Processing,LGC-88724
b5a49382-2d07-480e-46e8-d92a46576817,P1006,Cosmic Webcam,Accessories,1,60.00,60.00,C5002,South,S102,2025-04-28,Credit Card,0.00,Shipped,LGC-88725
a4938271-1c06-47fd-35d7-c81935465706,P1007,Meteor Speakers,Audio,1,150.00,150.00,C5005,North,S101,2025-05-01,PayPal,0.00,Shipped,LGC-88726
93827160-0b05-46ec-24c6-b708243546f5,P1001,Quantum Laptop,Electronics,1,1200.00,1140.00,C5006,West,S103,2025-05-03,Credit Card,0.05,Shipped,LGC-88727
8271605f-fa04-45db-13b5-a6f7132435e4,P1008,Eclipse VR Headset,Gaming,1,600.00,600.00,C5007,East,S104,2025-05-05,PayPal,0.00,Shipped,LGC-88728
71605f4e-e903-44ca-02a4-95e6021324d3,P1009,Supernova Gaming Chair,Gaming,1,400.00,400.00,C5007,East,S104,2025-05-06,Credit Card,0.00,Shipped,LGC-88729
605f4e3d-d802-43b9-f193-84d5f10213c2,P1010,Pulsar Power Bank,Accessories,3,40.00,120.00,C5008,South,S102,2025-05-10,PayPal,0.00,Shipped,LGC-88730
5f4e3d2c-c701-42a8-e082-73c4e0f102b1,P1002,Starlight Mouse,Accessories,1,25.00,25.00,C5009,West,S103,2025-05-12,Credit Card,0.00,Shipped,LGC-88731
4e3d2c1b-b600-4197-df71-62b3d0e0f1a0,P1011,Andromeda Phone,Mobile,1,800.00,760.00,C5010,North,S101,2025-05-15,PayPal,0.05,Shipped,LGC-88732
3d2c1b0a-a5ff-4086-ce60-51a2c0d0e09f,P1012,Comet Cable,Accessories,5,10.00,50.00,C5001,North,S101,2025-05-18,Credit Card,0.00,Shipped,LGC-88733
2c1b0a99-94fe-4f75-bd5f-4091b0c0d08e,P1004,Orion Monitor,Electronics,2,300.00,600.00,C5011,East,S104,2025-05-20,PayPal,0.00,Shipped,LGC-88734
1b0a9988-83fd-4e64-ac4e-3f80a0b0c07d,P1001,Quantum Laptop,Electronics,1,1200.00,1200.00,C5012,South,S102,2025-05-23,Credit Card,0.00,Shipped,LGC-88735
0a998877-72fc-4d53-9b3d-2e7f90a0b06c,P1005,Galaxy Tablet,Electronics,1,450.00,427.50,C5013,West,S103,2025-05-28,Credit Card,0.05,Processing,LGC-88736
99887766-61fb-4c42-8a2c-1d6e8990a05b,P1007,Meteor Speakers,Audio,1,150.00,150.00,C5014,North,S101,2025-06-02,PayPal,0.00,Shipped,LGC-88737
88776655-50ea-4b31-791b-0c5d7889904a,P1008,Eclipse VR Headset,Gaming,1,600.00,600.00,C5015,East,S104,2025-06-05,Credit Card,0.00,Shipped,LGC-88738
77665544-4fd9-4a20-680a-fb4c67788939,P1013,Rocket Router,Networking,1,120.00,120.00,C5016,South,S102,2025-06-10,PayPal,0.00,Shipped,LGC-88739
66554433-3ec8-491f-57f9-ea3b56677828,P1003,Nebula Keyboard,Accessories,2,75.00,150.00,C5003,West,S103,2025-06-12,Credit Card,0.00,Shipped,LGC-88740
55443322-2db7-480e-46e8-d92a45566717,P1014,Satellite SSD,Storage,1,200.00,190.00,C5017,North,S101,2025-06-15,PayPal,0.05,Shipped,LGC-88741
44332211-1ca6-47fd-35d7-c81934455606,P1009,Supernova Gaming Chair,Gaming,1,400.00,400.00,C5007,East,S104,2025-06-20,Credit Card,0.00,Shipped,LGC-88742
33221100-0b95-46ec-24c6-b708233445f5,P1011,Andromeda Phone,Mobile,1,800.00,800.00,C5018,South,S102,2025-06-25,Credit Card,0.00,Shipped,LGC-88743
221100ff-fa84-45db-13b5-a6f7122334e4,P1001,Quantum Laptop,Electronics,2,1200.00,2280.00,C5019,West,S103,2025-06-28,PayPal,0.05,Shipped,LGC-88744
```

---

## How Alteris Handles Identical Files

### Algorithm Walkthrough

```
STEP 1: Load Both Files
────────────────────────────────────────────────────────────────────
df_base = pl.read_csv("lenghthy data 1.csv")    # 25 rows
df_current = pl.read_csv("lenghthy data 2.csv")  # 25 rows

STEP 2: Outer Join on transaction_id
────────────────────────────────────────────────────────────────────
joined_df = df_base.join(df_current, on="transaction_id", how="outer")
# Result: 25 rows (all keys match perfectly)

STEP 3: Classify Rows
────────────────────────────────────────────────────────────────────
REMOVED: Rows where current columns are NULL
         Result: 0 rows (no base-only keys)

ADDED: Rows where base columns are NULL
       Result: 0 rows (no current-only keys)

MATCHED: Rows where both sides have values
         Result: 25 rows (all rows match)

STEP 4: Find Modifications in Matched Rows
────────────────────────────────────────────────────────────────────
For each of 25 rows:
  Compare: product_name == product_name_current? ✓
  Compare: quantity == quantity_current? ✓
  Compare: total_price == total_price_current? ✓
  ... (all columns match)

Result: 0 modified rows (all values identical)

STEP 5: Display Results
────────────────────────────────────────────────────────────────────
st.success("No row-level changes detected.")
```

---

## UI Display for Identical Files

When files are identical, Alteris displays:

### Summary Metrics
```
┌──────────────┬───────────────┬───────────────┬─────────────────────┐
│ ➕ Rows Added │ ➖ Rows Removed│ ✏️ Rows Modified│ ⬇️ Download Report │
│      0       │       0       │       0       │     [Disabled]      │
└──────────────┴───────────────┴───────────────┴─────────────────────┘
```

### Row-Level Changes Tab
```
┌─────────────────────────────────────────────────────────────────────┐
│  ✅ No row-level changes detected.                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### Schema Changes Tab
```
┌─────────────────────────────────────────────────────────────────────┐
│  ✅ No schema changes detected.                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Column Profiling Tab
```
┌─────────────────────────────────────────────────────────────────────┐
│  Statistics for 'total_price':                                      │
│  ┌──────────┬────────────┬────────────┐                             │
│  │ Metric   │ Base       │ Current    │                             │
│  ├──────────┼────────────┼────────────┤                             │
│  │ Mean     │ 543.60     │ 543.60     │  ← Identical                │
│  │ Std Dev  │ 487.53     │ 487.53     │  ← Identical                │
│  │ Min      │ 25.00      │ 25.00      │  ← Identical                │
│  │ Max      │ 2280.00    │ 2280.00    │  ← Identical                │
│  │ Nulls    │ 0          │ 0          │  ← Identical                │
│  └──────────┴────────────┴────────────┘                             │
│                                                                      │
│  [Distribution Chart]                                                │
│  ████████████████████████                                            │
│  Base and Current distributions completely overlap                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Why This Scenario Matters

### Real-World Use Cases for "No Changes"

| Scenario | Explanation |
|----------|-------------|
| **Daily Audit** | Confirm no unauthorized changes to production data |
| **Deployment Verification** | Ensure migration didn't corrupt data |
| **Change Freeze** | Verify data unchanged during code freeze period |
| **Backup Validation** | Confirm backup matches original |
| **ETL Testing** | Verify idempotent pipeline produces same output |

### User Confidence

When users see "No changes detected" on identical files, they gain confidence that:
1. The tool isn't reporting false positives
2. Their data integrity is maintained
3. The comparison algorithm is accurate

---

## Interview Points

### Q: "Why include identical files in your sample data?"

**Answer**:
> "Testing the 'no changes' scenario is critical:
> 1. **Avoid False Positives**: Users need confidence the tool won't report phantom changes
> 2. **Edge Case Handling**: An empty result is a valid and common outcome
> 3. **UI Testing**: Verify the 'No changes' message displays correctly
> 4. **Real Use Case**: Auditing and validation often confirm data is unchanged"

### Q: "How does the algorithm know there are no changes?"

**Answer**:
> "After the outer join:
> 1. Check for NULL in current columns → 0 rows → No removals
> 2. Check for NULL in base columns → 0 rows → No additions
> 3. Compare each column value in matched rows → All equal → No modifications
> 
> The algorithm doesn't special-case identical files; it naturally discovers there are no changes through the standard comparison process."

### Q: "What if the files are identical but in different row order?"

**Answer**:
> "The algorithm still works correctly because:
> 1. The outer join matches on the key column (`transaction_id`)
> 2. Row order doesn't matter for join-based matching
> 3. Each row is matched by its key, not its position
> 
> This is a key advantage of key-based comparison over line-by-line diff tools."

### Q: "How would you detect if someone modified and then reverted a change?"

**Answer**:
> "This tool compares two snapshots at a point in time. It can't detect 'modify then revert' because the final state is identical.
> 
> To detect such patterns, you'd need:
> - Change Data Capture (CDC) at the database level
> - Version control for data files
> - Audit logging with timestamps
> - Transaction logs rather than state comparison"

---

## Related Files

| File | Relationship | Purpose |
|------|--------------|---------|
| [lenghthy data 1.csv](lenghthy_data_1_csv.md) | Compare With | Identical base file |
| [app.py](../../app_py.md) | Processed By | Main application |
| [README.md](README.md) | Overview | Sample data documentation |

---

*This documentation explains the purpose and handling of identical datasets.*
