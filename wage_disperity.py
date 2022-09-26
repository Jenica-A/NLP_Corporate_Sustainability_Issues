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
st.markdown('''This salary data comes from [this kaggle dataset](https://www.kaggle.com/datasets/fedesoriano/gender-pay-gap-dataset)''',unsafe_allow_html=True)
st.write("It contains about 21,500 data points from ...")

#@st.cache 
df = pd.read_csv("./salary_df.csv")
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write("In the 'sex' column, 1 = Male, 2 = Female. In the 'regions' column") 
    st.write("I labeled the regions as: 1 = 'Pacific', 2 = 'Mountain', 3 = 'Central', 4 = 'Eastern'")
    st.write(df)
    
age = st.slider('Emplyee Age',  min_value=25, max_value=65, step=1)
years_exp = st.slider('Years of Experience',min_value=0,  max_value=50, step=1)
if age <= years_exp:
    st.warning('please pick a reasonable amount of experience based on employee age for most reliable model results'),
else:
    st.write(f"Age = {age} \n\n Year of Experience = {years_exp}")
    
X = df[['sex','region','yrsexp','age']]
y = df['salary']
reg = linear_model.LinearRegression()
reg.fit(X.values,y.values)

section_list = sorted(df.region.unique())
region = st.selectbox('Choose a region, arbitrarily imagined: 1 = Pacific, 2 = Mountain, 3 = Central, 4 = Eastern',
     section_list)
#st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")


female_wage = np.round(reg.predict([[2,region,years_exp,age]]),2)
male_wage = np.round(reg.predict([[1,region,years_exp,age]]),2)
wage_diff = round(float(male_wage - female_wage),2)
st.header("Model Output")
st.write(f"Female wage is ${female_wage}")
st.write(f"Male wage is ${male_wage}")
st.subheader(f"The wage gap is ${wage_diff}") 
st.write(f"In region #{region}, where employees are {age} years old, with {years_exp} years of experience. The male worker earns more.")





















