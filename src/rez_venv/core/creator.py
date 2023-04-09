import os
import shutil
import sys
import sysconfig
import venv

from ..utils import log
from .io import pythonpath_from_context, symlinktree


def create_venv(
    venv_path=".venv", system_site_packages=True, deep_copy=False, packages=[]
):
    """Create a new virtual environment."""

    log.info(f'Creating venv in "{venv_path}"')

    venv_path = os.path.abspath(venv_path)
    builder = venv.EnvBuilder(system_site_packages=system_site_packages)
    builder.create(venv_path)
    log.info(
        f"venv created successfully at {venv_path} using Python {sys.version}"
    )

    destination_path = sysconfig.get_path("purelib", vars={"base": venv_path})
    pythonpath = pythonpath_from_context(packages)

    if not pythonpath:
        return

    if deep_copy:
        log.info("Copying all packages found in PYTHONPATH to venv...")
        for path in pythonpath:
            shutil.copytree(path, destination_path, dirs_exist_ok=True)
        log.info("Sucessfully copied all packages found in PYTHONPATH to venv")
    else:
        log.info("Symlinking all packages found in PYTHONPATH to venv...")
        for path in pythonpath:
            symlinktree(path, destination_path)
        log.info(
            "Sucessfully symlinked all packages found in PYTHONPATH to venv"
        )