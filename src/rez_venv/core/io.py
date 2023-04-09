import os
from rez.resolved_context import ResolvedContext
from ..utils import log


def pythonpath_from_context(packages):
    """Returns the pythonpath of a Rez context"""

    log.info("Attempting to use current Rez context...")
    context = ResolvedContext.get_current()

    if not context:
        if packages:
            log.info(
                "No current Rez context found, resolving context with\
                requested Rez packages..."
            )
            context = ResolvedContext(package_requests=packages)
        else:
            log.warning(
                "No current Rez context found and no rez packages were requested, nothing will be installed to the venv"
            )
            return []

    environ = context.get_environ()
    pythonpath = environ.get("PYTHONPATH")

    if pythonpath:
        log.info("successfully found PYTHONPATH in Rez context!")
        return pythonpath.split(os.pathsep)
    log.warning(
        "PYTHONPATH has not been set in the Rez context, no packages will be installed to the venv"
    )
    return []


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

        # os.symlink(src_name, dst_name)

        elif os.path.isdir(src_name):
            symlinktree(src_name, dst_name, symlinks, ignore)

        else:
            os.symlink(src_name, dst_name)
