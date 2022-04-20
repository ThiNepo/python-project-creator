from ppc import PythonProjectCreator
import toml
import os

project_model = {}
with open("project.toml") as file:
    project_model = toml.loads(file.read())
    print(project_model)

creator = PythonProjectCreator(project_model)
creator.create("pip", "projects/pip_project")
