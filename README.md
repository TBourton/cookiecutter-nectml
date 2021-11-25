# Cookiecutter Data Science

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

    repo_name: Name for the repository, e.g. 'cat-detector'
    namespace_name: Name for the python packages. e.g. 'cat_detector'. This will create packages cat_detector.result, cat_detector.core, etc.
    description_name: Title for setup.py descriptions. e.g. Cat Detector.
    author_initials: Initials of the author, e.g. 'tb'.
    author_email: mailing address, e.g. 'tb@madeup.com',
    description: Short description of the project.
    python_requires_version: e.g. '3.8' will populate the setups with "python_requires>=3.8"
    docker_image: base docker image to use, e.g. 'python:3.8.11-slim-buster'
    gunicorn_port: Port to use for gunicorn, e.g. 9999


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests


### Acknowledgments
------------
This project was originally forked from [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).
