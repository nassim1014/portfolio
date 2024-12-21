import streamlit as st
import requests
from PIL import Image
import pandas as pd


import streamlit as st
import requests
from PIL import Image
import pandas as pd


def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page Configuration
st.set_page_config(
    page_title="Nassim ZAARI - Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

load_css("style.css")
# Sidebar
with st.sidebar:
    st.image("image/lin.png", caption="Nassim ZAARI")
    st.title("Navigation")
    page = st.radio("Go to", ["About Me", "Experience", "Skills", "Projects", "Certificates", "Contact"])

#page = st.session_state.current_page
# About Me Section
if page == "About Me":
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

# Experience Section
elif page == "Experience":
    st.title("💼 Professional Experience")
    
    # ASTEK Experience
    st.subheader("AI Engineer Intern | ASTEK")
    st.caption("February 2024 - August 2024 | Boulogne-Billancourt, France")
    with st.expander("View Details"):
        st.markdown("""
        - Developed a drone route planning system using Reinforcement Learning, Machine Learning, and Deep Learning
        - Achieved 80-100% success rate and 40% reduction in training time
        - Technologies: Python, PyTorch, Gym, MLflow, PostgreSQL, Docker
        - Worked in an AI team using Scrum methodology
        """)

    # AXA Experience
    st.subheader("Machine Learning Engineer Intern | AXA France")
    st.caption("March 2023 - August 2023 | Nantes, France")
    with st.expander("View Details"):
        st.markdown("""
        - Developed predictive analytics for agent recruitment zones
        - Created Streamlit application for customer potential forecasting
        - Automated workflows using Power Automate
        - Built reports using Power BI
        """)

    # Other experiences...
    st.subheader("Software Engineer Intern | Omnishore Group MedTech")
    st.caption("July 2022 - September 2022 | Casablanca, Morocco")
    
    st.subheader("Data Analyst Intern | Electroplanet")
    st.caption("July 2022 - September 2022 | Casablanca, Morocco")

# Skills Section
elif page == "Skills":
    st.title("🛠️ Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        skills_prog = {
            "Python": 90,
            "Java": 85,
            "JavaScript": 80,
            "R": 75,
            "C++": 70,
            "C#": 65
        }
        for skill, level in skills_prog.items():
            st.progress(level/100)
            st.caption(f"{skill}: {level}%")
    
    with col2:
        st.markdown("### Data Science & ML")
        ds_tools = {
            "scikit-learn": 85,
            "TensorFlow": 80,
            "PyTorch": 75,
            "NumPy": 90,
            "Pandas": 90
        }
        for tool, level in ds_tools.items():
            st.progress(level/100)
            st.caption(f"{tool}: {level}%")
    
    st.markdown("### Web Development")
    web_skills = ["ReactJS", ".NET", "Spring Boot", "Django", "Flask"]
    web_cols = st.columns(len(web_skills))
    for col, skill in zip(web_cols, web_skills):
        with col:
            st.markdown(f"<div class='skill-box'>{skill}</div>", unsafe_allow_html=True)
    
    st.markdown("### DevOps & Tools")
    devops_skills = ["Docker", "Git", "MLflow", "Airflow", "Kafka"]
    devops_cols = st.columns(len(devops_skills))
    for col, skill in zip(devops_cols, devops_skills):
        with col:
            st.markdown(f"<div class='skill-box'>{skill}</div>", unsafe_allow_html=True)

# Projects Section
elif page == "Projects":
    st.title("🚀 Projects")
    
    # Medical Self-Diagnosis Web App
    with st.container():
        st.markdown("""
        ### Medical Self-Diagnosis Web Application
        """)
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            - Developed a web application with 95% prediction accuracy
            - **Technologies**: React JS, Flask, SQLite, Python
            - **Features**:
                * Interactive user interface
                * Machine learning-based diagnosis
                * Secure data storage
            """)
        with col2:
            st.image("/api/placeholder/300/200", caption="Medical App Interface")
    
    # Current Projects
    st.header("🔨 Current Projects")
    st.info("""
    I'm currently working on:
    1. Enhanced Portfolio Website (Streamlit)
    2. Advanced Data Analysis Projects
    3. Contributing to Open Source
    """)

# Certificates Section
elif page == "Certificates":
    st.title("📜 Certificates & Courses")
    
    certificates = [
        {
            "name": "Machine Learning Specialization",
            "platform": "Coursera",
            "date": "2023"
        },
        {
            "name": "Deep Learning Specialization",
            "platform": "Coursera",
            "date": "2023"
        }
    ]
    
    for cert in certificates:
        st.markdown(f"""
        ### {cert['name']}
        **Platform**: {cert['platform']}  
        **Completed**: {cert['date']}
        """)
        st.image("/api/placeholder/400/200", caption=f"{cert['name']} Certificate")

# Contact Section
elif page == "Contact":
    st.title("📫 Contact Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Contact Information
        - 📧 Email: zaari.nassim@gmail.com
        - 📱 Phone: +33 6 99 38 30 36
        - 📍 Location: Paris, France
        """)
    
    with col2:
        st.markdown("""
        ### Professional Profiles
        - [LinkedIn](https://linkedin.com/in/nassim-zaari/)
        - [GitHub](https://github.com/nassim1014)
        - [Credly](https://credly.com/users/nassim-zaari/badges)
        """)
    
    # Contact Form
    st.header("Send me a message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success("Thank you for your message! I'll get back to you soon.")

# Footer
st.markdown("---")
st.markdown("© 2024 Nassim ZAARI. All rights reserved.")
