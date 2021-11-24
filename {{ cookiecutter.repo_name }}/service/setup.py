"""Setup for the {{ cookiecutter.namespace_name }}.service package."""

import os
from setuptools import find_namespace_packages, setup

version = os.environ.get(
    "{{ cookiecutter.namespace_name.upper() }}_VERSION",
    "0.0.0"
)

setup(
    name="{{ cookiecutter.namespace_name }}.service",
    version=version,
    description="{{ cookiecutter.description_name }} service functionality",
    packages=find_namespace_packages(
        include=["{{ cookiecutter.namespace_name }}.*"]
    ),
    namespace_packages=["{{ cookiecutter.namespace_name }}"],
    python_requires=">={{ cookiecutter.python_requires_version }}",
    install_requires=[
        "structlog",
        "nectlog",
        f"{{ cookiecutter.namespace_name }}.result>={version}"
        if version != "0.0.0" else "{{ cookiecutter.namespace_name }}.result",
        f"{{ cookiecutter.namespace_name }}.core>={version}"
        if version != "0.0.0" else "{{ cookiecutter.namespace_name }}.core"

    ]
)
