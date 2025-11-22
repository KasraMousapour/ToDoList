from app.services.projects import Project
from app.services.tasks import Task


class ProjectManager:
    def __init__(self):
        self.projects = []

    def find_project(self, name):
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def add_project(self, name):
        if self.find_project(name):
            print("Project already exists.")
        else:
            self.projects.append(Project(name))
            print(f"Project '{name}' added.")

    def rename_project(self, old_name, new_name):
        project = self.find_project(old_name)
        if project:
            try:
                project.name = new_name
                print(f"Project renamed to '{new_name}'.")
            except ValueError as e:
                print(e)    
        else:
            print("Project not found.")

    def change_description(self, name, new_description):
        project = self.find_project(name)
        if project:
            try:
                project.description = new_description
                print(f"Project description changed.")
            except ValueError as e:
                print(e)    
        else:
            print("Project not found.")
        
    def add_task_to_project(self, project_name, task:Task):
        project = self.find_project(project_name)
        if project:
            project.add_task(task)
            print(f"Task added to '{project_name}'.")
        else:
            print("Project not found.")

    def show_projects(self):
        if not self.projects:
            print("No projects yet.")
        for project in self.projects:
            print(project)
            print("-" * 30)  

    def delete_project(self, name):
        project = self.find_project(name)
        if project:
            self.projects.remove(project)
            project.delete_project()

        else:
            print("project doesn't exist.")    
