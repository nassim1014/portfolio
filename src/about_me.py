import streamlit as st
from src.contact import display_contact
def display_about_me():
        st.title("👋 Hello, I'm Nassim ")
        st.markdown("""
        Young graduate with solid training in Data Science and Software Development. 
        Passionate about creating innovative solutions and leveraging data for business impact.
        
        - Exploratory Data Analysis and Predictive Model Development | **AI - Python - Pytorch - Tensorflow**.     
        - Front-end and Back-end Development  | **React - Java - Python - SQL**.     
                """)

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
                st.subheader("Master's Degree @ **University of Technology of Compiègne**")
                #st.write("**University of Technology of Compiègne**")
                st.write("Machine Learning and Complex Systems Optimization")
                st.write("2022 - 2024 | Compiègne, France")

                st.subheader("Engineering Degree @ **Mohammadia School of Engineers**")
                #st.write("**Mohammadia School of Engineers**")
                st.write("Computer Science")
                st.write("2020 - 2023 | Rabat, Morocco")
        
        with col2:
            st.markdown("""
            ### Languages
            - French (Bilingual)
            - English (Bilingual)
            - Arabic (Native) """)
            st.markdown("""
            ### Professional Values
            - Team Collaboration
            - Adaptability
            - Autonomy
            - Rigor
            """)
        st.markdown("---")
        display_contact()