import setuptools
import shutil

from setuptools.command.sdist import sdist
from wheel.bdist_wheel import bdist_wheel

with open("README.md", "r") as fh:
    long_description = fh.read()

def clean_folders():
    print("Removing temporary folders.")

    TMP_FOLDERS = ["test_package.egg-info", "build"]
    for folder in TMP_FOLDERS:
        shutil.rmtree(folder)


class SdistCommand(sdist):
    """Custom build command."""

    def run(self):
        sdist.run(self)


class BdistWheelCommand(bdist_wheel):
    """Custom build command."""

    def run(self):
        bdist_wheel.run(self)
        clean_folders()


setuptools.setup(
    name="test_package",
    version="0.0.1",
    author="Thiago Nepomuceno",
    author_email="test@gmail.com",
    description="Short description of the project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    # url="https://github.com/username/test_package",
    packages=setuptools.find_packages(),   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["toml"],
    cmdclass={"sdist": SdistCommand, "bdist_wheel": BdistWheelCommand},
)