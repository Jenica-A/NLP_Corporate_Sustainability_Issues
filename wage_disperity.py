"""
Streamlit Interactive App to Show Wage Disperity
    
"""
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

st.title("Wage Disperity Simulation")
st.markdown('''This salary data comes from [this kaggle dataset](https://www.kaggle.com/datasets/fedesoriano/gender-pay-gap-dataset)''',unsafe_allow_html=True)
st.write("It contains about 21,000 data points from ...")

#st.sidebar.markdown('''
## Sections
#- [Section 1](#section-1)
#- [Section 2](#section-2)
#''', unsafe_allow_html=True)

data_path = ("./salary_df.csv")


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

#Attempt quick linear regression. 
# based on code from https://www.kaggle.com/code/sarthakniwate13/linear-regression-multiple-variables-example-2

df = pd.read_csv(r'salary_df.csv')
X = df[['sex','region','yrsexp','age']]
y = df['salary']
reg = linear_model.LinearRegression()
reg.fit(X.values,y.values)
female_wage = reg.predict([[2,4,17,40]])
male_wage = reg.predict([[1,4,17,40]])
print("With all other variables equal, the male worker earns ${} more than the female worker annually.".format(round(float(male_wage - female_wage)),4))


"""
Streamlit Interactive 
New York Times Article Archive Topic Modelling 
"""

import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import datetime
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.decomposition import NMF



st.title("Topic Modeling the New York Times")
st.subheader("January 2012 to August 2022")
st.caption("'More information is always better than less. When people know the reason things are happening, even if it's bad news, they can adjust their expectations and react accordingly. Keeping people in the dark only serves to stir negative emotions.' \n\n — Simon Sinek")

st.write("Choose a range of dates and newspaper sections to generate a wordcloud from terms used in article 'snippets'")

data_path = ("./df_snip_filtered.csv")


@st.cache 
def load_data(nrows):
    df = pd.read_csv(data_path, nrows = nrows)
    df.dropna(inplace = True)
    df['pub_date']= pd.to_datetime(df['pub_date']).dt.date
    df = df[["pub_date","section_name","filtered"]]

    return df
df = load_data(1_3900)

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(df)


start_date = st.date_input('Start date', min(df.pub_date))
end_date = st.date_input('End date', max(df.pub_date))
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')



    
section_list = sorted(df.section_name.unique())
selections = ['U.S.','Arts','World']
selections = st.multiselect(
     'Choose at least one section to model (by default all sections are shown)',
     section_list, default = section_list)

st.caption(f"Wordcloud of terms in articles from {start_date} to {end_date} in the following section(s): {selections}")
st.caption(f"Larger words appear more frequently")

filtered_data = df[(df['pub_date'] > pd.Timestamp(start_date)) & (df['pub_date'] < pd.Timestamp(end_date))]
#filtered_data = filtered_data[(filtered_data['section_name'].isin(selections).any(selections))]
filtered_data = filtered_data[(filtered_data['section_name'].isin(selections))]
text = " ".join(word for word in filtered_data.filtered)

#generate text from filtered column of df
text = " ".join(word for word in filtered_data.filtered)


# Create and generate a word cloud image:
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")

#@st.cache
def wordcloud_func(text):
    word_cloud = WordCloud(collocations = False, background_color = 'white',width=3000, height=2000, max_words=200, color_func = black_color_func).generate(text)

    # Display the generated image:
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return(st.pyplot(plt))

wordcloud_func(text)























