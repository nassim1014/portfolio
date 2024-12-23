# models/experience.py
from abc import ABC, abstractmethod

class Experience(ABC):
    @abstractmethod
    def get_experience_details(self):
        pass

class InternshipExperience(Experience):
    def __init__(self, title, company, date, location, details):
        self.title = title
        self.company = company
        self.date = date
        self.location = location
        self.details = details

    def get_experience_details(self):
        return {
            "title": self.title,
            "company": self.company,
            "date": self.date,
            "location": self.location,
            "details": self.details
        }
class ExperienceFactory:
    @staticmethod
    def create_experience(experience_type, **kwargs):
        if experience_type == "internship":
            return InternshipExperience(kwargs["title"], kwargs["company"], kwargs["date"], kwargs["location"], kwargs["details"])
        else:
            raise ValueError("Invalid experience type. Please choose 'Internship'.")