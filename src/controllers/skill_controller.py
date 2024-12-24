import json
from src.models.skill import Skill
from src.views.skill_view import SkillView

class SkillController:
    def __init__(self):
        self.skills = []

    def load_skills_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            for item in data.get("skills", []):
                skill = Skill(name=item["name"], level=item["level"])
                self.skills.append(skill)

    def display_skills(self):
        skill_details = [skill.get_skill_details() for skill in self.skills]
        SkillView.display_all_skills(skill_details)