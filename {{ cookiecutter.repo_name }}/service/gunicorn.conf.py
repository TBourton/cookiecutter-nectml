"""The gunicorn config."""
# pylint: disable=invalid-name
import sys

from structlog import get_logger

logger = get_logger(__name__)

bind = "0.0.0.0:{{ cookiecutter.gunicorn_port }}"

proc_name = "{{ cookiecutter.namespace_name.upper() }}"

workers = 1
threads = 20

timeout = 0
graceful_timeout = 0


def child_exit(_, __):
    """Exit the main process when a worker exits."""
    logger.error("Quitting gunicorn because worker exited.")
    sys.exit(4)
