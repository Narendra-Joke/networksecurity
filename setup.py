'''
The setup.py file is an essential part of packaging and
distributing Python Projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as it's metadata, dependencies, and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    this function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## read lines from the file
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found") 
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Narendra Joke",
    author_email="narendrajoke27@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

print(get_requirements())