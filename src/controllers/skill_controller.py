import json
from src.models.skill import SkillCategory, Technology
from src.views.skill_view import SkillView
import streamlit as st
class SkillController:
    def __init__(self):
        self.skills = []
    @st.cache_data
    def load_skills_from_file(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    def process_skills(self, data):
        self.skills = []
        for key in data.keys():
            skill_category_obj = SkillCategory(key)
            for value in data.get(key, []):
                skill_category_obj.add(Technology(value))
            self.skills.append(skill_category_obj)

    def load_and_process_skills(self, file_path):
        data = self.load_skills_from_file(file_path)
        self.process_skills(data)

    def display_skills(self):
        skills_to_display = [skill.get_name() for skill in self.skills]
        SkillView.display_skills(skills_to_display)
