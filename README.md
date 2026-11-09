# Vendor Performance Analysis

## 1. Project Overview

This project focuses on analyzing vendor performance, purchasing activities, inventory management, procurement costs, and supplier efficiency.

The objective is to identify opportunities to optimize procurement spending, improve supplier selection, manage inventory efficiently, and reduce supply-chain risks using data analytics.

## 2. Business Problem

The company needs to understand:

- Which vendors contribute the most to purchase spending?
- Which product classifications consume the highest budget?
- Which vendors have longer delivery durations?
- How efficiently is inventory being managed?
- Which products have high closing inventory but low purchase activity?
- How can procurement and freight costs be optimized?

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL / SQLite
- SQLAlchemy
- Power BI
- Jupyter Notebook
- Git and GitHub

## 4. Dataset Description

The project uses five datasets:

| Dataset | Description |
|---|---|
| Beginning Inventory | Opening inventory information |
| Ending Inventory | Closing inventory information |
| Purchase Prices | Product pricing and vendor information |
| Purchases | Purchase transactions and quantities |
| Vendor Invoice | Invoice amounts and freight costs |

## 5. Project Workflow

1. Data Loading
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Statistical Analysis
6. Outlier Detection
7. SQL Business Analysis
8. Power BI Dashboard Development
9. Business Insights
10. Recommendations

## 6. Analysis Performed

### Vendor Analysis
- Unique vendor count
- Vendor-wise purchase spending
- Average delivery duration
- Supplier performance comparison

### Purchase Analysis
- Average purchase price
- Purchase spending by classification
- Monthly purchasing trends

### Product Analysis
- Estimated gross margin percentage
- Supplier price differences
- Product purchase activity

### Inventory Analysis
- Opening vs closing inventory
- Inventory changes for matching inventory IDs
- Products with high closing inventory
- Products with zero closing stock
- Store-wise inventory analysis

### Freight Analysis
- Freight cost distribution
- Vendor-wise freight analysis
- Freight percentage analysis

## 7. Key Findings

- Total opening inventory: 4,219,275 units.
- Total closing inventory: 4,885,776 units.
- Overall inventory increased by 666,501 units (approximately 15.79%).
- No exact duplicate records were identified in the five datasets.
- Freight and purchase amounts contain potential statistical outliers that require business investigation.

## 8. Business Recommendations

- Optimize vendor selection based on cost and delivery performance.
- Investigate products with unusually high closing inventory.
- Improve procurement planning.
- Monitor supplier freight costs.
- Reduce dependency on highly concentrated suppliers.
- Negotiate competitive purchasing prices.
- Monitor supplier performance through KPIs.

## 9. Dashboard

Power BI dashboards will provide an interactive view of:

- Vendor Performance Overview
- Supplier Performance and Procurement Analysis
- Inventory and Product Analysis

## 10. Conclusion

This project demonstrates how Python, SQL, and Power BI can be used to analyze procurement and vendor performance data.

The analysis supports better purchasing decisions, improved inventory monitoring, cost optimization, and supplier performance management.
