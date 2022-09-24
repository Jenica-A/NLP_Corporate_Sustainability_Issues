"""
Streamlit Interactive Plots Demo
    
Example of a line chart of time-series simulation in Matplotlib
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulation")
st.write("'We have to realize that computers are simulators and then figure out what to simulate.' \n\n â€” Alan Kay")

trend = st.slider('Trend',  min_value=0.001, max_value=0.10, step=0.01)
noise = st.slider('Noise',min_value=0.01,  max_value=0.10, step=0.01)
st.write(f"Trend = {trend} \n\n Noise = {noise}")

intial_value = 1
n_series = 10 
time_series = np.cumprod(intial_value + np.random.normal(trend, noise, (100, n_series)), 
                         axis=0)

# st.line_chart(time_series)

fig, ax = plt.subplots()
for ts in time_series.T:
    ax.plot(ts)

st.pyplot(fig)

# Notes:
# - Switch from function to procedural
# - Lag in rendering
# - When you deploy you have to add an external dependency file (requirements.txt)

#Attempt quick linear regression. 
# based on code from https://www.kaggle.com/code/sarthakniwate13/linear-regression-multiple-variables-example-2
# importing essential libraries
import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

df = pd.read_csv(r'salary_df.csv')
X = df[['sex','region','yrsexp','age']]
y = df['salary']
reg = linear_model.LinearRegression()
reg.fit(X.values,y.values)
female_wage = reg.predict([[2,4,17,40]])
male_wage = reg.predict([[1,4,17,40]])
print("With all other variables equal, the male worker earns ${} more than the female worker annually.".format(round(float(male_wage - female_wage)),4))























