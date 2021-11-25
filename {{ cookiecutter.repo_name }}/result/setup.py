"""Setup for the {{ cookiecutter.namespace_name }}.result package."""

import os
from setuptools import find_namespace_packages, setup

version = os.environ.get("{{ cookiecutter.namespace_name.upper() }}_VERSION", "0.0.0")

setup(
    name="{{ cookiecutter.namespace_name }}.result",
    version=version,
    description="{{ cookiecutter.description_name }} result functionality",
    packages=find_namespace_packages(
        include=["{{ cookiecutter.namespace_name }}.*"]
    ),
    namespace_packages=["{{ cookiecutter.namespace_name }}"],
    python_requires=">={{ cookiecutter.python_requires_version }}",
    install_requires=[
        # TODO: result/setup.py install_requires
    ]
)
