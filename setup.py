from setuptools import setup, find_packages

setup(
    name="user_module",
    version="1.0.0",
    description="Reusable Django app for user management.",
    author="Your Name",
    author_email="your@email.com",
    url="https://github.com/your-org/user_module",
    packages=find_packages(),  # auto detects packages
    include_package_data=True,
    install_requires=[
        "Django>=3.2"
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
