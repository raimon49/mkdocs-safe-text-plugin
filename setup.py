import os
from setuptools import setup, find_packages

from mkdocssafetext import (__version__ as VERSION, __author__ as AUTHOR,
                            __license__ as LICENSE)


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


LONG_DESC = ''
try:
    from pypandoc import convert

    about_this = convert('README.md', 'rst', format='markdown_github')
    separate = '\n\n'
    change_log = convert('CHANGELOG.md', 'rst', format='markdown_github')

    LONG_DESC = about_this  + separate + change_log
except (IOError, ImportError):
    LONG_DESC = read_file('README.md')


setup(
    name='mkdocs-safe-text-plugin',
    version=VERSION,
    description='Plugin for safe text editing with MKDocs.',
    long_description=LONG_DESC,
    author='raimon49',
    author_email='raimon49@hotmail.com',
    url='https://github.com/raimon49/mkdocs-safe-text-plugin',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Text Processing',
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
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest-cov',
        'pytest-pycodestyle',
        'pytest-pythonpath',
    ],
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_safe_text = mkdocssafetext.plugin:SafeTextPlugin',
        ]
    }
)
