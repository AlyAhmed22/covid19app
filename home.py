import streamlit as st

#''' with st.container():
#    col1,col2=st.columns(2)
 #   with col1: 
  #      st.markdown("'#'")
   #     st.markdown('covid19')
    #with col2:
     #   st.image('download.jpeg',width=200)'''

from page import countries, Regions,about_data # استيراد الملفات الأخرى

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["Home", "Countries", "Regions","About Data"])  # إضافة خيارات التنقل

# Home page
if page == "Home":
    st.title("Home Page")
    st.title('covid19 Data Analysis')
    st.image('download.jpeg',width=200)
    st.write("Welcome to the COVID-19 Data Analysis App!")
    st.header('Description')
    st.markdown('this app is created to analyze the covid19 data')

# Countries page
elif page == "Countries":
    countries.app()  

# Regions page
elif page == "Regions":
    Regions.app()  
elif page== "About Data":
    about_data.app()
