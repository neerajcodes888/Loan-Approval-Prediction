import pandas as pd
import datetime
import joblib
import streamlit as st
html_tag="""
    <div style = "background-color:grey;padding:15px">
    <h2 style="color:yellow;text-align:center;">Loan Approval Prediction World</h2>
    <ul>
        <li style="color:red;">
        <h5 style="color:blue;text-align:centre;">Welcome to loan approval  Prediction System Made by Machine Learning </h5>
        </li>
        <li style="color:red;"> 
        <h5 style="color:blue;text-align:centre;">     Predict Your loan is approved or not!</h5>
        </li>
        <li style="color:red;">
        <h5 style="color:blue;text-align:centre;">Fill the details Carefully!!!</h5></li>
    </ul>   
    
    <h5 style="color:black;text-align:left;">Incase of Clarifiction or doubts Contact me:-> 
    <ul>
      <li style="color:yellow;">
      <a href="https://www.linkedin.com/in/neeraj-kumar-9a75811a2" style="color:#36AE7C;">Linkdin Profile</a>
      </li>
      <li style="color:yellow;">
      <a href="https://github.com/neerajcodes888" style="color:#36AE7C;">Github Profile</a
      </li>
   </ul>
    </h5> 
      </div>
    """
model=joblib.load('loan_approval_model')
    
st.markdown(html_tag,unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
 
p1=st.selectbox("Please Choose Your Gender",('Male','Female'))
if p1=='Male':
    arg1=1
else:
    arg1=0
p2=st.selectbox("What is Your Marital Status",('Married','Unmarried'))
if p2=='Married':
    arg2=1
elif p2=='Unmarried':
    arg2=0
p3=st.selectbox("How many dependents are in Your Family",('0','1','2','3 or more'))
if p3=='0':
    arg3=0
elif p3=='1':
    arg3=1
elif p3=='2':
    arg3=2
elif p3=='3 or more':
    arg3=4
p4=st.selectbox("Are you Self-Employed",('Yes','No'))
if p4=='Yes':
    arg4=1
else:
    arg4=0
p5 =st.selectbox("What is Your Education level",('Graduated','Not Graduated'))
if p4=='Graduated':
    arg5=1
else:
    arg5=0
arg6 = st.number_input("What is income of the Loan Applicant",150,81000,step=100)
arg7 = st.number_input("What is income of the Loan Co-Applicant",0,50000,step=100)
arg8 = st.number_input("Enter the amount of Loan You Want(in Lakhs)",1,700,step=10)
arg9 = st.number_input("In how many months , you will repay the Loan Amount",12,480,step=1)
p6=st.selectbox("Does Credit History meet your Guidelines",('Yes','No'))
if p6=='Yes':
    arg10=1
else:
    arg10=0
p7=st.selectbox("In which area does your property exist",('Urban','SemiUrban','Rural'))
if p7=='Urban':
    arg11=0
elif p7=='SemiUrban':
    arg11=1
elif p7=='Rural':
    arg11=2

final_data=pd.DataFrame({
    'Gender':arg1,
    'Married':arg2,
    'Dependents':arg3,
    'Education':arg5,
    'Self_Employed':arg4,
    'ApplicantIncome':arg6,
    'CoapplicantIncome':arg7,
    'LoanAmount':arg8,
    'Loan_Amount_Term':arg9,
    'Credit_History':arg10,
    'Property_Area':arg11
},index=[0])

if st.button('Predict'):
    loan=model.predict(final_data)
    if loan==1:
        st.balloons()
        st.success("Congratilations,Loan is successfully Approved")
    else:
        st.warning("Sorry,You are not eligible for Loan approval")