import pandas as pd

def prepare_input(
    age,
    gender,
    marital_status,
    monthly_salary,
    years_of_employment,
    monthly_rent,
    family_size,
    dependents,
    school_fees,
    college_fees,
    travel_expenses,
    groceries_utilities,
    other_monthly_expenses,
    existing_loans,
    current_emi_amount,
    credit_score,
    bank_balance,
    emergency_fund,
    requested_amount,
    requested_tenure,
    education,
    employment_type,
    company_type,
    house_type,
    emi_scenario
):
    # binary encoding (gender , marital_status, existing_loans)
    
    gender = 1 if gender == "Male" else 0
    marital_status = 1 if marital_status == "Married" else 0
    existing_loans = 1 if existing_loans == "Yes" else 0
    
    # one hot encoding 
    # Education
    
    education_high_school = 1 if education == "High School" else 0

    education_post_graduate = 1 if education == "Post Graduate" else 0

    education_professional = 1 if education == "Professional" else 0
    
    # Employment Type
    
    employment_private = 1 if employment_type == "Private" else 0

    employment_self_employed = 1 if employment_type == "Self-employed" else 0
    
    # Company Type
    
    company_mnc = 1 if company_type == "MNC" else 0

    company_mid_size = 1 if company_type == "Mid-size" else 0

    company_small = 1 if company_type == "Small" else 0

    company_startup = 1 if company_type == "Startup" else 0
    
    # House Type
    
    house_own = 1 if house_type == "Own" else 0

    house_rented = 1 if house_type == "Rented" else 0
    
    # EMI Scenario
    
    emi_education = 1 if emi_scenario == "Education EMI" else 0

    emi_home_appliances = 1 if emi_scenario == "Home Appliances EMI" else 0

    emi_personal = 1 if emi_scenario == "Personal Loan EMI" else 0

    emi_vehicle = 1 if emi_scenario == "Vehicle EMI" else 0
    
    
    new_customer = pd.DataFrame({

        "age": [age],
        "gender": [gender],
        "marital_status": [marital_status],
        "monthly_salary": [monthly_salary],
        "years_of_employment": [years_of_employment],
        "monthly_rent": [monthly_rent],
        "family_size": [family_size],
        "dependents": [dependents],
        "school_fees": [school_fees],
        "college_fees": [college_fees],
        "travel_expenses": [travel_expenses],
        "groceries_utilities": [groceries_utilities],
        "other_monthly_expenses": [other_monthly_expenses],
        "existing_loans": [existing_loans],
        "current_emi_amount": [current_emi_amount],
        "credit_score": [credit_score],
        "bank_balance": [bank_balance],
        "emergency_fund": [emergency_fund],
        "requested_amount": [requested_amount],
        "requested_tenure": [requested_tenure],

        "education_High School": [education_high_school],
        "education_Post Graduate": [education_post_graduate],
        "education_Professional": [education_professional],

        "employment_type_Private": [employment_private],
        "employment_type_Self-employed": [employment_self_employed],

        "company_type_MNC": [company_mnc],
        "company_type_Mid-size": [company_mid_size],
        "company_type_Small": [company_small],
        "company_type_Startup": [company_startup],

        "house_type_Own": [house_own],
        "house_type_Rented": [house_rented],

        "emi_scenario_Education EMI": [emi_education],
        "emi_scenario_Home Appliances EMI": [emi_home_appliances],
        "emi_scenario_Personal Loan EMI": [emi_personal],
        "emi_scenario_Vehicle EMI": [emi_vehicle]

    })
    return new_customer
  

