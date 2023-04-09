import os
from rez.resolved_context import ResolvedContext


def pythonpath_from_context(packages):
    """Returns the pythonpath of a Rez context"""
    context = ResolvedContext.get_current()
    if not context:
        if packages:
            context = ResolvedContext(package_requests=packages)
        else:
            return []
    environ = context.get_environ()
    return environ["PYTHONPATH"].split(os.pathsep)


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
