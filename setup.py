from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "CLI Utility for creating virtual environments based on a Rez context"

setup(
    name="rez-venv",
    version=VERSION,
    author="Jaime Florian Urueta",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["rez-venv=rez_venv.main:main"]},
)
