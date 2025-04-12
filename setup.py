from setuptools import setup, find_packages

setup(
    name='user_module',
    version='1.0.0',
    packages=find_packages(),  # This finds user_module/
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
)
