import argparse
import os
import sys
import venv


def create_venv(venv_path="", system_site_packages=True):
    """Create a new virtual environment."""
    venv_path = os.path.abspath(venv_path)
    builder = venv.EnvBuilder(system_site_packages=system_site_packages)
    builder.create(venv_path)


def parse_args(args):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Create a virtual environment")
    parser.add_argument(
        "venv_path",
        type=str,
        nargs='?',
        default="venv",
        help="Path to the virtual environment",
    )

    parser.add_argument(
        "--system-site-packages",
        type=bool,
        nargs='?',
        default=True,
        help="Give access to the system site-packages",
    )
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    create_venv(args.venv_path, args.system_site_packages)


if __name__ == "__main__":
    main()
