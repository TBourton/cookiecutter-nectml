"""Script to launch a http web server for {{ cookiecutter.namespace_name }}."""
import os

import nectml_flaskutils
import yaml
from nectlog import logging2json
from nectlog.log import initialize_logging
from nectml_flaskutils.blue_print import health_basic
from nectml_flaskutils.tracer import initialize_tracer_jaeger

from ..core import __version__ as CORE_VERSION
from .api import setup, v1

logging_path = os.environ["LOGGING_CONF"]
logging2json.initialize_logging_config(logging_path)

with open(
    os.environ['{{ cookiecutter.namespace_name.upper() }}_CONF'], encoding='utf-8'
) as config_file:
    config = yaml.safe_load(config_file)

initialize_logging(**config.pop('logging', {}))

setup(config["{{ cookiecutter.namespace_name }}"])

nectml_flaskutils.flask_service.version = CORE_VERSION
nectml_flaskutils.flask_service.app.register_blueprint(v1, url_prefix='/')
nectml_flaskutils.flask_service.app.register_blueprint(
    health_basic.bp,
    url_prefix='/'
)
nectml_flaskutils.flask_service.add_generic_metrics(
    name='{{ cookiecutter.namespace_name }}',
    version=CORE_VERSION)
initialize_tracer_jaeger('{{ cookiecutter.namespace_name }}')

app = nectml_flaskutils.flask_service.app


if __name__ == "__main__":
    app.run()
