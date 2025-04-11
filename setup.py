
from setuptools import setup, find_packages

setup(
    name='user_module',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django>=3.2', 'djangorestframework'],
)
