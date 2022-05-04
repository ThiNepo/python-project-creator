import click
import os
import sys
import jinja2

from ppc.python_project_creator import PythonProjectCreator


@click.group()
def main():
    pass


@main.command()
@click.option("-t", "--template", help="Template to use.")
@click.argument("output")
def create(template, output):
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

    try:
        creator = PythonProjectCreator(model=None, template=template)
        creator.create(output)
        click.echo("Project created :)")
    except jinja2.exceptions.UndefinedError as e:
        print(e)


if __name__ == "__main__":
    main()
