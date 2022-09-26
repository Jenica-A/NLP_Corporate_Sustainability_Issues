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
    
#st.sidebar.markdown('''
## Sections
#- [Section 1](#section-1)
#- [Section 2](#section-2)
#''', unsafe_allow_html=True)

age = st.slider('age',  min_value=25, max_value=65, step=1)
years_exp = st.slider('yrsexp',min_value=0,  max_value=50, step=1)
st.write(f"Age = {age} \n\n Year of Experience = {years_exp}")
    
X = df[['sex','regions','yrsexp','age']]
y = df['salary']
reg = linear_model.LinearRegression()
reg.fit(X.values,y.values)

section_list = sorted(df.regions.unique())
regions = st.selectbox('Choose a region (Original data has regions numbered 1.0-4.0; here they arbitrarily labeled: 1 = Pacific, 2 = Mountain, 3 = Central, 4 = Eastern',
     section_list)
#st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")


female_wage = reg.predict([[2,regions,years_exp,age]])
male_wage = reg.predict([[1,regions,years_exp,age]])
wage_diff = round(float(male_wage - female_wage),2)
st.write("female wage is $",female_wage)
st.write("male wage is $",male_wage)
st.write(f"In cases where emplyees in region {regions}, who are {age} years old, with {years_exp} years of experience, the male worker earns ${wage_diff} more than the female worker annually.")





















