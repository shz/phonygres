#!/usr/bin/env python

import os
import sys
import subprocess
from distutils.cmd import Command
from distutils.core import setup

class TestCommand(Command):
    '''
    Runs unit tests, via pytest.
    '''
    user_options = []

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
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        commands = (
            # [sys.executable, '-m', 'pylint'],
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
    cmdclass={
        'lint': LintCommand,
        'test': TestCommand,
    },
)
