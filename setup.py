"""Setup configuration for System 7 TUI"""

from setuptools import setup, find_packages

setup(
    name="system7-tui",
    version="0.1.0",
    description="A faithful recreation of Apple's System 7 in the terminal",
    author="Stormzady",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "textual>=0.38.0",
        "rich>=13.7.0",
    ],
    entry_points={
        "console_scripts": [
            "system7=main:main",
        ],
    },
)