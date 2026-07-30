import streamlit as st

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
    layout="wide"
)

# ----------------------------------------------------
# PAGE TITLE
# ----------------------------------------------------

st.title("👨‍💻 About the Developer")

st.write("""
This page provides information about the developer,
the project, and the technologies used.
""")

st.markdown("---")

# ----------------------------------------------------
# DEVELOPER PROFILE
# ----------------------------------------------------

st.subheader("👤 Developer")

col1, col2 = st.columns([1,2])

with col1:

    st.info("""
**Name**

Sai Meiyappan
""")

with col2:

    st.write("""
Aspiring **AI & Machine Learning Engineer**
with a strong interest in Machine Learning,
Data Science, and MLOps.

This project was developed as part of an
end-to-end Machine Learning portfolio to
demonstrate model development, experiment
tracking, and deployment using Streamlit.
""")

st.markdown("---")

# ----------------------------------------------------
# SKILLS
# ----------------------------------------------------

st.subheader("🛠 Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("Programming")

    st.write("""
- Python
- SQL
- Pandas
- NumPy
""")

with col2:

    st.success("Machine Learning")

    st.write("""
- Scikit-Learn
- XGBoost
- MLflow
- Feature Engineering
""")

with col3:

    st.success("Deployment")

    st.write("""
- Streamlit
- GitHub
- Joblib
""")

st.markdown("---")

# ----------------------------------------------------
# PROJECT SUMMARY
# ----------------------------------------------------

st.subheader("🏦 Project Summary")

st.info("""
EMI Predict AI is an end-to-end Machine Learning
application that predicts:

• Customer EMI Eligibility

• Maximum Affordable Monthly EMI

using optimized XGBoost models.

The application includes data preprocessing,
feature engineering, model training,
MLflow experiment tracking,
and deployment through Streamlit.
""")

st.markdown("---")

# ----------------------------------------------------
# PROJECT HIGHLIGHTS
# ----------------------------------------------------

st.subheader("🚀 Project Highlights")

st.success("""
✅ End-to-End Machine Learning Workflow

✅ Classification + Regression

✅ Hyperparameter Tuning

✅ MLflow Integration

✅ Streamlit Deployment

✅ Modular Project Structure
""")

st.markdown("---")

# ----------------------------------------------------
# THANK YOU
# ----------------------------------------------------

st.subheader("🙏 Thank You")

st.write("""
Thank you for exploring **EMI Predict AI**.

This project demonstrates practical implementation
of Machine Learning, MLOps concepts,
and deployment using Python and Streamlit.
""")