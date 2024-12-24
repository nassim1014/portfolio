import streamlit as st

from src.controllers.projects_controller import ProjectController
from src.controllers.experience_controller import ExperienceController
from src.controllers.certificate_controller import CertificateController
from src.controllers.skill_controller import SkillController

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
    st.image("data/image/utc_grad.jpg", caption="Nassim ZAARI")
    st.title("Navigation")
    #page = st.radio("Go to", ["About Me", "Experience", "Skills", "Projects", "Certificates", "Contact"])
    page = st.sidebar.selectbox("Navigation", ["About Me", "Experience", "Skills", "Projects", "Certificates", "Contact"])

#page = st.session_state.current_page
# About Me Section
if page == "About Me":
    from src.about_me import display_about_me
    display_about_me()

# Experience Section
elif page == "Experience":
  #  from src.experience import display_experience
  #  display_experience()
    experience_controller = ExperienceController()
    # Load experiences from JSON
    experience_controller.load_experiences_from_file("data/experiences.json")
    # Display experiences
    experience_controller.display_experiences()

# Skills Section
elif page == "Skills":
   # Initialize the SkillController
    skill_controller = SkillController()

    # Load skills from JSON file
    skill_controller.load_skills_from_file("data/skills.json")

    # Display skills
    skill_controller.display_skills()
# Projects Section
elif page == "Projects":
    projects_controller = ProjectController()
    # Load projectss from JSON
    projects_controller.load_projects_from_file("data/projects.json")
    # Display projects
    projects_controller.display_projects()

# Certificates Section
elif page == "Certificates":
    certificates_controller = CertificateController()
    # Load certificatess from JSON
    certificates_controller.load_certificates_from_file("data/certificates.json")
    # Display certificates
    certificates_controller.display_certificates()

    
# Contact Section
elif page == "Contact":
    from src.contact import display_contact
    display_contact()

# Footer
st.markdown("---")
st.markdown("© 2024 Nassim ZAARI. All rights reserved.")
