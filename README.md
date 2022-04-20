# Python Project Creator

This project generates Python code to start a new project.

In the current state it support well the following templates:

- [x] **basic**: A basic project with a main.py file
- [x] **cp**: Contains the files used to solve competitive programming problems.

It does not support templates that need models such as:

- [ ] **pip**: A template to create a package that will be uploaded to PIP.

In the future I expect to create templates that need more sofisticated code generation, such as:

- [ ] **flask**: A template to be used when starting a Flask project.

# Build and Upload

python setup.py sdist
python setup.py bdist_wheel

twine upload dist/\*
