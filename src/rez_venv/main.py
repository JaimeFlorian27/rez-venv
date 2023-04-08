import argparse
import os
import sys
import venv
import shutil
import sysconfig

from rez.resolved_context import ResolvedContext


def pythonpath_from_context(packages):
    """Returns the pythonpath of a rez context"""
    context = ResolvedContext.get_current()
    if not context and packages:
        context = ResolvedContext(package_requests=packages)
    else:
        return ""
    environ = context.get_environ()
    return environ["PYTHONPATH"]


def symlinktree(source, destination, symlinks=False, ignore=None):
    """
    Create symbolic links of the source tree in the destination tree.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)
    files = os.listdir(source)
    if ignore:
        ignored_files = ignore(source, files)
    else:
        ignored_files = set()

    for name in files:
        if name in ignored_files:
            continue

        src_name = os.path.join(source, name)
        dst_name = os.path.join(destination, name)

        if symlinks and os.path.islink(src_name):
            linkto = os.readlink(src_name)
            os.symlink(linkto, dst_name)

        elif os.path.isdir(src_name):
            symlinktree(src_name, dst_name, symlinks, ignore)

        else:
            os.symlink(src_name, dst_name)


def create_venv(venv_path="", system_site_packages=True, packages=[]):
    """Create a new virtual environment."""
    venv_path = os.path.abspath(venv_path)
    builder = venv.EnvBuilder(system_site_packages=system_site_packages)
    builder.create(venv_path)

    site_packages_path = sysconfig.get_path("purelib", vars={"base": venv_path})
    pythonpath = pythonpath_from_context(packages).split(":")

    if not pythonpath:
        return

    for path in pythonpath:
        symlinktree(path, site_packages_path)


def parse_args(args):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Create a virtual environment")
    parser.add_argument(
        "--venv-path",
        type=str,
        nargs="?",
        default=".venv",
        help="Path to the virtual environment",
    )

    parser.add_argument(
        "--system-site-packages",
        type=bool,
        nargs="?",
        default=True,
        help="Give access to the system site-packages",
    )

    parser.add_argument(
        "packages",
        type=str,
        nargs="*",
        help="packages to use in the target environment",
    )

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    create_venv(args.venv_path, args.system_site_packages, args.packages)


if __name__ == "__main__":
    main()
