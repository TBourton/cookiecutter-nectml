"""Setup for the {{ cookiecutter.namespace_name }}.dev package."""

import os
from setuptools import find_namespace_packages, setup

version = os.environ.get("{{ cookiecutter.namespace_name.upper() }}_VERSION", "0.0.0")

setup(
    name="{{ cookiecutter.namespace_name }}.dev",
    version=version,
    description="{{ cookiecutter.description_name }} dev functionality",
    packages=find_namespace_packages(
        include=["{{ cookiecutter.namespace_name }}.*"]
    ),
    namespace_packages=["{{ cookiecutter.namespace_name }}"],
    install_requires=[
        # TODO: dev/setup.py install_requires
    ]
)
