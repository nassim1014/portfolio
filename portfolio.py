import streamlit as st
from streamlit_option_menu import option_menu
from src.controllers.projects_controller import ProjectController
from src.controllers.experience_controller import ExperienceController
from src.controllers.certificate_controller import CertificateController
from src.controllers.skill_controller import SkillController
from utils import load_json_from_drive , get_direct_download_link
from streamlit_navigation_bar import st_navbar
from dotenv import load_dotenv
import os
import requests
from PIL import Image
from io import BytesIO
from PIL import Image, ImageOps, ImageDraw

def create_circular_image(img, size):
#    img = Image.open(image_path)
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    output = ImageOps.fit(img, (size, size), centering=(0.5, 0.5))
    output.putalpha(mask)
    return output

load_dotenv()  # This loads the .env file

# Get the URLs from environment variables
experiences_file_url = os.getenv("EXPERIENCES_URL")
certificates_file_url = os.getenv("CERTIFICATES_URL")
skills_file_url = os.getenv("SKILLS_URL")
projects_file_url = os.getenv("PROJECTS_URL")
image_url = os.getenv("IMAGE_URL")

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

# filepath: /C:/Users/heeln/OneDrive/Documents/portfolio/portfolio.py



with st.sidebar:
    if image_url:
        direct_link = get_direct_download_link(image_url)
        response = requests.get(direct_link)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="Nassim ZAARI")
            #image = "images/utc_grad.jpg"
            #circular_image = create_circular_image(image, 300)
            #st.image(circular_image , caption="Nassim ZAARI")
        else:
            st.warning("Unable to load image from the provided URL.")
    else:
        st.warning("Image URL not found in environment variables.")
        st.title("Navigation")
        # Sidebar navigation

    #page = st.sidebar.radio("Navigation", ["About Me", "Experience", "Skills", "Projects", "Certificates", "Contact"])
    page = option_menu(
        menu_title="Navigation",
        options=["About Me", "Experience", "Skills", "Projects", "Certificates", "Contact"],
        icons=["person", "briefcase", "tools", "clipboard", "award", "envelope"],
        menu_icon="cast",
        default_index=0
    )

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
