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

#st.sidebar.markdown('''
## Sections
#- [Section 1](#section-1)
#- [Section 2](#section-2)
#''', unsafe_allow_html=True)



age = st.slider('age',  min_value=25, max_value=65, step=1)
years_exp = st.slider('yrsexp',min_value=0,  max_value=50, step=1)
st.write(f"Age = {age} \n\n Year of Experience = {years_exp}")



#@st.cache 
df = pd.read_csv("./salary_df.csv")
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write("In the 'sex' column, 1 = Male, 2 = Female. In the 'regions' column") 
    st.write("I labeled the regions as: 1 = 'Pacific', 2 = 'Mountain', 3 = 'Central', 4 = 'Eastern'")
    st.write(df)
    
X = df[['sex','region','yrsexp','age']]
y = df['salary']
reg = linear_model.LinearRegression()
reg.fit(X.values,y.values)

section_list = sorted(df.region.unique())
selections = ['U.S.','Arts','World']
selections = st.select(
     'Choose at least one section to model (by default all sections are shown)',
     section_list, default = section_list)


female_wage = reg.predict([[2,4,17,40]])
male_wage = reg.predict([[1,4,17,40]])
st.write("With all other variables equal, the male worker earns ${} more than the female worker annually.".format(round(float(male_wage - female_wage)),4))




















