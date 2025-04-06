from setuptools import setup, find_packages

setup(
    name="scripts",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # No external dependencies required
    ],
    entry_points={
        "console_scripts": [
            "scripts=scripts.cli:main",
        ],
    },
    author="John Doe",
    author_email="john.doe@email.com",
    description="A simple command-line task manager built with Python and SQLite.",
)