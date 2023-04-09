import sys
import argparse
from core import create_venv


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
        "--deep-copy",
        type=bool,
        nargs="?",
        default=False,
        help="create copies of the packages instead of symlinks",
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
