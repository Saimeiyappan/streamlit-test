import streamlit as st


from utils.model_loader import load_models
from utils.preprocessing import prepare_input

classifier_model, regression_model, label_encoder = load_models()

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EMI Prediction",
    page_icon="🏦",
    layout="wide"
)



# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🏦 EMI Predict AI")
st.subheader("EMI Eligibility & Maximum EMI Prediction")

st.markdown("---")

# --------------------------------------------------
# FORM
# --------------------------------------------------

with st.form("emi_prediction_form"):

    # ==============================================
    # PERSONAL INFORMATION
    # ==============================================

    st.header("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "🎂 Age",
            min_value=18,
            max_value=100,
            value=30
        )

        gender = st.selectbox(
            "🚻 Gender",
            ["Male", "Female"]
        )

    with col2:

        marital_status = st.selectbox(
            "💍 Marital Status",
            ["Single", "Married"]
        )

        education = st.selectbox(
            "🎓 Education",
            [
                "Graduate",
                "High School",
                "Post Graduate",
                "Professional"
            ]
        )

    st.markdown("---")

    # ==============================================
    # EMPLOYMENT INFORMATION
    # ==============================================

    st.header("💼 Employment Information")

    col1, col2 = st.columns(2)

    with col1:

        monthly_salary = st.number_input(
            "💰 Monthly Salary",
            min_value=0,
            value=50000,
            step=1000
        )

        employment_type = st.selectbox(
            "🏢 Employment Type",
            [
                "Government",
                "Private",
                "Self-employed"
            ]
        )

    with col2:

        years_of_employment = st.number_input(
            "📅 Years of Employment",
            min_value=0,
            value=5
        )

        company_type = st.selectbox(
            "🏭 Company Type",
            [
                "Large",
                "MNC",
                "Mid-size",
                "Small",
                "Startup"
            ]
        )

    st.markdown("---")

    # ==============================================
    # FINANCIAL INFORMATION
    # ==============================================

    st.header("💰 Financial Information")

    col1, col2 = st.columns(2)

    with col1:

        monthly_rent = st.number_input(
            "🏠 Monthly Rent",
            min_value=0,
            value=10000,
            step=500
        )
        house_type = st.selectbox(
            "🏠 House Type",
        [
        "Family",
        "Own",
        "Rented"
    ]
    )

        family_size = st.number_input(
            "👨‍👩‍👧 Family Size",
            min_value=1,
            value=4
        )

        dependents = st.number_input(
            "👶 Dependents",
            min_value=0,
            value=2
        )

        school_fees = st.number_input(
            "🏫 School Fees",
            min_value=0,
            value=3000
        )

        college_fees = st.number_input(
            "🎓 College Fees",
            min_value=0,
            value=0
        )

        travel_expenses = st.number_input(
            "🚌 Travel Expenses",
            min_value=0,
            value=2500
        )

    with col2:

        groceries_utilities = st.number_input(
            "🛒 Groceries & Utilities",
            min_value=0,
            value=8000
        )

        other_monthly_expenses = st.number_input(
            "💳 Other Monthly Expenses",
            min_value=0,
            value=4000
        )

        existing_loans = st.selectbox(
            "🏦 Existing Loans",
            ["No", "Yes"]
        )

        current_emi_amount = st.number_input(
            "💵 Current EMI Amount",
            min_value=0,
            value=8000
        )

        credit_score = st.number_input(
            "📈 Credit Score",
            min_value=300,
            max_value=900,
            value=750
        )

        bank_balance = st.number_input(
            "🏛 Bank Balance",
            min_value=0,
            value=150000
        )

        emergency_fund = st.number_input(
            "💼 Emergency Fund",
            min_value=0,
            value=50000
        )

    st.markdown("---")

    # ==============================================
    # LOAN INFORMATION
    # ==============================================

    st.header("🏦 Loan Information")

    col1, col2 = st.columns(2)

    with col1:

        requested_amount = st.number_input(
            "💰 Requested Amount",
            min_value=10000,
            value=500000,
            step=10000
        )

    with col2:

        requested_tenure = st.number_input(
            "📅 Requested Tenure (Months)",
            min_value=6,
            value=60
        )

        emi_scenario = st.selectbox(
            "🚗 EMI Scenario",
            [
                "Home Loan EMI",
                "Education EMI",
                "Home Appliances EMI",
                "Personal Loan EMI",
                "Vehicle EMI"
            ]
        )

    st.markdown("")

    predict_button = st.form_submit_button(
        "🚀 Predict EMI",
        use_container_width=True
    )

st.markdown("---")

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if predict_button:

    new_customer = prepare_input(

        age=age,
        gender=gender,
        marital_status=marital_status,

        monthly_salary=monthly_salary,
        years_of_employment=years_of_employment,

        monthly_rent=monthly_rent,
        family_size=family_size,
        dependents=dependents,

        school_fees=school_fees,
        college_fees=college_fees,

        travel_expenses=travel_expenses,
        groceries_utilities=groceries_utilities,
        other_monthly_expenses=other_monthly_expenses,

        existing_loans=existing_loans,
        current_emi_amount=current_emi_amount,

        credit_score=credit_score,
        bank_balance=bank_balance,
        emergency_fund=emergency_fund,

        requested_amount=requested_amount,
        requested_tenure=requested_tenure,

        education=education,
        employment_type=employment_type,
        company_type=company_type,
        house_type=house_type,
        emi_scenario=emi_scenario
    )

    classification_prediction = classifier_model.predict(new_customer)

    regression_prediction = regression_model.predict(new_customer)

    eligibility = label_encoder.inverse_transform(classification_prediction)

    st.success("Prediction Completed Successfully!")

    st.markdown("## 🎯 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:

        if eligibility[0] == "Eligible":
            st.success(f"✅ EMI Eligibility\n\n**{eligibility[0]}**")
            st.balloons()

        elif eligibility[0] == "Not_Eligible":
            st.error(f"❌ EMI Eligibility\n\n**{eligibility[0]}**")

        else:
            st.warning(f"⚠️ EMI Eligibility\n\n**{eligibility[0]}**")

    with col2:

        st.metric(
            "💰 Maximum Monthly EMI",
            f"₹ {regression_prediction[0]:,.2f}"
        )

