#!/usr/bin/env python

import re
import ast
from os import path
from setuptools import setup

PACKAGE_NAME = "antlr_ast"
HERE = path.abspath(path.dirname(__file__))
VERSION_FILE = path.join(HERE, PACKAGE_NAME, "version.py")

if __name__ == "__main__":
    setup(use_scm_version={"write_to": VERSION_FILE, "write_to_template": '__version__ = "0.8.1"\n'})