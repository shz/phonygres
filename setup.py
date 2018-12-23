#!/usr/bin/env python

import sys
import subprocess
from typing import List, Any
from setuptools import Command, setup

class TestCommand(Command):
    '''
    Runs unit tests, via pytest.
    '''
    user_options: List[Any] = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise SystemExit(subprocess.call([sys.executable, '-m', 'pytest']))

class LintCommand(Command):
    '''
    Runs linting.
    '''
    user_options: List[Any] = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        commands = (
            [sys.executable, '-m', 'pylint', 'phonygres', 'setup.py'],
            [sys.executable, '-m', 'mypy', 'phonygres'],
        )
        for cmd in commands:
            code = subprocess.call(cmd)
            if code != 0:
                raise SystemExit(code)
        raise SystemExit(0)

setup(
    name='Phonygres',
    version='1.0',
    description='Python implementation of Postgres',
    author='Patrick Stein',
    author_email='lylepstein@gmail.com',
    url='https://github.com/shz/phonygres',
    packages=['phonygres'],
    install_requires=[
        'sqlparse==0.2.4'
    ],
    cmdclass={
        'lint': LintCommand,
        'test': TestCommand,
    },
)
