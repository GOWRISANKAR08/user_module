from setuptools import setup, find_packages

setup(
    name="django-user-module",  # PyPI compatible name
    version="0.1.0",  # Initial version (semantic versioning)
    packages=find_packages(),
    include_package_data=True,  # Required for Django templates/static files
    install_requires=[
        "Django>=5.0",  # Django 5.0+ has official Python 3.13 support
        # Add other dependencies if needed
    ],
    python_requires=">=3.13",  # Explicit Python version lock
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "Framework :: Django :: 5.0",
        "Operating System :: OS Independent",
    ],
)