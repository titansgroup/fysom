# coding: utf-8
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import re
import sys

here = os.path.abspath(os.path.dirname(__file__))

# find the first version number in CHANGES
with open(os.path.join(here, 'CHANGES')) as f:
    for line in f:
        version = line.strip()
        if re.search("^[0-9]+\.[0-9]+\.[0-9]+$", version):
            break
    else:
        raise RuntimeError('Could not determine a version from CHANGES file.')


class ToxCommand(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

setup(
    name='tg-fysom',
    version=version,
    url='https://github.com/titansgroup/fysom',
    author='Titans Group Engineering Team',
    author_email='l-engenharia@titansgroup.com.br',
    classifiers=[
        'Development Status :: 3 - Production/Stable',
        # Who the project is intended for.
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: Other/Proprietary License',
        # Supported Python versions.
        'Programming Language :: Python :: 2.7',
        # Supported OSes
        'Operating System :: OS Independent'
    ],
    packages=find_packages(exclude=['tests']),
    test_suite='nose.collector',
    tests_require=['tox'],
    cmdclass={
        'test': ToxCommand,
    }
)
