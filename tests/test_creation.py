"""Test creation."""
# pylint: disable=no-member
import glob
import os
from subprocess import check_output

import pytest

EXPECTED_PKGS = ['result', 'core', 'client', 'dev', 'service']


def dir_contents(dirname):
    """Recurse directory for all files."""
    contents = []
    for root, dirs, files in os.walk(dirname):
        contents += [os.path.join(root, file_) for file_ in files]
        for dir_ in dirs:
            contents += dir_contents(os.path.join(root, dir_))

    return contents


@pytest.mark.usefixtures("default_baked_repo")
def test_repo_name(default_baked_repo):
    """Test repo name."""
    repo = default_baked_repo
    if pytest.param.get('repo_name'):
        assert repo.name == 'nect-cc'
    else:
        assert repo.name == 'repo-name'


@pytest.mark.usefixtures("default_baked_repo")
def test_namespace_name(default_baked_repo):
    """Test namespace name."""
    repo = default_baked_repo
    ns_name = pytest.param.get('namespace_name', 'repo_name')
    for pkg in EXPECTED_PKGS:
        pkg_path = repo / pkg / ns_name / pkg
        assert pkg_path.exists()


@pytest.mark.usefixtures("default_baked_repo")
def test_setup(default_baked_repo):
    """Test setups."""
    repo = default_baked_repo
    for pkg in EXPECTED_PKGS:
        wd = os.getcwd()
        try:
            os.chdir(str(repo / pkg))
            args = ['python3', 'setup.py', '--version']
            assert check_output(args).decode('ascii').strip() == "0.0.0"
        except Exception:
            assert False
        finally:
            os.chdir(wd)


@pytest.mark.usefixtures("default_baked_repo")
def test_no_curlies(default_baked_repo):
    """Check curly braces appear in a file.

    That is, was Jinja able to render everything?

    """
    repo = default_baked_repo
    ignored_files = ['.drone.yml']
    template_strings = ['{{', '}}', '{%', '%}']
    files = dir_contents(repo)
    files = [x for x in files if not any(v in x for v in ignored_files)]

    for file_ in files:
        with open(file_) as file_:
            data = file_.read()
            assert not any(s in data for s in template_strings)


def test_drone(default_baked_repo):
    """Test only one drone."""
    repo = default_baked_repo
    contents = dir_contents(repo)
    drones = [x for x in contents if '.drone' in x]
    assert len(drones) == 1
    assert (repo / ".drone.yml").exists()
