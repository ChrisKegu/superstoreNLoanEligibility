import streamlit as st
import pandas as pd
import numpy as np

import pickle

#col1, col2,col3 = st.columns([3, 1])
col1, col2,col3 = st.columns([2,3,2])
#data = np.random.randn(10, 1)
with col2:
    with st.form(key='loan_form1'):
        st.subheader('Loan Eligibility App')
        #col1.subheader("Please enter loan amount ")
        loan_amount = st.number_input('Please Enter Loan Amount',min_value=0)
        #col2.subheader("A narrow column with the data")
        coapplicant_amount = st.number_input('Please enter CoApplicant Amount',
        min_value=0)
        #applicant's income
        applicant_income = st.number_input('Please enter your income',min_value=0)

        loan_amount_term=st.number_input('Please enter loan amount term',
        min_value=0,step=1)
        #education-graduate=0,1 
        education=st.selectbox('Please select your educational level',
        ('Graduate','Not Graduated'))
        if education=='Graduate':
            edu=0
        elif education=='Not Graduated':
            edu=1

        #print('Education is {}'.format(edu))
        #get property area
        property_area=st.selectbox('Please select your property area',
        ('Urban','Semiurban','Rural'))
        #property area: 'Urban': 0, 'Semiurban': 1 ,'Rural': 2 
        if property_area=='Urban':
            prop_area=0
        elif property_area=='Semiurban':
            prop_area=1
        elif property_area=='Rural':
            prop_area=2
        #get gender
        #gender 1=male, 0 female
        gender=st.selectbox('Please select your gender',
        ('Male','Female'))
        if gender=='Male':
            gen1=1
        elif gender=='Female':
            gen1=0
        #print(gen1)
        #marital status yes=1,0, self employed no=0
        marital_status=st.selectbox('Are you married?',
        ('Yes','No'))
        if marital_status=='Yes':
            married=1
        elif marital_status=='No':
            married=0
        self_employed=st.selectbox('Are you self employed?',
        ('Yes','No'))
        if self_employed=='Yes':
            employed=1
        elif self_employed=='No':
            employed=0
        #credit history 1=yes,0
        credit_history=st.selectbox('Do you have any credit history?',
        ('Yes','No'))
        if credit_history=='Yes':
            history=1
        elif credit_history=='No':
            history=0
        #dependents
        #('0','1','2','3 or more'))
        dependents=st.selectbox('Please select the number of dependents you have',
        ('0','1','2','3 or more'))
        if dependents=='0':
            children=0
        elif dependents=='1':
            children=1
        elif dependents=='2':
            children=2
        elif dependents=='3 or more':
            children=3
        
        #submit button
        submit_button=st.form_submit_button(label='Submit')
        if submit_button:
    
    	#Dependents	Education	ApplicantIncome	CoapplicantIncome	
        # LoanAmount	Loan_Amount_Term	Credit_History	
        # Property_Area	Gender	Marital_Status	Self_Employed
            values=[children,edu,applicant_income,coapplicant_amount,
            loan_amount,loan_amount_term,history,prop_area,gen1,married,employed]

            df=pd.DataFrame([values])
            cols=['Dependents', 'Education', 'ApplicantIncome', 'CoapplicantIncome',
            'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area',
            'Gender', 'Marital_Status', 'Self_Employed']
            df.columns=cols
    #

            #loading saved model for prediction
            model_filename = "loan_prediction_model.sav"
            loan_prediction_model = pickle.load(open(model_filename, 'rb'))

            result = loan_prediction_model.predict(df)

    
            if result[0]==1:
                #st.subheader('You qualify for a loan')
                #st.write('You qualify for a loan')
                st.success('# You qualify for a loan')
                #st.info('This is a purely informational message', icon="ℹ️")
                #st.success('success', icon="✅")
                st.balloons()
                st.snow()
            elif result[0]==0:
                st.write('Unfortunately you do not qualify for a loan')
                #st.success('', icon="✅")
                st.warning('Unfortunately you do not qualify for a loan',icon='🙍')

 
col1.image('gh200.jpg')
