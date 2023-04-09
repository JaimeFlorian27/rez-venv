import os
import shutil
import subprocess
from rez_venv import main
import pytest


@pytest.fixture(scope="module")
def venv_path():
    path = "test_venv"
    main.create_venv(path)
    yield path
    shutil.rmtree(path)


def test_venv_exists(venv_path):
    assert os.path.isdir(venv_path)
    assert os.path.isdir(os.path.join(venv_path, 'bin'))
    assert os.path.isfile(os.path.join(venv_path, 'bin', 'python'))


def test_venv_functional(venv_path):
    # subprocess.check_call([os.path.join(venv_path, 'bin', 'pip'), 'list'])
    subprocess.check_call([os.path.join(venv_path, 'bin', 'python'), '-c', 'import argparse'])


def test_venv_system_site_packages():
    path = "test_venv_sys_site_pkgs"
    main.create_venv(path, system_site_packages=True)

    try:
        subprocess.check_call([os.path.join(path, 'bin', 'python'), '-c', 'import pprint'])
    finally:
        shutil.rmtree(path)