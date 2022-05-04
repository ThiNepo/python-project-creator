from ppc.python_project_creator import PythonProjectCreator
import toml
import os

project_model = None
with open("project.toml") as file:
    project_model = toml.loads(file.read())
    print(project_model)

creator = PythonProjectCreator(project_model, "pip")
creator.create("projects/pip_project")
