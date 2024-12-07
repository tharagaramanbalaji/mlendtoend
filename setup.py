from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def read_requirements(file_path: str) -> List[str]:
    # This function will return the list of requirements
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Tharak",
    author_email="tharagaraman2004@gmail.com",
    packages=find_packages(),  
    install_requires=read_requirements('requirements.txt')
)
