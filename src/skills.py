import streamlit as st
def display_skills():
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
