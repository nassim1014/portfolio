
import streamlit as st
from utils import txt3

def display_skills():
    st.markdown('''
    ## 🛠️ Skills
    ''')
    
    # Add custom CSS for better spacing and alignment
    st.markdown("""
        <style>
        .skills-section {
            margin-top: 2rem;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        txt3('Programming Languages', '`Python`, `Java`, `SQL`, `HTML/CSS`')
        txt3('Data Science & ML', '`NumPy`, `Pandas`, `Scikit-learn`, `TensorFlow`, `PyTorch`, `Keras`')
        txt3('Web Development', '`Django`, `Flask`, `Spring Boot`, `React`, `Streamlit`')
        txt3('Databases', '`MySQL`, `PostgreSQL`, `MongoDB`, `SQLite`')
        txt3('MLOps', '`Git`, `Docker`, `Mlflow`, `Linux`, `ZenML`')
        txt3('Data Visualization', '`Power BI`,`Matplotlib`, `Seaborn`, `Plotly`')
        txt3('Big Data', '`Apache Spark`, `Hadoop`, `Kafka`')
        txt3('Project Management', '`Agile`, `Scrum`, `Jira`, `ClickUp`')
