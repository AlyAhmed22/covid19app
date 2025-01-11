import streamlit as st
import pandas as pd

def app():

    # Load Data
    @st.cache_data
    def load_data():
        df = pd.read_csv('covid19app/WHO-COVID-19-global-daily-data (1).csv')
        df['Date_reported'] = pd.to_datetime(df['Date_reported'])
        return df

    df = load_data()

    # About Data
    st.title('About Data')
    st.markdown('''
    This app is created to analyze the Covid-19 data.
    ''')

    # Display Data
    st.header('Data')
    if st.checkbox('Show Data'):
        st.write(df)
