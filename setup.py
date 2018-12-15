import sys

from setuptools import setup, find_packages

requires = ["click"]
tests_requires = ["pytest", "pytest-cache", "pytest-cov"]
lint_requires = ["flake8", "black"]
dev_requires = ["bumpversion"] + requires + tests_requires + lint_requires


setup(
    name="gypsy",
    version="0.1",
    description="Project and Code Analysis tool to find things out about your code",
    long_description="\n\n".join([open("README.rst").read()]),
    license="MIT",
    author="David G. Daniel",
    author_email="davydany@aeroxis.com",
    url="https://gypsy.readthedocs.org",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "gypsy = gypsy.cli:gypsy"
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    extras_require={"test": tests_requires, "dev": dev_requires, "lint": lint_requires},
)
