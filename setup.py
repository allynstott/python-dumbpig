"""A Python library for running the Dumbpig Snort Rule Checker"""
from distutils.core import setup

setup(
    name="python-dumbpig",
    version="0.0.2",
    description="Python library for Dumbpig",
    author="Ryan Hays, Allyn Stott",
    author_email="ryan@oculussec.com, allynstott@gmail.com",
    packages=["dumbpig"],
    package_dir={"dumbpig": "."},
    license="GNU General Public License (GPL) 3.0")
