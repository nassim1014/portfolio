import streamlit as st

class SkillView:
    @staticmethod
    def box_skill(title : str , skills_list : list):
        st.markdown(f"### {title}")
        cols = st.columns(4)
        for col, skill in zip(cols, skills_list):
            with col:
                st.markdown(
                    f"<div class='skill-box' style='color: white;'>{skill}</div>",
                    unsafe_allow_html=True
                )
    @staticmethod
    def display_skills(technologies):
        st.title("🛠️ Technical Skills")
        for category in technologies:
            SkillView.box_skill(category['name'], category['skills'])



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