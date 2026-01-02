# 📊 lenghthy data 1.csv - Base Transaction Dataset Documentation

> **E-Commerce Transaction Data: The "Before" Snapshot**

---

## File Overview

| Property | Value |
|----------|-------|
| **File Path** | `Sample Data/Dataset 2/lenghthy data 1.csv` |
| **Role** | Base (Old) Dataset |
| **Rows** | 25 data rows + 1 header |
| **Columns** | 15 |
| **File Size** | ~3.5 KB |
| **Encoding** | UTF-8 |

---

## Complete Schema Definition

| # | Column | Data Type | Nullable | Description |
|---|--------|-----------|----------|-------------|
| 1 | `transaction_id` | UUID | No | **Primary Key** - Unique transaction identifier |
| 2 | `product_id` | String | No | Product code (e.g., P1001) |
| 3 | `product_name` | String | No | Product display name |
| 4 | `category` | String | No | Product category |
| 5 | `quantity` | Integer | No | Units purchased |
| 6 | `unit_price` | Float | No | Price per unit (USD) |
| 7 | `total_price` | Float | No | Line total after discount |
| 8 | `customer_id` | String | No | Customer code (e.g., C5001) |
| 9 | `customer_region` | String | No | Geographic region |
| 10 | `salesperson_id` | String | No | Sales rep code (e.g., S101) |
| 11 | `transaction_date` | Date | No | Sale date (YYYY-MM-DD) |
| 12 | `payment_method` | String | No | Payment type |
| 13 | `discount_applied` | Float | No | Discount rate (0.00-0.05) |
| 14 | `shipping_status` | String | No | Delivery status |
| 15 | `legacy_order_ref` | String | No | Old system reference |

---

## Complete Data

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

## Column Deep Dive

### Column 1: transaction_id (UUID)

```
Type: UUID v4 (Random)
Format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Example: d8e8b79a-720c-4b53-9a3d-2b7e9b0a1c6a
```

**What is UUID?**
UUID (Universally Unique Identifier) is a 128-bit number used to identify information in computer systems.

**Why UUID for Transaction IDs?**:

| Benefit | Explanation |
|---------|-------------|
| **Globally Unique** | No collisions even across distributed systems |
| **Unpredictable** | Can't guess other transaction IDs |
| **Decentralized** | Can be generated without a central authority |
| **Merge-Safe** | No conflicts when combining data from different sources |

**UUID v4 Structure**:
```
d8e8b79a-720c-4b53-9a3d-2b7e9b0a1c6a
│        │    │    │    │
│        │    │    │    └── Random (48 bits)
│        │    │    └─────── Random (12 bits) + variant
│        │    └──────────── Random (4 bits) + version (4)
│        └───────────────── Random (16 bits)
└────────────────────────── Random (32 bits)
```

**Interview Point**:
> "I chose UUID over auto-increment because:
> 1. Works in distributed systems without coordination
> 2. Can be generated on the client before sending to server
> 3. Prevents enumeration attacks (can't guess order IDs)
> 4. Easier data migration and merging"

---

### Column 2: product_id

```
Type: String
Format: P + 4-digit number
Values: P1001 through P1014
```

**Product Catalog** (14 unique products):

| product_id | product_name | category | unit_price |
|------------|--------------|----------|------------|
| P1001 | Quantum Laptop | Electronics | $1,200 |
| P1002 | Starlight Mouse | Accessories | $25 |
| P1003 | Nebula Keyboard | Accessories | $75 |
| P1004 | Orion Monitor | Electronics | $300 |
| P1005 | Galaxy Tablet | Electronics | $450 |
| P1006 | Cosmic Webcam | Accessories | $60 |
| P1007 | Meteor Speakers | Audio | $150 |
| P1008 | Eclipse VR Headset | Gaming | $600 |
| P1009 | Supernova Gaming Chair | Gaming | $400 |
| P1010 | Pulsar Power Bank | Accessories | $40 |
| P1011 | Andromeda Phone | Mobile | $800 |
| P1012 | Comet Cable | Accessories | $10 |
| P1013 | Rocket Router | Networking | $120 |
| P1014 | Satellite SSD | Storage | $200 |

---

### Column 3: product_name

```
Type: String
Pattern: Space-themed names
```

**Naming Theme**: All products follow a space/astronomy theme:
- Quantum, Starlight, Nebula, Orion, Galaxy
- Cosmic, Meteor, Eclipse, Supernova, Pulsar
- Andromeda, Comet, Rocket, Satellite

**Interview Point - Denormalization**:
> "Product name is stored directly with the transaction (denormalized) rather than just storing product_id and joining. This trades storage space for query performance and preserves the product name at time of purchase."

---

### Column 4: category

```
Type: String (Categorical)
Unique Values: 7
Distribution:
  - Electronics: 8 (32%)
  - Accessories: 7 (28%)
  - Gaming: 4 (16%)
  - Audio: 2 (8%)
  - Mobile: 2 (8%)
  - Networking: 1 (4%)
  - Storage: 1 (4%)
```

---

### Column 5: quantity

```
Type: Integer
Range: 1 to 5
Distribution:
  - 1 item: 21 transactions (84%)
  - 2 items: 3 transactions (12%)
  - 3 items: 0 transactions
  - 5 items: 1 transaction (4%)
```

---

### Column 6: unit_price

```
Type: Float
Range: $10.00 to $1,200.00
Currency: USD (assumed)
```

**Price Tiers**:
| Tier | Range | Products |
|------|-------|----------|
| Budget | $10-$50 | Cables, Mouse, Power Bank |
| Mid | $51-$200 | Keyboard, Webcam, Speakers, Router, SSD |
| Premium | $201-$500 | Monitor, Tablet, Gaming Chair |
| High-End | $501+ | Laptop, VR Headset, Phone |

---

### Column 7: total_price

```
Type: Float
Formula: quantity * unit_price * (1 - discount_applied)
Range: $25.00 to $2,280.00
```

**Examples**:
```
Transaction 1: 1 × $1,200 × (1 - 0.00) = $1,200.00
Transaction 2: 2 × $25 × (1 - 0.05) = $47.50
Transaction 25: 2 × $1,200 × (1 - 0.05) = $2,280.00
```

---

### Column 8: customer_id

```
Type: String
Format: C + 4-digit number
Unique Customers: 19
```

**Customer Distribution**:
- C5001: 3 transactions (repeat customer)
- C5007: 3 transactions (repeat customer)
- Others: 1-2 transactions each

---

### Column 9: customer_region

```
Type: String (Categorical)
Values: [North, South, East, West]
Distribution:
  - North: 7 (28%)
  - South: 6 (24%)
  - East: 5 (20%)
  - West: 7 (28%)
```

---

### Column 10: salesperson_id

```
Type: String
Format: S + 3-digit number
Values: S101, S102, S103, S104
```

**Sales Rep Performance**:
| Rep | Transactions | Total Revenue | Top Region |
|-----|--------------|---------------|------------|
| S101 | 7 | $4,630 | North |
| S102 | 6 | $1,902.50 | South |
| S103 | 7 | $4,457.50 | West |
| S104 | 5 | $2,600 | East |

---

### Column 11: transaction_date

```
Type: Date
Format: YYYY-MM-DD
Range: 2025-04-15 to 2025-06-28
Span: 74 days (~2.5 months)
```

**Monthly Distribution**:
| Month | Transactions | Revenue |
|-------|--------------|---------|
| April 2025 | 6 | $2,117.50 |
| May 2025 | 10 | $4,572.50 |
| June 2025 | 9 | $6,900 |

---

### Column 12: payment_method

```
Type: String (Categorical)
Values: [Credit Card, PayPal]
Distribution:
  - Credit Card: 14 (56%)
  - PayPal: 11 (44%)
```

---

### Column 13: discount_applied

```
Type: Float
Values: 0.00 or 0.05
Distribution:
  - No discount (0.00): 18 (72%)
  - 5% discount (0.05): 7 (28%)
```

---

### Column 14: shipping_status

```
Type: String (Categorical)
Values: [Shipped, Processing]
Distribution:
  - Shipped: 23 (92%)
  - Processing: 2 (8%)
```

---

### Column 15: legacy_order_ref

```
Type: String
Format: LGC- + 5-digit number
Range: LGC-88720 to LGC-88744
```

**Purpose**: Reference to old order system (migration scenario).

**Interview Point**:
> "The legacy_order_ref column represents a common real-world scenario: system migration. When companies migrate from old systems, they keep references to the original records for:
> - Audit trails
> - Customer support (looking up old orders)
> - Data reconciliation during transition"

---

## Key Statistics

### Financial Summary

| Metric | Value |
|--------|-------|
| Total Revenue | $13,590.00 |
| Average Transaction | $543.60 |
| Highest Transaction | $2,280.00 |
| Lowest Transaction | $25.00 |
| Total Items Sold | 29 |

### Top Products by Revenue

| Product | Units | Revenue | % of Total |
|---------|-------|---------|------------|
| Quantum Laptop | 5 | $5,820 | 42.8% |
| Eclipse VR Headset | 2 | $1,200 | 8.8% |
| Andromeda Phone | 2 | $1,560 | 11.5% |
| Supernova Gaming Chair | 2 | $800 | 5.9% |
| Orion Monitor | 3 | $885 | 6.5% |

---

## Comparison with lenghthy data 2.csv

**Key Finding**: The files are **identical**.

When compared using Alteris with `transaction_id` as the key:
- ➕ Added Rows: 0
- ➖ Removed Rows: 0
- ✏️ Modified Rows: 0

**Purpose**: This demonstrates:
1. How the app behaves when no changes exist
2. Performance testing with larger dataset
3. "Success" message for identical files

---

## Interview Deep Dives

### Q: "Why is product_name stored with each transaction?"

**Answer**:
> "This is **denormalization** - intentionally adding redundancy for performance:
> 
> **Normalized Design** (3NF):
> ```
> transactions: transaction_id, product_id, ...
> products: product_id, product_name, category, price
> ```
> - Pros: No redundancy, easy updates
> - Cons: Requires JOIN for every query
>
> **Denormalized Design** (used here):
> ```
> transactions: transaction_id, product_id, product_name, ...
> ```
> - Pros: Faster reads, no joins needed
> - Cons: More storage, update anomalies possible
>
> For a transaction log, denormalization makes sense because:
> 1. Transactions are append-only (rarely updated)
> 2. Product name at time of sale should be preserved
> 3. Reporting queries are faster without joins"

### Q: "How would you optimize this for millions of rows?"

**Answer**:
> "Several strategies:
> 1. **Partitioning**: Split by transaction_date (monthly/yearly)
> 2. **Columnar Storage**: Use Parquet format for analytics
> 3. **Indexing**: Index on transaction_id, customer_id, transaction_date
> 4. **Lazy Loading**: Use Polars' `scan_csv()` for streaming
> 5. **Sampling**: For visualizations, sample large datasets"

### Q: "What's the formula for total_price?"

**Answer**:
> "`total_price = quantity × unit_price × (1 - discount_applied)`
> 
> For example, 2 laptops at $1,200 with 5% discount:
> `2 × 1200 × (1 - 0.05) = 2 × 1200 × 0.95 = $2,280`"

---

## Related Files

| File | Relationship | Purpose |
|------|--------------|---------|
| [lenghthy data 2.csv](lenghthy_data_2_csv.md) | Compare With | Identical file for testing |
| [app.py](../../app_py.md) | Processed By | Main application |
| [README.md](README.md) | Overview | Sample data documentation |

---

*This documentation provides complete understanding of the transaction dataset.*
