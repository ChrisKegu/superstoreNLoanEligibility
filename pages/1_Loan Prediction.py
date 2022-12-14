import streamlit as st 
import pickle
import os
import pandas as pd

css_path=os.path.join('static','style.css')

with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
    
with st.form(key='loan_form',clear_on_submit=True):

    st.markdown('<h2>Loan Eligibility Prediction</h2>', unsafe_allow_html=True)

    st.markdown('<h2>User Information</h2>', unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        fname = col1.text_input('First Name', placeholder='Enter your first name here')
        lname = col2.text_input( 'Last Name', placeholder='Enter your last name here')
    
    st.markdown('<h2>Loan Information</h2>', unsafe_allow_html=True)
    
    with st.container():
        col3, col4 = st.columns(2)
        loan_amount = col3.number_input('Enter Loan Amount', min_value=0)
        # col2.subheader("A narrow column with the data")
        coapplicant_amount = col4.number_input('Enter CoApplicant Amount',
                                           min_value=0)
    with st.container():
        col5, col6 = st.columns(2)
        # applicant's income
        applicant_income = col5.number_input('Enter your income', min_value=0)

        loan_amount_term = col6.number_input('Enter loan amount term',
                                         min_value=0, step=1)
    with st.container():
        col7, col8 = st.columns(2)
        # education-graduate=0,1
        education = col7.selectbox('Please select your educational level',
                               ('Graduate', 'Not Graduated'))
        if education == 'Graduate':
            edu = 0
        elif education == 'Not Graduated':
            edu = 1
        
        # get property area
        property_area = col8.selectbox('Please select your property area',
                                   ('Urban', 'Semiurban', 'Rural'))
        # property area: 'Urban': 0, 'Semiurban': 1 ,'Rural': 2
        if property_area == 'Urban':
            prop_area = 0
        elif property_area == 'Semiurban':
            prop_area = 1
        elif property_area == 'Rural':
            prop_area = 2
    with st.container():
        col9,col10=st.columns(2)
        # get gender
        # gender 1=male, 0 female
        gender = col9.selectbox('Please select your gender',
                            ('Male', 'Female'))
        if gender == 'Male':
            gen1 = 1
        elif gender == 'Female':
            gen1 = 0
    #print(gen1)
    # marital status yes=1,0, 
        marital_status = col10.selectbox('Are you married?',
                                    ('Yes', 'No'))
        if marital_status == 'Yes':
            married = 1
        elif marital_status == 'No':
            married = 0
        #self employed no=0
    with st.container():
        #self employed no=0
        col11,col12=st.columns(2)
        self_employed = col11.selectbox('Are you self employed?',
                                   ('Yes', 'No'))
        if self_employed == 'Yes':
            employed = 1
        elif self_employed == 'No':
            employed = 0
        # credit history 1=yes,0=no
        credit_history = col12.selectbox('Do you have any credit history?', ('Yes', 'No'))
        if credit_history == 'Yes':
            history = 1
        elif credit_history == 'No':
            history = 0
    with st.container():
        col13,col14=st.columns(2)
        # dependents
        # ('0','1','2','3 or more'))
        dependents = col13.selectbox('Please select the number of dependents you have',
                              ('0', '1', '2', '3 or more'))
        if dependents == '0':
            children = 0
        elif dependents == '1':
            children = 1
        elif dependents == '2':
            children = 2
        elif dependents == '3 or more':
            children = 3
        col14.markdown('')
        col14.markdown('')
        submit_button=col14.form_submit_button('Submit',type='primary')
if submit_button:
    # blah blah blah
    # Dependents	Education	ApplicantIncome	CoapplicantIncome
    # LoanAmount	Loan_Amount_Term	Credit_History
    # Property_Area	Gender	Marital_Status	Self_Employed
    if fname=='' or lname=='':
        st.warning('First name or last name required', icon="??????")
    else:

        values = [children, edu, applicant_income, coapplicant_amount,
              loan_amount, loan_amount_term, history, prop_area, gen1, married, employed]

        df = pd.DataFrame([values])
        cols = ['Dependents', 'Education', 'ApplicantIncome', 'CoapplicantIncome',
            'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area',
            'Gender', 'Marital_Status', 'Self_Employed']
        df.columns = cols
    #

    # loading saved model for prediction
        model_path=os.path.join('static',)
        model_filename = "loan_prediction_model.sav"
        model_path=os.path.join('static',model_filename)
        loan_prediction_model = pickle.load(open(model_path, 'rb'))

        result = loan_prediction_model.predict(df)


        if result[0] == 1:
            #st.header(f'Congratulations {fname} {lname}')
            #st.subheader('# You qualify for a loan')
            # st.write('You qualify for a loan')
            #st.success('##  qualify for a loan')
            #st.info('This is a purely informational message', icon="??????")
            st.success('# Hello {} {} you qualify for a loan'.format(fname,lname), icon="???")
            st.balloons()
            # st.snow()
        elif result[0] == 0:
            #st.write('Unfortunately you do not qualify for a loan')
            # st.success('', icon="???")
            st.warning('Hello {} {} ,unfortunately you do not qualify for a loan'.format(fname,lname), icon='????')
