"""Configure end-to-end test env."""
import os

import pytest

DEFAULT_CLIENT_TIMEOUT = 60


@pytest.fixture(scope="module")
def svc_address():
    """Get the SVC_ADDRESS."""
    output = os.environ.get("SVC_ADDRESS")
    if output is None:
        raise ValueError("SVC_ADDRESS enviroment variable is not set")
    return output


@pytest.fixture(scope="module")
def timeout():
    """Get the TIMEOUT."""
    return os.environ.get("CLIENT_TIMEOUT", DEFAULT_CLIENT_TIMEOUT)
