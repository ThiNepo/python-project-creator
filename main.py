from ppc.python_project_creator import PythonProjectCreator
import toml
import os

project_model = {}
with open("project.toml") as file:
    project_model = toml.loads(file.read())
    print(project_model)

creator = PythonProjectCreator(project_model)
creator.create("basic", "projects/basic_project")
