import streamlit as st
from abc import ABC, abstractmethod

class Experience(ABC):
    @abstractmethod
    def return_experience(self):
        pass

class InternshipExperience(Experience):
    def __init__(self, title : str, company : str, date : str, location : str, details : str):
        self.title = title
        self.company = company
        self.date = date
        self.location = location
        self.details = details

    def return_experience(self):
        st.subheader(f"{self.title} | {self.company}")
        st.caption(f"{self.date} | {self.location}")
        with st.expander("View Details"):
            st.markdown(self.details)

class ExperienceFactory:
    @staticmethod
    def create_experience(experience_type, **kwargs):
        if experience_type == "internship":
            return InternshipExperience(kwargs["title"], kwargs["company"], kwargs["date"], kwargs["location"], kwargs["details"])
        else:
            raise ValueError("Invalid experience type. Please choose 'Internship'.")