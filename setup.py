__author__ = 'tusharmakkar08'

from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=False)
install_requirement = [str(ir.req) for ir in install_reqs]

setup(
    # Application name:
    name="facebook_image_search",

    # Version number:
    version="0.0.1",

    # Application author details:
    author="Tushar Makkar",
    author_email="tusharmakkar08@gmail.com",

    # Packages
    packages=find_packages(),

    package_data={'': ['*.md']},

    # Details
    url="http://tusharmakkar08.github.io/",

    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],

    # license="LICENSE.txt",
    description=open("README.md").read(),

    long_description=open("README.md").read(),

    entry_points={
        'console_scripts': [
            'yaml_validator = main:command_line_runner',
        ]
    },

    # Dependent packages (distributions)
    install_requires=install_requirement,

)
