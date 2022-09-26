"""
Streamlit Interactive App to Show Wage Disperity
    
"""
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import linear_model
#import matplotlib.pyplot as plt
#%matplotlib inline
#import seaborn as sns


#Quick linear regression code based on https://www.kaggle.com/code/sarthakniwate13/linear-regression-multiple-variables-example-2
st.title("Wage Disperity Simulation")
st.write('This app uses linear regression to model the difference between employee salary, based on gender.')
st.markdown("***")
st.markdown('''The salary data come from [this kaggle dataset](https://www.kaggle.com/datasets/fedesoriano/gender-pay-gap-dataset), where a lengthier explanation of the data can be found.''',unsafe_allow_html=True)
st.markdown('''The data replicate [this 1996 publication](https://docs.iza.org/dp9656.pdf) from the Institute of Labor Economics, Bonn Germany, which explores the lower earnings of female workers compared to their male counterparts''',unsafe_allow_html=True)
st.write("Here, a stripped down version of the data is used for a simple model. \n\n Only sex, region, years of experience and age are included.")
st.markdown("***")


#@st.cache 
df = pd.read_csv("./salary_df.csv")
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write("In the 'sex' column, 1 = Male, 2 = Female") 
    st.write("I labeled the regions as: 1 = 'Pacific', 2 = 'Mountain', 3 = 'Central', 4 = 'Eastern'")
    st.write(df)

st.markdown("***")

st.write('Pick a reasonable amount of experience based on employee age, for the most reliable model results')
age = st.slider('Emplyee Age',  min_value=25, max_value=65, step=1)
st.markdown("***")
years_exp = st.slider('Years of Experience',min_value=0,  max_value=50, step=1)
st.markdown("***")
section_list = sorted(df.region.unique())
region = st.selectbox('Choose a region, arbitrarily imagined: 1 = Pacific, 2 = Mountain, 3 = Central, 4 = Eastern',
     section_list)
st.markdown("***")
st.subheader("Model Input:")
st.write(f"Age = {age} \n\n Years of Experience = {years_exp} \n\n Region = {region}")
st.markdown("***")
    
X = df[['sex','region','yrsexp','age']]
y = df['salary']
reg = linear_model.LinearRegression()
reg.fit(X.values,y.values)


female_wage = np.round(reg.predict([[2,region,years_exp,age]]),2)
male_wage = np.round(reg.predict([[1,region,years_exp,age]]),2)
wage_diff = round(float(male_wage - female_wage),2)
st.subheader("Model Output")
st.write(f"Female wage is ${female_wage}")
st.write(f"Male wage is ${male_wage}")
st.header("Your company's wage gap is ${:,}, annually".format(wage_diff))


















