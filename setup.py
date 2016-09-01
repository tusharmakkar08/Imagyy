__author__ = 'tusharmakkar08'

from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=False)
install_requirement = [str(ir.req) for ir in install_reqs]

setup(
    # Application name:
    name="imagyy",

    # Version number:
    version="1.0.3",

    # Application author details:
    author="Tushar Makkar",
    author_email="tusharmakkar08@gmail.com",

    # Packages
    packages=['image_search', 'image_search.search_files'],

    package_data={'': ['*.md']},

    license='MIT',
    platforms=['any'],
    # Details
    url="https://github.com/tusharmakkar08/Imagyy/",

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # license="LICENSE.txt",
    description="Fetches public photos of different social networking platforms",

    long_description=open("README.rst").read(),

    entry_points={
        'console_scripts': [
            'imagyy = image_search.main_search:command_line_runner',
        ]
    },

    # Dependent packages (distributions)
    install_requires=install_requirement,

)
