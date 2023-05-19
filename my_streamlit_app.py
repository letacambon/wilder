import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please choise your favorit region") 

cars = pd.read_csv('C:\Formation\odyssey csv\cars.csv')

viz_correlation = sns.heatmap(cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

if st.button('Click on'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
