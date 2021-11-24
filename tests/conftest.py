"""Configure the tests."""
import shutil
from pathlib import Path

import pytest
from cookiecutter import main

CC_ROOT = Path(__file__).parents[1].resolve()

args = {
    'repo_name': 'nect-cc',
    'namespace_name': 'nectml_package',
}


@pytest.fixture(scope='module', params=[{}, args])
def default_baked_repo(tmpdir_factory, request):
    """Create a default project."""
    temp = tmpdir_factory.mktemp('data-project')
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CC_ROOT),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir
    )

    repo_name = pytest.param.get('repo_name', 'repo-name')

    proj = out_dir / repo_name
    # request.cls.path = proj
    yield proj

    # cleanup after
    shutil.rmtree(out_dir)
