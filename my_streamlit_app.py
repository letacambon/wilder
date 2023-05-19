import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('Hello Wilders, welcome to my application!')

cars = pd.read_csv('C:\Formation\odyssey csv\cars.csv')

viz_correlation = sns.heatmap(cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

cars = pd.DataFrame(cars)

region = st.selectbox('Filtrer par région', ['Toutes les régions', 'US', 'Europe', 'Japan'])
button_clicked = st.button("Sélectionner")


if button_clicked:
    if region != 'Toutes les régions':
        filtered_cars = cars.loc[cars['continent'] == region, :]
        st.dataframe(filtered_cars)  # Affiche les valeurs du DataFrame filtré
    else:
        st.dataframe(cars)  # Affiche toutes les valeurs du DataFrame