# Cookiecutter NectML

_Nect CVML template service layout._


### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

```bash
$ pip install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/TBourton/cookiecutter-nectml

That will prompt you to enter the following:

    repo_name: Name for the repository, e.g. 'nect-cc'
    namespace_name: Name for the python packages. e.g. 'nect_cc'. This will create packages nect_cc.result, nect_cc.core, etc.
    description_name: Title for setup.py descriptions. e.g. Nect CC.
    author_initials: Initials of the author, e.g. 'tb'.
    author_email: mailing address, e.g. 'tb@madeup.com',
    description: Short description of the project.
    python_requires_version: e.g. '3.8' will populate the setups with "python_requires>=3.8"
    docker_image: base docker image to use, e.g. 'python:3.8.11-slim-buster'
    gunicorn_port: Port to use for gunicorn, e.g. 9999


### The Resulting Directory Structure
------------------------

The directory structure of the new project (run with the above inputs) looks like this: 
```
nect-cc
├── CHANGES.txt
├── charts
│   └── nect-cc
│       ├── Chart.yaml
│       ├── templates
│       │   └── TODO.yaml
│       └── values.yaml
├── client
│   ├── nect_cc
│   │   └── client
│   │       ├── client.py
│   │       ├── __init__.py
│   │       └── node.py
│   ├── requirements.txt
│   ├── setup.py
│   └── tox.ini
├── core
│   ├── nect_cc
│   │   └── core
│   │       ├── core.py
│   │       └── __init__.py
│   ├── requirements.txt
│   ├── setup.py
│   └── tox.ini
├── dev
│   ├── nect_cc
│   │   └── dev
│   │       └── __init__.py
│   ├── requirements.txt
│   └── setup.py
├── integration_test
│   ├── conftest.py
│   ├── README.md
│   └── test_e2e.py
├── Makefile
├── README.md
├── requirements-dev.txt
├── result
│   ├── nect_cc
│   │   └── result
│   │       ├── __init__.py
│   │       └── result.py
│   ├── requirements.txt
│   ├── setup.py
│   └── tox.ini
├── service
│   ├── Dockerfile
│   ├── gunicorn.conf.py
│   ├── logging.yaml
│   ├── nect_cc
│   │   └── service
│   │       ├── api.py
│   │       ├── app.py
│   │       ├── __init__.py
│   │       └── jlgeh.py
│   ├── nect_cc.yaml
│   ├── requirements.txt
│   ├── setup.py
│   ├── tests
│   │   └── pytest.ini
│   └── tox.ini
└── values
    ├── dev.yaml
    ├── e2e.yaml
    ├── int.yaml
    ├── prod.yaml
    ├── secrets
    │   └── TODO.yaml.crypt
    └── test.yaml
```

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests


### Acknowledgments
------------
This project was originally forked from [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).
