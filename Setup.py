from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path):
    with open(path) as file:
        requirements = file.readlines()

        requirements = [requirement for requirement in requirements if requirement!=HYPEN_E_DOT]
        return requirements

setup(
    name = 'Automated Document summarizaion and Keyword Extraction',
    version= '0.0.1',
    author='K Prakash',
    author_email='prakashkofficials@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)