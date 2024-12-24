import requests
import streamlit as st
from PIL import Image
from io import BytesIO
from utils import get_direct_download_link

class PrjoectView:

    def display_old_project(project):
        st.subheader(f"{project['title']}")

        with st.container():
            st.markdown(f"""### {project['title']}""")
            col1, col2 = st.columns([2,1])
            with col1:
                st.markdown(project['description'])
        with col2:
            direct_link = get_direct_download_link(project['image_path'])
            response = requests.get(direct_link)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image)
            else:
                st.warning("Unable to load image from the provided URL.")

    def display_current_project(project):
        st.subheader(f"{project['title']}")
        st.info(f"{project['description']}")
    
    def display_all_projects(self, old_projects = [], current_projects = []):
        st.title("🚀 Projects")
        for project in old_projects:
            PrjoectView.display_old_project(project)

        st.header("🔨 Current Projects")
        for project in current_projects:
            PrjoectView.display_current_project(project)