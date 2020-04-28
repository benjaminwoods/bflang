"""
BFLang/bfmachine.

Requires Python >= 3.7.
"""

import sys

from setuptools import setup

if sys.version_info < (3, 7):
    raise NotImplementedError('devtools requires Python >= 3.7.')

setup(
    name="BFLang/bfmachine",
    version="dev",

    package_dir={'':'src'},
    packages=['bfmachine'],
    install_requires=[],

    # Metadata
    author="Benjamin Woods",
    author_email="ben@bjqw.me",
    description="Simple BF class-based compiler.",
    keywords="esoteric language",
    url="https://github.com/benjaminwoods/bflang",
    project_urls={},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ]
)
