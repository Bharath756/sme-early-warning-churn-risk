# Early Warning Churn Risk System (SME Customers)

## 1. Business Problem
Customer churn often becomes visible only after it is too late to intervene.
Traditional churn analysis explains *why* customers left, but does not identify *who is at risk now*.

This project builds an **early warning churn risk system** that proactively flags customers likely to churn in the near future, enabling targeted retention actions.

## 2. Dataset Overview
Snapshot-based SME customer dataset with anonymized customer, usage, pricing, and churn indicators.

## 3. Approach & Methodology
### Early Warning Definition
- Churn risk defined as near-term likelihood  
- Focus on risk ranking, not binary prediction  
- Explicit assumptions and scope  

### Time-Based Feature Engineering
- Tenure and lifecycle indicators  
- Contract flexibility signals  
- Pricing pressure metrics  
- Service engagement depth  

Strict leakage controls exclude:
- Churn label  
- Cumulative future variables  
- CLV and segmentation outputs  

### Leakage-Safe Modeling
- Stratified train/test split  
- Train-only scaling  
- Interpretable Logistic Regression baseline  

## 4. Notebook Walkthrough
- `notebooks/01_early_warning_definition.ipynb` — Problem framing and assumptions  
- `notebooks/02_time_based_feature_engineering.ipynb` — Leakage-safe feature construction  
- `notebooks/03_churn_risk_modeling.ipynb` — Model training and risk scoring  

## 5. Key Outputs & Business Interpretation
- Customer-level churn risk score (0–1)  
- Early warning risk tiers (Low / Medium / High)  

| Risk Tier | Description | Recommended Action |
|----------|------------|-------------------|
| High | Imminent churn likelihood | Immediate outreach |
| Medium | Elevated churn signals | Targeted offers |
| Low | Stable customers | No action |

## 6. Tech Stack
Python, Pandas, NumPy, Scikit-learn, Jupyter Notebook, Matplotlib, Seaborn

## 7. Limitations & Next Improvements
- Snapshot-based data limits temporal precision  
- Risk scores reflect likelihood, not certainty  
- Future enhancements:
  - Time-series data  
  - Survival analysis  
  - Cost-sensitive optimization  

## Final Note
This project emphasizes deployable analytics, strong data governance, and business-first decision support.
