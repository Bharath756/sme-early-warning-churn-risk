# Early Warning Churn Risk System (SME Customers)

## Business Context
Customer churn often becomes visible only after it is too late to intervene.
Traditional churn analysis explains 'why' customers left, but does not help
identify 'who is at risk now'.

This project builds an "early warning churn risk system" that proactively
flags customers likely to churn in the near future, enabling targeted
retention actions before revenue is lost.

---

## Objective
Design a "leakage-safe, interpretable churn risk model" that:
- Identifies customers at elevated churn risk 'before' churn occurs
- Produces probability-based risk scores for prioritization
- Supports proactive retention decision-making

---

## Project Approach

### 1. Early Warning Definition
- Defined churn risk as a "near-term likelihood", not exact churn timing
- Explicitly documented assumptions and scope limitations
- Focused on *risk ranking* rather than binary prediction

### 2. Time-Based Feature Engineering
Engineered proxy early-warning signals using information available "prior to churn":
- Tenure and lifecycle indicators
- Contract flexibility (month-to-month risk)
- Pricing pressure (high monthly charges)
- Service engagement depth (service count)

Strict leakage controls were applied to exclude:
- Churn label
- TotalCharges (cumulative future signal)
- CLV and segmentation outputs from prior projects

### 3. Leakage-Safe Modeling Pipeline
- Stratified train/test split to preserve churn distribution
- Leakage-safe feature scaling (train-only fit)
- Interpretable Logistic Regression baseline model

### 4. Risk Scoring & Evaluation
- Generated churn risk probabilities for each customer
- Evaluated ranking performance using ROC-AUC
- Prioritized recall to minimize missed churners

---

## Key Outputs
- "Customer-level churn risk score (0–1)"
- "Early warning risk tiers" (Low / Medium / High)
- Feature-level interpretability for business understanding

---

## Business Interpretation

| Risk Tier | Description | Recommended Action |
|---------|------------|-------------------|
| High Risk | Imminent churn likelihood | Immediate retention outreach |
| Medium Risk | Elevated churn signals | Targeted offers & monitoring |
| Low Risk | Stable customers | No immediate action |

The model enables retention teams to "focus effort where it matters most",
balancing intervention cost against churn risk.

---

## Tools & Techniques
- Python, Pandas, NumPy
- Scikit-learn (Logistic Regression, preprocessing)
- Jupyter Notebook
- Matplotlib / Seaborn

---

## Limitations & Future Enhancements
- Snapshot-based data (no true event-level time series)
- Risk scores reflect likelihood, not certainty
- Future work could incorporate:
  - Time-series behavioral data
  - Survival analysis
  - Cost-sensitive threshold optimization

---

## Repository Structure
# Early Warning Churn Risk System (SME Customers)

## Business Context
Customer churn often becomes visible only after it is too late to intervene.
Traditional churn analysis explains *why* customers left, but does not help
identify *who is at risk now*.

This project builds an **early warning churn risk system** that proactively
flags customers likely to churn in the near future, enabling targeted
retention actions before revenue is lost.

---

## Objective
Design a **leakage-safe, interpretable churn risk model** that:
- Identifies customers at elevated churn risk *before* churn occurs
- Produces probability-based risk scores for prioritization
- Supports proactive retention decision-making

---

## Project Approach

### 1. Early Warning Definition
- Defined churn risk as a **near-term likelihood**, not exact churn timing
- Explicitly documented assumptions and scope limitations
- Focused on *risk ranking* rather than binary prediction

### 2. Time-Based Feature Engineering
Engineered proxy early-warning signals using information available **prior to churn**:
- Tenure and lifecycle indicators
- Contract flexibility (month-to-month risk)
- Pricing pressure (high monthly charges)
- Service engagement depth (service count)

Strict leakage controls were applied to exclude:
- Churn label
- TotalCharges (cumulative future signal)
- CLV and segmentation outputs from prior projects

### 3. Leakage-Safe Modeling Pipeline
- Stratified train/test split to preserve churn distribution
- Leakage-safe feature scaling (train-only fit)
- Interpretable Logistic Regression baseline model

### 4. Risk Scoring & Evaluation
- Generated churn risk probabilities for each customer
- Evaluated ranking performance using ROC-AUC
- Prioritized recall to minimize missed churners

---

## Key Outputs
- **Customer-level churn risk score (0–1)**
- **Early warning risk tiers** (Low / Medium / High)
- Feature-level interpretability for business understanding

---

## Business Interpretation

| Risk Tier | Description | Recommended Action |
|---------|------------|-------------------|
| High Risk | Imminent churn likelihood | Immediate retention outreach |
| Medium Risk | Elevated churn signals | Targeted offers & monitoring |
| Low Risk | Stable customers | No immediate action |

The model enables retention teams to **focus effort where it matters most**,
balancing intervention cost against churn risk.

---

## Tools & Techniques
- Python, Pandas, NumPy
- Scikit-learn (Logistic Regression, preprocessing)
- Jupyter Notebook
- Matplotlib / Seaborn

---

## Limitations & Future Enhancements
- Snapshot-based data (no true event-level time series)
- Risk scores reflect likelihood, not certainty
- Future work could incorporate:
  - Time-series behavioral data
  - Survival analysis
  - Cost-sensitive threshold optimization

---

## Repository Structure
sme-early-warning-churn-risk/
│
├── data/
│ └── raw/
│ └── telco_customer_churn.csv
│
├── notebooks/
│ ├── 01_early_warning_definition.ipynb
│ ├── 02_time_based_feature_engineering.ipynb
│ └── 03_churn_risk_modeling.ipynb
│
├── README.md
└── LICENSE


---

## Final Note
This project emphasizes "deployable analytics", strong "data governance",
and "business-first decision support", reflecting real-world customer
analytics practices.
