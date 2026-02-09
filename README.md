# Explainable Review Intelligence System

### *Transforming Customer Behavior Dimensions into Actionable Revenue Insights*

## Executive Summary

Businesses lose millions due to "silent churn"—customers who leave after a bad experience without filing a formal complaint. This project moves beyond simple "Star Rating" prediction to build an **Explainable Intelligence System**. By engineering **50+ features** from unstructured review data, we identify the exact "Revenue Killers" that drive customer dissatisfaction.

**Key Business Questions Addressed:**

* **The "Why" Factor:** Which specific service failure (wait time, staff behavior, price) is the strongest leading indicator of a customer never returning?
* **The High-Dimensional Edge:** How do 50+ diverse variables (from exclamation counts to holiday trends) interact to create a "High-Risk" profile?
* **Actionable Intelligence:** What specific operational changes will yield the highest increase in average customer lifetime value?

---

## Tech Stack & High-Leverage Tools

* **Data Architecture:** Python (Pandas, NumPy) for handling massive, high-dimensional datasets.
* **Intelligence Layer:** Scikit-learn (Random Forest, Logistic Regression) for predictive modeling.
* **Explainability (XAI):** SHAP / Feature Importance to translate "Black Box" models into business logic.
* **NLP Engineering:** TF-IDF and N-Gram extraction to turn raw text into 30+ binary features.
* **Analysis:** PCA (Principal Component Analysis) for 50D-to-2D cluster visualization.

---

## Data Architecture & Feature Engineering

To move from "Data" to "Intelligence," I engineered a wide feature set to capture the nuance of customer sentiment:

1. **Metadata Features (20+):** `review_length`, `is_weekend`, `is_holiday`, `subjectivity_score`, etc.
2. **NLP Dimension Features (30+):** Automated extraction of top 30 "Pain Point" phrases (e.g., *"manager rude"*, *"long wait"*) as distinct binary signals.
3. **Dimensionality Reduction:** Used **PCA** to visualize clusters of failure in high-dimensional space, ensuring the model identifies distinct "types" of bad experiences.

---

## Business Insights (Work in Progress)

> *This section is updated as the project reaches Phase 5-7.*

* **Insight 1:** [Pending - High correlation found between Feature X and Churn]
* **Insight 2:** [Pending - Clusters identified via PCA show X% of bad reviews are related to...]

---

## How to Run (Backend Focus)

This project is built with a **Backend-First** philosophy. No unnecessary frontend bloat—just raw, high-performance logic.

1. **Clone the Repo:**
```bash
git clone https://github.com/alinazir105/review-intelligence.git

```


2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run Initial Analysis:**
```bash
python src/data_pipeline.py

```



---

## Project Structure

```
├── data/
│   ├── raw/            # Original Yelp/Amazon Datasets
│   └── processed/      # Engineered 50+ Feature Matrix
├── notebooks/
│   ├── 01_eda.ipynb    # Finding the "Story" in the data
│   └── 02_modeling.ipynb # Predictive & Explainable AI
├── src/
│   ├── engineering.py  # Script for the 50+ feature pipeline
│   └── model_logic.py  # Backend AI logic
└── README.md

```
---
