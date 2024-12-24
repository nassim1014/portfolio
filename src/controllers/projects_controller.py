import json
from src.models.project import ProjectFactory
from src.views.project_view import PrjoectView


class ProjectController:
    def __init__(self):
        self.old_projects = []
        self.current_projects = []
        self.view = PrjoectView()

    def get_project_item(item , type):
        if type == "old":
            return ProjectFactory.create_project(
                project_type= type,
                title=item["title"],
                description=item["description"],
                image_path=item["image_path"]
            )
        if type == "current":
            return ProjectFactory.create_project(
                        project_type= type,
                        title=item["title"],
                        description=item["description"],
                    )
        raise ValueError("Invalid project type. Please choose 'Old' or 'Current'.")

    # filepath: /C:/Users/heeln/OneDrive/Documents/portfolio/src/controllers/projects_controller.py
    def load_projects_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            self.load_projects(data)
    def load_projects(self, data):
            # Load old projects
            for item in data.get("old_projects", []):
                project = ProjectController.get_project_item(item , type = "old")
                self.old_projects.append(project)
            
            # Load current projects
            for item in data.get("current_projects", []):
                project = ProjectController.get_project_item(item,  type = "current")
                self.current_projects.append(project)
    
    def display_projects(self):
        old_project_details = [project.get_project_details() for project in self.old_projects]
        new_project_details = [project.get_project_details() for project in self.current_projects]
        self.view.display_all_projects(old_project_details, new_project_details)