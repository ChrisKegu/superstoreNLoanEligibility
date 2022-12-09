import streamlit as st
import pandas as pd
import numpy as np

#col1, col2,col3 = st.columns([3, 1])
col1, col2,col3 = st.columns([2,3,2])
#data = np.random.randn(10, 1)

#col1.subheader("Please enter loan amount ")
loan_amount = col2.number_input('Please Enter Loan Amount',min_value=0)


#col2.subheader("A narrow column with the data")
coapplicant_amount = col2.number_input('Please enter CoApplicant Amount',
min_value=0)
#applicant's income
applicant_income = col2.number_input('Please enter your income',min_value=0)

loan_amount_term=col2.number_input('Please enter loan amount term',
min_value=0,step=1)
#education-graduate=0,1 
education=col2.selectbox('Please select your educational level',
('Graduate','Not Graduated'))
if education=='Graduate':
    edu=0
elif education=='Not Graduated':
    edu=1

print(f'Education is {edu}')
#get property area
property_area=col2.selectbox('Please select your property area',
('Urban','Semiurban','Rural'))
#property area: 'Urban': 0, 'Semiurban': 1 ,'Rural': 2 

#get gender
#gender 1=male, 0 female
gender=col2.selectbox('Please select your gender',
('Male','Femal'))

#marital status yes=1,0, self employed no=0
marital_status=col2.selectbox('Are you married?',
('Yes','No'))

self_employed=col2.selectbox('Are you self employed?',
('Yes','No'))

#credit history 1=yes,0
credit_history=col2.selectbox('Do you have any credit history?',
('Yes','No'))

#dependents
#('0','1','2','3 or more'))
dependents=col2.selectbox('Please select the number of dependents you have',
('0','1','2','3 or more'))


