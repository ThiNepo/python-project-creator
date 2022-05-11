import click
import os
import sys
import jinja2
import toml

from ppc.python_project_creator import PythonProjectCreator


@click.group()
def main():
    pass


@main.command()
@click.option("-t", "--template", help="Template to use.")
@click.option("-c", "--config", help="TOML file with config.")
@click.argument("output")
def create(template, config, output):
    """Create a python project based on a template.

    Currently the following templates are supported:

    * basic
    * cp
    * pip

    To create a project you can run `ppc create --template pip projects/new_project`.

    This will create a project in the folder `projects/new_project`.

    The default template is `basic`.
    """

    if template is None:
        template = "basic"

    click.echo(f"Creating project with template {template} at {output}")

    project_model = None
    if config:
        with open(config) as file:
            project_model = toml.loads(file.read())
            click.echo("Using config file...")

    try:
        creator = PythonProjectCreator(model=project_model, template=template)
        creator.create(output)
        click.echo("Project created :)")
    except jinja2.exceptions.UndefinedError as e:
        print(e)


if __name__ == "__main__":
    main()
