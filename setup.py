import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from mkdocssafetext import (__version__ as VERSION, __author__ as AUTHOR,
                            __license__ as LICENSE)


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = '--pep8 -v --cov mkdocssafetext'

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='mkdocs-safe-text-plugin',
    version=VERSION,
    description='TBD.',
    long_description=read_file('README.md'),
    author='raimon49',
    author_email='raimon49@hotmail.com',
    url='https://github.com/raimon49/mkdocs-safe-text-plugin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    keywords=['mkdocs', 'bleach', 'xss'],
    license=LICENSE,
    install_requires=[
        'bleach',
        'bleach-whitelist',
        'mkdocs>=0.17.0',
    ],
    tests_require=[
        'pytest-cov',
        'pytest-pycodestyle',
        'pytest-pythonpath',
    ],
    cmdclass={
        'test': PyTest,
    },
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_safe_text = mkdocssafetext.plugin:SafeTextPlugin',
        ]
    }
)
