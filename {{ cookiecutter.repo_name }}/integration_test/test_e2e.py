"""Run end-to-end tests for {{ cookiecutter.namespace_name }}."""
# pylint: disable=redefined-outer-name
# TODO: Write e2e tests.
import requests


def test_health(svc_address):
    """Test a health call."""
    res = requests.get(f"{svc_address}/v1/health")
    assert res.status_code == 200
