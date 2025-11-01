import streamlit as st
import pandas as pd
from translations import dropdown_vals

def login_page(t, valid_user, valid_pass):
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        st.title(t["login_title"])
        username = st.text_input(t["username"])
        password = st.text_input(t["password"], type='password')
        if st.button(t["login_button"]):
            if username == valid_user and password == valid_pass:
                st.session_state.logged_in = True
                st.success(t["login_success"])
    else:
        st.info(f"{t['login_success']} {t['select_language']} to continue.")

def stroke_prediction_app(t, model, lang):
    st.title(t["app_title"])
    if st.button(t["logout_button"]):
        st.session_state.logged_in = False
        return
    
    # Two column layout for inputs
    col1, col2 = st.columns(2)

    with col1:
        gender_idx = st.selectbox(t["gender"], list(range(len(dropdown_vals["gender"][lang]))),
                                 format_func=lambda i: dropdown_vals["gender"][lang][i])
        hypertension_idx = st.selectbox(t["hypertension"], [0, 1],
                                       format_func=lambda i: dropdown_vals["yesno"][lang][i])
        heart_idx = st.selectbox(t["heart_disease"], [0, 1],
                                format_func=lambda i: dropdown_vals["yesno"][lang][i])
        married_idx = st.selectbox(t["ever_married"], [0, 1],
                                  format_func=lambda i: dropdown_vals["yesno"][lang][i])
        age = st.number_input(t["age"], min_value=0, max_value=120, value=50)

    with col2:
        work_idx = st.selectbox(t["work_type"], list(range(len(dropdown_vals["work_type"][lang]))),
                               format_func=lambda i: dropdown_vals["work_type"][lang][i])
        residence_idx = st.selectbox(t["residence_type"], [0, 1],
                                    format_func=lambda i: dropdown_vals["residence"][lang][i])
        avg_glucose = st.number_input(t["avg_glucose"], min_value=50.0, max_value=300.0, value=100.0)
        bmi = st.number_input(t["bmi"], min_value=10.0, max_value=70.0, value=25.0)
        smoking_idx = st.selectbox(t["smoking_status"], list(range(len(dropdown_vals["smoking"][lang]))),
                                  format_func=lambda i: dropdown_vals["smoking"][lang][i])

    if st.button(t["predict_button"]):
        input_data = pd.DataFrame([[
            gender_idx, age, hypertension_idx, heart_idx, married_idx,
            work_idx, residence_idx, avg_glucose, bmi, smoking_idx
        ]], columns=[
            'gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
            'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'
        ])
        pred_prob = model.predict_proba(input_data)[0][1]
        st.success(f"{t['prediction_result']} {pred_prob*100:.2f}%")
