from jinja2 import Template
import os

TEMPLATES_FOLDER = os.path.join("ppc", "templates")


def render_template(path: str, **kwargs):
    with open(os.path.join(TEMPLATES_FOLDER, path)) as file_:
        template = Template(file_.read())

    return template.render(kwargs)


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
                template_path = os.path.join(project_template, file)
                output_file = os.path.join(output_path, file)
                with open(output_file, "w") as f:
                    f.write(render_template(template_path, model=self.model))

    def create(self, project_template, output_path):
        self._create(project_template, output_path)
