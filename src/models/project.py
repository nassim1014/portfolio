from abc import ABC , abstractmethod

class Project(ABC):
    @abstractmethod
    def get_project_details(self):
        pass

class Current_Project(Project):
    def __init__(self, title : str, description : str):
        self.title = title
        self.description = description
    def get_project_details(self):
        return {
            "title": self.title,
            "description": self.description
        }

class Old_Project(Project):
    def __init__(self, title : str, description : str , image_path : str):
        self.title = title
        self.description = description
        self.image_path = image_path
    def get_project_details(self):
        return {
            "title": self.title,
            "description": self.description,
            "image_path": self.image_path
        }

class ProjectFactory:
    @staticmethod
    def create_project(project_type, **kwargs):
        if project_type == "old":
            return Old_Project(kwargs["title"], kwargs["description"], kwargs["image_path"])
        if project_type == "current":
            return Current_Project(kwargs["title"], kwargs["description"])
        else:
            raise ValueError("Invalid project type. Please choose 'Old' or 'Current'.")