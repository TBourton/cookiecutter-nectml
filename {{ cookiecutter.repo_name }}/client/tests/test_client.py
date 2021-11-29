"""Tests for {{ cookiecutter.namespace_name }}.client.client."""
# pylint: disable=redefined-outer-name
import time

import pytest

from .mock_server import MockServer


@pytest.fixture(scope="session")
def worker_number(worker_id):
    """Get the current worker number."""
    id_as_str = "".join(ch for ch in worker_id if ch.isdigit())
    if len(id_as_str) == 0:
        return 0
    return int(id_as_str)


@pytest.fixture
def mockserver(request, worker_number):
    """Get a mockserver."""
    port = int(worker_number) + 9871
    server = MockServer(port=port)
    server.start()
    time.sleep(0.1)

    def fin():
        server.shutdown_server()
        time.sleep(0.1)

    # Use the request.addfinalizer as yield requests are not stackable
    request.addfinalizer(fin)
    return server
