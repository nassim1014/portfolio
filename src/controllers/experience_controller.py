# controllers/experience_controller.py
import json
from src.models.experience import ExperienceFactory
from src.views.experience_view import ExperienceView

class ExperienceController:
    def __init__(self ):
        self.experiences = []
        self.view = ExperienceView()

    def load_experiences(self, data):
            for item in data:
                experience = ExperienceFactory.create_experience(
                    experience_type=item["experience_type"],
                    title=item["title"], 
                    company=item["company"],
                    date=item["date"],
                    location=item["location"],
                    details=item["details"]
                )
                self.experiences.append(experience)
    def load_experiences_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            self.load_experiences(data)
            
    def display_experiences(self):
        experience_details = [exp.get_experience_details() for exp in self.experiences]
        self.view.display_all_experiences(experience_details)
