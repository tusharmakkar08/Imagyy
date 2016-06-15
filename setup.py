__author__ = 'tusharmakkar08'

from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=False)
install_requirement = [str(ir.req) for ir in install_reqs]

setup(
    # Application name:
    name="facebook_image_search",

    # Version number:
    version="0.0.3",

    # Application author details:
    author="Tushar Makkar",
    author_email="tusharmakkar08@gmail.com",

    # Packages
    py_modules=['fb_search'],

    package_data={'': ['*.md']},

    license='MIT',
    platforms=['any'],
    # Details
    url="http://tusharmakkar08.github.io/Facebook_Graph_Search_Images/",

    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],

    # license="LICENSE.txt",
    description="Fetches public photos of any facebook id/username",

    long_description=open("README.md").read(),

    entry_points={
        'console_scripts': [
            'fb-search = fb_search:command_line_runner',
        ]
    },

    # Dependent packages (distributions)
    install_requires=install_requirement,

)
