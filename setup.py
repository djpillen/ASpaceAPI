from setuptools import setup, find_packages

setup(
    name="ASpaceAPI",
    packages=find_packages(),
    install_requires=[
        "requests",
        "lxml"
    ]
)
