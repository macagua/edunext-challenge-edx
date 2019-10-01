#!/usr/bin/env python
# pylint: disable=C0111,W6005,W6100

import os
import re
import sys

from setuptools import find_packages, setup


def get_version(*file_paths):
    """Extract the version string."""
    # Extract the version string from the file at the given relative path fragments.
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


PCKS = find_packages(exclude=['tests', 'tests.*']),
VERSION = get_version(str(PCKS[0][0]), '__init__.py')
DESCRIPTION = """An REST API that processor the client payments from Paypal."""

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
CHANGELOG = open(os.path.join(
    os.path.dirname(__file__), 'CHANGELOG.rst')).read()

# Get more https://pypi.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Intended Audience :: Developers',
    'License :: Other/Proprietary License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
],


setup(
    name=str(PCKS[0][0]),
    version=VERSION,
    description=DESCRIPTION,
    long_description=README + '\n\n' + CHANGELOG,
    author='Leonardo J. Caballero G.',
    author_email='leonardocaballero@gmail.com',
    url='https://bitbucket.org/macagua/edunext-challenge',
    packages=PCKS[0],
    include_package_data=True,
    install_requires=[
        "Django>=1.8,<1.11"
    ],
    zip_safe=False,
    keywords='Django edx',
    classifiers=CLASSIFIERS,
    license='Other/Proprietary License',
    platforms='OS Independent',
)
