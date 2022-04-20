from jinja2 import Environment, PackageLoader, select_autoescape
import os

env = Environment(loader=PackageLoader("ppc"), autoescape=select_autoescape())

TEMPLATES_FOLDER = "ppc\\templates"


class PythonProjectCreator:
    def __init__(self, model=None):
        self.model = model

    def get_project_templates(self):
        project_templates = os.listdir(TEMPLATES_FOLDER)
        return project_templates

    def _create(self, project_template, output_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for file in os.listdir(os.path.join(TEMPLATES_FOLDER, project_template)):
            if os.path.isdir(os.path.join(TEMPLATES_FOLDER, project_template, file)):
                self._create(
                    os.path.join(project_template, file),
                    os.path.join(output_path, file),
                )
            else:
                template_path = str(os.path.join(project_template, file)).replace(
                    "\\", "/"
                )
                template = env.get_template(template_path)
                output_file = os.path.join(output_path, file)
                with open(output_file, "w") as f:
                    f.write(template.render(model=self.model))

    def create(self, project_template, output_path):
        self._create(project_template, output_path)
