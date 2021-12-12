#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="hello_app",
    version="1.0.0",
    description="Hello world app with CPU load generator",
    author="Tris Emmy Wilson",
    author_email="tris@tris.fyi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
