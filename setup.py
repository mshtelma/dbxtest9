from setuptools import find_packages, setup
from dbxtest9 import __version__

setup(
    name='dbxtest9',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='Databricks Labs CICD Templates Sample Project',
    author=''
)
