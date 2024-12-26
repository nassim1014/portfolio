import streamlit as st
from streamlit_option_menu import option_menu
from src.controllers.projects_controller import ProjectController
from src.controllers.experience_controller import ExperienceController
from src.controllers.certificate_controller import CertificateController
from utils import load_image, load_json_from_drive , get_direct_download_link , load_css
from dotenv import load_dotenv
import os
import requests
from PIL import Image
from io import BytesIO
from streamlit_navigation_bar import st_navbar
from src.about_me import display_about_me

load_dotenv()  # This loads the .env file

# Get the URLs from environment variables
experiences_file_url = os.getenv("EXPERIENCES_URL")
certificates_file_url = os.getenv("CERTIFICATES_URL")
skills_file_url = os.getenv("SKILLS_URL")
projects_file_url = os.getenv("PROJECTS_URL")
image_url = os.getenv("IMAGE_URL")

# Page Configuration
st.set_page_config(
    page_title="Nassim ZAARI - Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

load_css("style.css")
# Sidebar

with st.sidebar:
    if image_url:
        direct_link = get_direct_download_link(image_url)
        image = load_image(direct_link)
        st.image(image, caption="Nassim ZAARI")
    else:
        st.warning("Image URL not found in environment variables.")
        st.title("Navigation")
        # Sidebar navigation

    #page = st.sidebar.radio("Navigation", ["About Me", "Experience", "Skills", "Projects", "Certificates", "Contact"])
    page = option_menu(
        menu_title="Navigation",
    #    options=["About Me", "Experience", "Skills", "Projects", "Certificates"],
    #    icons=["person", "briefcase", "tools", "clipboard", "award", "envelope"],
        options=["About Me", "Experience", "Projects", "Certificates"],
        icons=["person", "briefcase", "clipboard", "award", "envelope"],
        menu_icon="cast",
        default_index=0
    )

# About Me Section
if page == "About Me":
    display_about_me()

# Experience Section
elif page == "Experience":

    experiences_data = load_json_from_drive(experiences_file_url)
    experience_controller = ExperienceController()
    # Load experiences from JSON
    experience_controller.process_experiences(experiences_data)
    # Display experiences
    experience_controller.display_experiences()

# Skills Section
#elif page == "Skills":
#    skills_data = load_json_from_drive(skills_file_url)
   # Initialize the SkillController
#    skill_controller = SkillController()
    
    # Load skills from JSON file
#    skill_controller.process_skills(skills_data)

    # Display skills
#    skill_controller.display_skills()
# Projects Section
elif page == "Projects":
    projects_data = load_json_from_drive(projects_file_url)
    projects_controller = ProjectController()
    # Load projectss from JSON
    projects_controller.process_projects(projects_data)
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
#elif page == "Contact":
#    from src.contact import display_contact
#    display_contact()

# Footer
st.markdown("---")
st.markdown("2024 | Nassim ZAARI | zaari.nassim@gmail.com | +33 6 99 38 30 36")
