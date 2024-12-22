from abc import ABC , abstractmethod
import streamlit as st

class Project(ABC):
    @abstractmethod
    def return_project(self):
        pass
class Current_Project(Project):
    def __init__(self, title : str, description : str):
        self.title = title
        self.description = description
    def return_project(self):
        st.subheader(f"{self.title}")
        st.info(f"{self.description}")

class Old_Project(Project):
    def __init__(self, title : str, description : str , image_path : str):
        self.title = title
        self.description = description
        self.image_path = image_path
    def return_project(self):
        st.subheader(f"{self.title}")

        with st.container():
            st.markdown(f"""### {self.title}""")
            col1, col2 = st.columns([2,1])
            with col1:
                st.markdown(self.description)
        with col2:
            st.image(self.image_path) #, caption="Medical App Interface")

class ProjectFactory:
    @staticmethod
    def create_project(project_type, **kwargs):
        if project_type == "old":
            return Old_Project(kwargs["title"], kwargs["description"], kwargs["image_path"])
        if project_type == "current":
            return Current_Project(kwargs["title"], kwargs["description"])
        else:
            raise ValueError("Invalid project type. Please choose 'Old' or 'Current'.")