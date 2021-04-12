from setuptools import setup, find_packages
import yaml



with open('app_data.yml','r') as app_data_file:
    app_data = yaml.load(app_data_file,yaml.SafeLoader)

setup(
    name='{{cookiecutter.app_name}}',
    version=f"{app_data.get('version')}",
    url='',
    author='',
    author_email='',
    description='',
    packages=find_packages(),    
    install_requires=[],
)
