import json
from src.models.skill import SkillCategory, Technology
from src.views.skill_view import SkillView

class SkillController:
    def __init__(self):
        self.skills = []

    def load_skills_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            self.load_skills(data)

    def load_skills(self, data):
            for key in data.keys():
                skill_category_obj = SkillCategory(key)
                for value in data.get(key, []):
                    skill_category_obj.add(Technology(value))
                self.skills.append(skill_category_obj)

    def display_skills(self):
        skills_to_display = [skill.get_name() for skill in self.skills]
        SkillView.display_skills(skills_to_display)
# Test the SkillController
if __name__ == "__main__":
    skill_controller = SkillController()
    skill_controller.load_skills_from_file("data/skills.json")
    skills = skill_controller.display_skills()
    for skill in skills:
        print(skill)