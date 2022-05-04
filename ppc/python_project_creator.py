from jinja2 import Template
import os
import toml
import copy 

from jinja2.exceptions import UndefinedError

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")


def render_template(path: str, **kwargs):
    with open(os.path.join(TEMPLATES_FOLDER, path)) as file_:
        template = Template(file_.read())

    return template.render(kwargs)

def dict_from_keys(dictionary, keys):
    for key in keys:
        dictionary = dictionary[key]
    return dictionary

class PythonProjectCreator:
    def __init__(self, model=None, template='basic'):
        self.model = model if model else {}
        self.template = template
        self.config = self.__get_template_config()
        self.__ask_config([])


    def get_project_templates(self):
        project_templates = os.listdir(TEMPLATES_FOLDER)
        return project_templates

    def __ask_config(self, _previous: list):
        previous = copy.deepcopy(_previous)
        if 'variables' in self.config:
            for key, value in dict_from_keys(self.config['variables'], previous).items():
                # TODO: Handle different types of variables
                if key not in dict_from_keys(self.model, previous):
                    if value in ["String"]:
                        dict_from_keys(self.model, previous)[key] = input(f"{'.'.join(previous + [key])}: ")
                    else:                        
                        dict_from_keys(self.model,previous)[key] = {}
                        self.__ask_config(previous + [key])

                

    def __get_template_config(self):
        project_config = {}
        if os.path.exists(os.path.join(TEMPLATES_FOLDER, self.template, "__ppc__.toml")):    
            with open(os.path.join(TEMPLATES_FOLDER, self.template, "__ppc__.toml")) as file:
                project_config = toml.loads(file.read())
        return project_config

    def __create(self, project_template, output_path):

        # Replace routes based on config
        if 'replace_on_routes' in self.config:

            for key, value in self.config['replace_on_routes'].items():
                if key in output_path:
                    output_path = output_path.replace(key, dict_from_keys(self.model, value.split('.')))
                    
        if not os.path.exists(output_path):
            os.makedirs(output_path)


        for file in os.listdir(os.path.join(TEMPLATES_FOLDER, project_template)):
            # ignore configuration file
            if file == '__ppc__.toml':
                continue

            if os.path.isdir(os.path.join(TEMPLATES_FOLDER, project_template, file)):
                self.__create(
                    os.path.join(project_template, file),
                    os.path.join(output_path, file),
                )
            else:
                template_path = os.path.join(project_template, file)
                output_file = os.path.join(output_path, file)                

                with open(output_file, "w") as f:
                    f.write(render_template(template_path, model=self.model))

    def create(self, output_path):
        self.__create(self.template, output_path)
