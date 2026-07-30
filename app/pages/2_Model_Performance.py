import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Model Performance")

st.write("""
This page presents the performance of all machine learning models
trained during the EMI Predict AI project.
""")

st.markdown("---")

# Step 3: Best Models

st.subheader("🏆 Selected Models")

col1, col2 = st.columns(2)

with col1:
    st.success("Classification")
    st.metric("Best Model", "XGBoost")

with col2:
    st.success("Regression")
    st.metric("Best Model", "XGBoost")
    
    
# Step 4: Classification Table

classification_df = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy": [
        0.891093,
        0.888697,
        0.919947,
        0.950370
    ],
    "Precision": [
        0.858732,
        0.892188,
        0.921211,
        0.939611
    ],
    "Recall": [
        0.891093,
        0.888697,
        0.919947,
        0.950370
    ],
    "F1 Score": [
        0.871479,
        0.890406,
        0.899757,
        0.935441
    ]
})

st.subheader("📈 Classification Performance")

st.dataframe(classification_df, use_container_width=True)

# Step 5: Regression Table

regression_df = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],
    "MAE": [
        2979.957055,
        1257.399672,
        782.334163,
        763.373215
    ],
    "RMSE": [
        4156.643724,
        2216.703322,
        1379.308036,
        1175.816712
    ],
    "R² Score": [
        0.710625,
        0.917702,
        0.968136,
        0.976844
    ]
})

st.subheader("📉 Regression Performance")

st.dataframe(regression_df, use_container_width=True)

st.subheader("🧪 MLflow")

st.info("""
Experiment Tracking Enabled

✔ Parameters Logged

✔ Metrics Logged

✔ Models Logged

✔ Best Models Selected
""")

st.markdown("---")

st.subheader("🏅 Conclusion")

st.success("""
Based on the evaluation metrics, XGBoost achieved the best performance
for both classification and regression tasks.

Therefore, XGBoost models were selected for deployment in the
EMI Predict AI application.
""")