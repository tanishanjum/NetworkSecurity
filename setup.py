'''
The setup.py file is an essential part of packaging and
distributing a Python project. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project,such as its metadata,dependencies,and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            #read the lines from file
            lines= file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement != '-e.':

                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst


setup(
    name='NetworkSecurityProject',
    version='0.0.1',
    author='Tanish Anjum M.S',
    author_email='tanishanjum04@gmail.com',
    description='A project for network security',
    packages=find_packages(),
    install_requires=get_requirements()
)
print(get_requirements())