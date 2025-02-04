import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# App Configuration
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='🩺')

# Load models
diabetes_model = pickle.load(open(r"C:\Users\gargp\OneDrive\Documents\Downloads\predictions\training-models\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\gargp\OneDrive\Documents\Downloads\predictions\training-models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\gargp\OneDrive\Documents\Downloads\predictions\training-models\parkinsons_model.sav", 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        'Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson\'s Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Input Validation Function
def validate_input(value):
    try:
        return float(value)
    except ValueError:
        return None  # Return None for invalid inputs

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    
    # Input Fields
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
        skin_thickness = st.text_input('Skin Thickness Value')
        diabetes_pedigree = st.text_input('Diabetes Pedigree Function')
    with col2:
        glucose = st.text_input('Glucose Level')
        insulin = st.text_input('Insulin Level')
        age = st.text_input('Age of the Person')
    with col3:
        blood_pressure = st.text_input('Blood Pressure Value')
        bmi = st.text_input('BMI Value')

    if st.button('Diabetes Test Result'):
        # Validate inputs
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
        user_input = [validate_input(x) for x in user_input]

        if None in user_input:
            st.error("Please enter valid numeric values for all fields.")
        else:
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic.' if diab_prediction[0] == 1 else 'The person is not diabetic.'
            st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    
    # Input Fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        restecg = st.text_input('Resting ECG Results')
        oldpeak = st.text_input('Oldpeak')
        ca = st.text_input('Number of Major Vessels (CA)')
        exang = st.text_input('Exercise-Induced Angina (1 = Yes, 0 = No)')

    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
        thalach = st.text_input('Maximum Heart Rate Achieved')
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
        thal = st.text_input('Thal (3 = Normal, 6 = Fixed Defect, 7 = Reversible Defect)')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
        chol = st.text_input('Serum Cholesterol (mg/dL)')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL (1 = True, 0 = False)')
        

    if st.button('Heart Disease Test Result'):
        # Validate inputs
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [validate_input(x) for x in user_input]

        if None in user_input:
            st.error("Please enter valid numeric values for all fields.")
        else:
            heart_prediction = heart_model.predict([user_input])
            heart_diagnosis = 'The person has heart disease.' if heart_prediction[0] == 1 else 'The person does not have heart disease.'
            st.success(heart_diagnosis)

# Parkinson's Prediction
if selected == 'Parkinson\'s Prediction':
    st.title('Parkinson\'s Disease Prediction Using ML')

    # Input Fields with Descriptions
    st.markdown(
        """
        **Input Features Explanation:**
        - **MDVP:Fo(Hz)**: Average vocal fundamental frequency (pitch).
        - **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency.
        - **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency.
        - **MDVP:Jitter(%)**: Variation in the frequency of the voice.
        - **MDVP:Jitter(Abs)**: Absolute variation in fundamental frequency.
        - **MDVP:RAP**: Relative Amplitude Perturbation (short-term jitter).
        - **MDVP:PPQ**: Five-point Period Perturbation Quotient.
        - **Jitter:DDP**: Average absolute difference of differences between consecutive periods.
        - **MDVP:Shimmer**: Variation in the amplitude of the voice.
        - **MDVP:Shimmer(dB)**: Shimmer measured in decibels.
        - **Shimmer:APQ3**: Three-point Amplitude Perturbation Quotient.
        - **Shimmer:APQ5**: Five-point Amplitude Perturbation Quotient.
        - **MDVP:APQ**: Amplitude Perturbation Quotient (11-point).
        - **Shimmer:DDA**: Average absolute difference of differences between consecutive amplitudes.
        - **NHR**: Noise-to-Harmonics Ratio.
        - **HNR**: Harmonics-to-Noise Ratio.
        - **Status**: Clinical status of the subject (1 = Parkinson's, 0 = Healthy).
        - **RPDE**: Recurrence Period Density Entropy (a nonlinear dynamical measure).
        - **DFA**: Detrended Fluctuation Analysis.
        - **Spread1**: Nonlinear measure of fundamental frequency variation.
        - **Spread2**: Nonlinear measure of voice amplitude variation.
        - **D2**: Correlation dimension (a nonlinear measure of signal complexity).
        - **PPE**: Pitch Period Entropy (a measure of voice irregularity).
        """
    )

    # Input Fields
    col1, col2, col3 = st.columns(3)
    with col1:
        mdvp_fo = st.text_input('MDVP:Fo(Hz) (Average vocal fundamental frequency)')
        mdvp_jitter = st.text_input('MDVP:Jitter(%) (Frequency variation)')
        mdvp_rap = st.text_input('MDVP:RAP (Relative Amplitude Perturbation)')
        jitter_ddp = st.text_input('Jitter:DDP (Absolute frequency difference)')
        shimmer_apq3 = st.text_input('Shimmer:APQ3 (Three-point amplitude variation)')
        nhr = st.text_input('NHR (Noise-to-Harmonics Ratio)')
        spread1 = st.text_input('Spread1 (Frequency variation measure)')
        d2 = st.text_input('D2 (Signal complexity measure)')

    with col2:
        mdvp_fhi = st.text_input('MDVP:Fhi(Hz) (Maximum vocal fundamental frequency)')
        mdvp_jitter_abs = st.text_input('MDVP:Jitter(Abs) (Absolute frequency variation)')
        mdvp_ppq = st.text_input('MDVP:PPQ (Five-point frequency variation)')
        mdvp_shimmer = st.text_input('MDVP:Shimmer (Amplitude variation)')
        shimmer_apq5 = st.text_input('Shimmer:APQ5 (Five-point amplitude variation)')
        hnr = st.text_input('HNR (Harmonics-to-Noise Ratio)')
        spread2 = st.text_input('Spread2 (Amplitude variation measure)')
        ppe = st.text_input('PPE (Pitch Period Entropy)')

    with col3:
        mdvp_flo = st.text_input('MDVP:Flo(Hz) (Minimum vocal fundamental frequency)')
        shimmer_dba = st.text_input('MDVP:Shimmer(dB) (Amplitude variation in dB)')
        mdvp_apq = st.text_input('MDVP:APQ (11-point amplitude variation)')
        shimmer_dda = st.text_input('Shimmer:DDA (Amplitude difference measure)')
        status = st.text_input('Status (1 = Parkinson\'s, 0 = Healthy)')
        rpde = st.text_input('RPDE (Recurrence Period Density Entropy)')
        dfa = st.text_input('DFA (Detrended Fluctuation Analysis)')
        
       

    # Button and Prediction Logic
    if st.button('Parkinson\'s Test Result'):
        # Collect inputs into a list
        user_input = [
            mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter, mdvp_jitter_abs,
            mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, shimmer_dba,
            shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr,
            hnr, status, rpde, dfa, spread1, spread2, d2, ppe
        ]
        
        # Validate inputs
        user_input = [validate_input(x) for x in user_input]

        if None in user_input:
            st.error("Please enter valid numeric values for all fields.")
        else:
            # Make prediction using the Parkinson's model
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = 'The person has Parkinson\'s disease.' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinson\'s disease.'
            st.success(parkinsons_diagnosis)

