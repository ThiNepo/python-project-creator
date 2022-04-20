import click
import os
import sys
import jinja2

# TODO: Investigate a better way to handle this pathing problem.

ORIGINAL_CWD = os.getcwd()

parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

os.chdir(parentPath)

from ppc import PythonProjectCreator


@click.group()
def main():
    pass


@main.command()
@click.option("-t", "--template", help="Template to use.")
@click.argument("output")
def create(template, output):
    """Create a python project based on a template."""

    if template is None:
        template = "basic"

    click.echo(f"Creating project with template {template} at {output}")

    try:
        creator = PythonProjectCreator()
        creator.create(template, os.path.join(ORIGINAL_CWD, output))
        click.echo("Project created :)")
    except jinja2.exceptions.UndefinedError as e:
        print(e)


if __name__ == "__main__":
    main()
