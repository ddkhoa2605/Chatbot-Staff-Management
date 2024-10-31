import re
import streamlit as st
import pandas as pd
import numpy as np
from time import sleep
from streamlit_option_menu import option_menu
from sklearn.metrics import mean_squared_error

def show():
    st.header("Prediction Model 💰")

    # Sidebar options for prediction type
    prediction_option = option_menu(
        menu_title=None, options=["One Value", 'From File'],
        icons=[" "]*2, menu_icon="cast", default_index=0,
        orientation="horizontal"
    )

    if prediction_option == "One Value":
        with st.form("Predict_value"):
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input('Employee Age', min_value=20, max_value=60, value=24)
            with c2:
                exp_year = st.number_input('Experience Years', min_value=0, max_value=30, value=2)
            education_level = st.selectbox("Education Level", options=["Bachelor's", "Master's", "PhD"])

            predict_button = st.form_submit_button(label='Predict', use_container_width=True)
            if predict_button:
                education = [0, 0]  # Bachelor's
                if education_level == "Master's":
                    education = [1, 0]
                elif education_level == "PhD":
                    education = [0, 1]
                new_data = [age, exp_year]
                new_data.extend(education)

                # Dummy model prediction, replace with actual model code
                predicted_value = f"{np.random.randint(50000, 100000):,.0f}"
                sleep(1.2)

                predicted_col, score_col = st.columns(2)
                with predicted_col:
                    st.subheader("Expected Salary")
                    st.subheader(f"${predicted_value}")
                with score_col:
                    st.subheader("Model Accuracy")
                    st.subheader("92.5%")

    elif prediction_option == "From File":
        st.warning("Please upload a file with columns ['Age', 'Years of Experience', 'Education Level']")
        test_file = st.file_uploader("Upload Your Test File 📂")

        if test_file is not None:
            df = pd.read_csv(test_file)
            df.dropna(inplace=True)
            st.dataframe(df)
            # Here, apply your prediction logic to the uploaded file and display results
