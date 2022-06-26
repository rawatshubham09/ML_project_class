from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "housing-prediction"
VERSION = "0.0.2"
AUTHOR = "Shubham Rawat"
DESCRIPTION = "THis is First Live Project in Class"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function get the requirements.txt file
    and return all requirement libraries name, it will
    get install in system
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

