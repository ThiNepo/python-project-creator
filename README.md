![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-project-creator) ![PyPI](https://img.shields.io/pypi/v/python-project-creator)

![Discord](https://img.shields.io/discord/479923444017004556?label=discord) ![PyPI - Downloads](https://img.shields.io/pypi/dm/python-project-creator) ![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCMb90JgsFJpZyZzdmWCaCTg?style=social)

![Logo](https://github.com/ThiNepo/python-project-creator/raw/main/images/logo.svg)

This tool generates help you start a new Python project by generating its starting code. In the current stage it only generates very simple project, but more is planned to be added in the future (_including a Flask project with features selection_).

To install this tool run:

```
pip install python-project-creator
```

After installing you will have access to the `ppc` tool on your terminal. To know more about the tool and its commands run:

```
ppc --help
```

You can use the command `create` to create a new project. It follows the syntax:

```
ppc create --template <template> <output>
```

Where:

- **template**: The template to use for the project. If no template is informed the **basic** template will be used (check more below).
- **output**: The output directory where the project will be created.

Currently it support the folloging templates:

### Basic

This is a very simple template to use when starting a new project. It only creates a blank `main.py` file.

To use this template run:

```
ppc create --template basic <output>
```

### CP

This template can be used when solving programming exercises in Online Judges (OJs) using the Python language. Some examples of OJs are [Neps Academy](https://neps.academy/), [Codeforces](https://codeforces.com/), [Kattis](https://open.kattis.com/) and [Beecrowd](https://www.beecrowd.com.br/judge/en/login).

This template will create the following structure:

- main.py
- input.txt
- output.txt

Where `main.py` can be used to solve the problem. The input and output files are used to test the solution.

To use this template run:

```
ppc create --template cp <output>
```

### PIP

This template creates the structure that is needed when creating a package that will be uploaded to [PiPy](https://pypi.org/).

It will create:

- **module folder**: where you will write your module's code.
- **main.py**: to showcase a concrete example using your module.
- **setup.py**: contains the configuration of your project and creates the **wheel** needed when uploading your module to [PiPy](https://pypi.org/).
- **README.md**: where you will describe what is and how to use your module.

To use this template run:

```
ppc create --template pip <output>
```

This template will ask for some additional information during the creating. The information you provide will be filled in some parts of your project's files.

# Build and Upload

To build new this project run:

```
python setup.py sdist
python setup.py bdist_wheel
```

To upload a new version use (don't forget to update the version number in `setup.py`):

```
twine upload dist/*
```
