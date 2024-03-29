"""API functionality for {{ cookiecutter.repo_name }}."""
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = "0.0.0"
