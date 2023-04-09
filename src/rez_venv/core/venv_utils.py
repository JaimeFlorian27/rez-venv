import os
import sysconfig
import venv
import shutil
from .io import pythonpath_from_context, symlinktree


def create_venv(venv_path=".venv",
                system_site_packages=True,
                deep_copy=False,
                packages=[]):
    """Create a new virtual environment."""
    venv_path = os.path.abspath(venv_path)
    builder = venv.EnvBuilder(system_site_packages=system_site_packages)
    builder.create(venv_path)

    site_packages_path = sysconfig.get_path("purelib", vars={"base": venv_path})
    pythonpath = pythonpath_from_context(packages)

    if not pythonpath:
        return

    if deep_copy:
        for path in pythonpath:
            shutil.copytree(pythonpath, site_packages_path, dirs_exist_ok=True)
    else:
        for path in pythonpath:
            symlinktree(path, site_packages_path)
