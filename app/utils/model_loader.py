import os
import joblib
import streamlit as st


# --------------------------------------------------
# MODEL DIRECTORY
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "models")


# --------------------------------------------------
# LOAD ALL MODELS
# --------------------------------------------------

@st.cache_resource
def load_models():

    classifier_model = joblib.load(
        os.path.join(MODEL_DIR, "best_xgb_classifier_pipeline.pkl")
    )

    regression_model = joblib.load(
        os.path.join(MODEL_DIR, "best_xgb_pipeline.pkl")
    )

    label_encoder = joblib.load(
        os.path.join(MODEL_DIR, "label_encoder.pkl")
    )

    return classifier_model, regression_model, label_encoder