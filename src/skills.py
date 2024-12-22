import streamlit as st

def prog_skills():
    pass
def box_skills(title : str , skills_list : list):
    st.markdown(f"### {title}")
    web_cols = st.columns(len(skills_list))
    for col, skill in zip(web_cols, skills_list):
        with col:
            st.markdown(f"<div class='skill-box'>{skill}</div>", unsafe_allow_html=True)


#def display_skills(technologies):
#    st.title("🛠️ Technical Skills")
    
#    col1, col2 = st.columns(2)
    
#    with col1:
#        st.markdown("### Programming Languages")
#        skills_prog = {
#            "Python": 90,
#            "Java": 85,
#            "JavaScript": 80,
#            "R": 75,
#            "C++": 70,
#            "C#": 65
#        }
#        for skill, level in skills_prog.items():
#            st.progress(level/100)
#            st.caption(f"{skill}: {level}%")
    
#    with col2:
#        st.markdown("### Data Science & ML")
#        ds_tools = {
#            "scikit-learn": 85,
#            "TensorFlow": 80,
#            "PyTorch": 75,
#            "NumPy": 90,
#            "Pandas": 90
#        }
#        for tool, level in ds_tools.items():
#            st.progress(level/100)
#            st.caption(f"{tool}: {level}%")
    
  #  st.markdown("### Web Development")
  #  web_skills = ["ReactJS", ".NET", "Spring Boot", "Django", "Flask"]
  #  box_skills("Web Development",web_skills)
    
  #  st.markdown("### DevOps & Tools")
  #  devops_skills = ["Docker", "Git", "MLflow", "Airflow", "Kafka"]
  #  box_skills("DevOps & Tools",devops_skills)

# Technologies Dictionary
technologies = {
    "Programming Languages": [
        "Python", 
        "Java", 
        "JavaScript", 
        "R"
    ],
    
    "Frontend Development": [
        "HTML", 
        "CSS", 
        "JavaScript", 
        "SharePoint", 
        "Power Apps"
    ],
    
    "Backend Development": [
        "Python (Flask, FastAPI)", 
        "SQL (PostgreSQL)", 
        "Docker", 
        "Power Automate"
    ],
    
    "Machine Learning & Data Science": [
        "Machine Learning (scikit-learn, TensorFlow, PyTorch)", 
        "Deep Learning (Keras, TensorFlow, PyTorch)", 
        "Reinforcement Learning (Gym, MFlow)", 
        "Predictive Analytics (RStudio, Python)", 
        "Data Analysis (Pandas, NumPy, scikit-learn)", 
        "Model Evaluation & Tuning", 
        "Feature Engineering"
    ],
    
    "Data Visualization & Reporting": [
        "Power BI", 
        "Excel", 
        "Tableau", 
        "Streamlit"
    ],
    
    "MLOps": [
        "Docker", 
        "MFlow", 
        "Git", 
        "CI/CD pipelines", 
        "Model Deployment"
    ],
    
    "Database & Data Management": [
        "PostgreSQL", 
        "Power Query"
    ],
    
    "Additional Technologies (Familiar, Not Expert)": [
        "AWS", 
        "Azure", 
        "Kubernetes", 
        "Jenkins", 
        "Hadoop", 
        "Apache Spark", 
        "Data Lakes"
    ]
}

def display_skills():
    st.title("🛠️ Technical Skills")
    for key , value in technologies.items():
        box_skills(key,value)
