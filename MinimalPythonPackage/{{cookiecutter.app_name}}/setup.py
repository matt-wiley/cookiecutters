#
# Package structure sourced from:
#   https://waylonwalker.com/minimal-python-package/
# 
from setuptools import setup
import yaml

with open('package_data.yml','r') as package_data_file:
    package_data = yaml.load(package_data_file, yaml.SafeLoader)

setup(
    name="{{cookiecutter.app_name}}",
    version=f"{package_data.get('version')}",
    py_modules=["{{cookiecutter.app_name}}"],
    install_requires=[""],
)