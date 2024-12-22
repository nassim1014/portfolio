import streamlit as st
def display_about_me():
    st.title("👋 Hello, I'm Nassim ZAARI")
    st.header("Software Engineer | Data Scientist")
        
    col1, col2 = st.columns(2)
    with col1:
            st.markdown("""
            ### Professional Summary
            Young graduate with solid training in Data Science and Software Development. 
            Passionate about creating innovative solutions and leveraging data for business impact.
            
            ### Education
            - **Master's Degree** in Machine Learning and Complex Systems Optimization
            * University of Technology of Compiègne (GPA: 4.77/5)
            * 2022 - 2024
            
            - **Engineering Degree** in Computer Science
            * Mohammadia School of Engineers
            * 2020 - 2023
            """)
        
    with col2:
            st.markdown("""
            ### Languages
            - French (Bilingual)
            - English (Bilingual)
            - Arabic (Native)
            
            ### Professional Values
            - Team Collaboration
            - Adaptability
            - Autonomy
            - Rigor
            """)