import streamlit as st

from src.controllers.projects_controller import ProjectController
from src.controllers.experience_controller import ExperienceController
from src.controllers.certificate_controller import CertificateController
from src.controllers.skill_controller import SkillController
from utils import load_json_from_drive

from dotenv import load_dotenv
import os

load_dotenv()  # This loads the .env file

# Get the URLs from environment variables
experiences_file_url = os.getenv("EXPERIENCES_URL")
certificates_file_url = os.getenv("CERTIFICATES_URL")
skills_file_url = os.getenv("SKILLS_URL")
projects_file_url = os.getenv("PROJECTS_URL")

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

    experiences_data = load_json_from_drive(experiences_file_url)
    experience_controller = ExperienceController()
    # Load experiences from JSON
 #   experience_controller.load_experiences_from_file("data/experiences.json")
    experience_controller.load_experiences(experiences_data)
    # Display experiences
    experience_controller.display_experiences()

# Skills Section
elif page == "Skills":
    skills_data = load_json_from_drive(skills_file_url)
   # Initialize the SkillController
    skill_controller = SkillController()
    
    # Load skills from JSON file
    skill_controller.load_skills(skills_data)

    # Display skills
    skill_controller.display_skills()
# Projects Section
elif page == "Projects":
    projects_data = load_json_from_drive(projects_file_url)
    projects_controller = ProjectController()
    # Load projectss from JSON
    projects_controller.load_projects(projects_data)
    # Display projects
    projects_controller.display_projects()

# Certificates Section
elif page == "Certificates":
    certificates_data = load_json_from_drive(certificates_file_url)
    certificates_controller = CertificateController()
    # Load certificatess from JSON
    certificates_controller.load_certificates(certificates_data)
    # Display certificates
    certificates_controller.display_certificates()

    
# Contact Section
elif page == "Contact":
    from src.contact import display_contact
    display_contact()

# Footer
st.markdown("---")
st.markdown("© 2024 Nassim ZAARI. All rights reserved.")
