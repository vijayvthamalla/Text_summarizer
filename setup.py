import logging
from typing import List

from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .' #To trigger setup.py automatically

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d %(message)s]')

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.1"
REPO_NAME = "Project_Name"
author = "Vijay Thamalla"
author_email = "vijayvthamalla@gmail.com"
short_description = "Project_Description"
github_url = "https://github.com/vijayvthamalla/Effectiveness_of_ML_Algorithms"

def get_requirements(filepath:str)->List[str]:
    '''
    This function will get required packages from requirements.txt
    '''
    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements= [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

logging.info(f"Starting setup for {REPO_NAME}")
logging.info(f"Version: {version}")
logging.info(f"Author: {author}")
logging.info(f"Author Email: {author_email}")
logging.info(f"Short Description: {short_description}")
logging.info(f"Getting Requirements: {get_requirements('requirements.txt')}")
setup(
    name=REPO_NAME,
    version=version,
    author=author,
    author_email=author_email,
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=github_url,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))

logging.info(f"Finished setup for {REPO_NAME}")