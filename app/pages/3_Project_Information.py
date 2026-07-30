import streamlit as st

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Project Information",
    page_icon="📖",
    layout="wide"
)

# ----------------------------------------------------
# PAGE TITLE
# ----------------------------------------------------

st.title("📖 Project Information")

st.write("""
This page provides an overview of the EMI Predict AI project,
including its objectives, dataset, workflow, technologies,
and deployment process.
""")

st.markdown("---")

# ----------------------------------------------------
# PROJECT OBJECTIVE
# ----------------------------------------------------

st.subheader("🎯 Project Objective")

st.info("""
The objective of this project is to develop an intelligent
machine learning application capable of:

• Predicting a customer's EMI Eligibility (Classification)

• Estimating the Maximum Affordable Monthly EMI (Regression)

The application assists financial institutions in making
faster and more reliable loan approval decisions.
""")

# ----------------------------------------------------
# DATASET
# ----------------------------------------------------

st.subheader("📂 Dataset Information")

col1, col2 = st.columns(2)

with col1:

    st.success("Dataset Overview")

    st.write("""
- Records : 404,800

- Features : 35

- Classification Target :
  EMI Eligibility

- Regression Target :
  Maximum Monthly EMI
""")

with col2:

    st.success("Input Features")

    st.write("""
- Customer Demographics

- Employment Details

- Financial Information

- Credit Score

- Existing Loans

- EMI Scenario

- Requested Loan Details
""")

st.markdown("---")

# ----------------------------------------------------
# ML WORKFLOW
# ----------------------------------------------------

st.subheader("⚙️ Machine Learning Workflow")

st.write("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis (EDA)

4. Feature Engineering

5. Data Preprocessing

6. Model Training

7. Hyperparameter Tuning

8. MLflow Experiment Tracking

9. Model Selection

10. Streamlit Deployment
""")

st.markdown("---")

# ----------------------------------------------------
# TECHNOLOGIES
# ----------------------------------------------------

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.success("Programming")

    st.write("""
- Python

- Pandas

- NumPy
""")

with tech2:

    st.success("Machine Learning")

    st.write("""
- Scikit-Learn

- XGBoost

- MLflow
""")

with tech3:

    st.success("Deployment")

    st.write("""
- Streamlit

- GitHub

- Joblib
""")

st.markdown("---")

# ----------------------------------------------------
# MLFLOW
# ----------------------------------------------------

st.subheader("🧪 MLflow Integration")

st.info("""
MLflow was used to:

✔ Track Experiments

✔ Log Parameters

✔ Log Metrics

✔ Compare Multiple Models

✔ Store Best Performing Models
""")

st.markdown("---")

# ----------------------------------------------------
# PROJECT OUTCOME
# ----------------------------------------------------

st.subheader("🚀 Project Outcome")

st.success("""
The XGBoost Classification model achieved an accuracy of
95.04%, while the XGBoost Regression model achieved an
R² Score of 0.9768.

These models were selected as the final deployed models
for the EMI Predict AI application.
""")