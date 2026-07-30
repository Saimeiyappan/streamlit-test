import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EMI Predict AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# LOAD CUSTOM CSS
# --------------------------------------------------


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("🏦 EMI Predict AI")
st.subheader("Intelligent Financial Eligibility & Maximum EMI Prediction System")

st.markdown(
"""
AI Powered Loan Eligibility Prediction using **XGBoost**, **Scikit-Learn**, **MLflow** and **Streamlit**.
"""
)

st.divider()

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.header("📌 Project Overview")

st.write("""
Welcome to **EMI Predict AI**.

This application predicts:

- ✅ EMI Eligibility (Classification)
- ✅ Maximum Monthly EMI (Regression)

using Machine Learning models trained with XGBoost.

The goal of this project is to help financial institutions evaluate loan applicants and estimate an affordable EMI amount.
""")

st.divider()

# --------------------------------------------------
# PROJECT DASHBOARD
# --------------------------------------------------

st.header("📊 Project Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Classification", "XGBoost")

with col2:
    st.metric("Regression", "XGBoost")

with col3:
    st.metric("Accuracy", "95.33%")

with col4:
    st.metric("MLflow", "Enabled")

st.divider()

# --------------------------------------------------
# KEY FEATURES
# --------------------------------------------------

st.header("🚀 Key Features")

left, right = st.columns(2)

with left:

    st.success("EMI Eligibility Prediction")

    st.write("""
- Eligible
- Not Eligible
- High Risk
""")

    st.success("Maximum EMI Prediction")

    st.write("""
Predicts the maximum affordable monthly EMI using an optimized XGBoost Regression model.
""")

with right:

    st.success("Experiment Tracking")

    st.write("""
- MLflow Parameter Logging
- MLflow Metric Logging
- MLflow Model Logging
- Experiment Tracking
""")

    st.success("Deployment")

    st.write("""
- Streamlit
- GitHub
- Streamlit Cloud
""")

st.divider()

# --------------------------------------------------
# MACHINE LEARNING WORKFLOW
# --------------------------------------------------

st.header("⚙️ Machine Learning Workflow")

workflow = [
    "Data Collection",
    "Data Cleaning",
    "Exploratory Data Analysis (EDA)",
    "Feature Engineering",
    "Model Training",
    "Hyperparameter Tuning",
    "MLflow Experiment Tracking",
    "Model Serialization",
    "Streamlit Deployment",
    "Cloud Deployment"
]

for step in workflow:
    st.write(f"✅ {step}")

st.divider()

# --------------------------------------------------
# TECHNOLOGY STACK
# --------------------------------------------------

st.header("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("""
### Programming

- Python
- Pandas
- NumPy
""")

with tech2:
    st.info("""
### Machine Learning

- Scikit-Learn
- XGBoost
- MLflow
""")

with tech3:
    st.info("""
### Deployment

- Streamlit
- GitHub
- Streamlit Cloud
""")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("## 🏦 EMI Predict AI")

st.sidebar.markdown("---")

st.sidebar.write("👨‍💻 **Developer**")
st.sidebar.write("Sai Meiyappan")

st.sidebar.markdown("---")

st.sidebar.caption("Version 1.0")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Developed by Sai Meiyappan | EMI Predict AI | Machine Learning Project"
)

