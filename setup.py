## begin license ##
#
# Seecr initVM will initialize java VM, based on pylucene-py3
#
# Copyright (C) 2021 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Seecr initVM"
#
# "Seecr initVM" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Seecr initVM" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Seecr initVM".  If not, see <http://www.gnu.org/licenses/>.
#
## end license ##

from setuptools import setup

setup(
    name='seecr_initvm',
    version='$Version: 1.0.x$'[9:-1].strip(),
    packages=['seecr_initvm'],
    description='Seecr initVM will initialize java VM, based on pylucene-py3',
    long_description='Seecr initVM will initialize java VM, based on pylucene-py3',
    author='Seecr (Seek You Too B.V.)',
    author_email='info@seecr.nl',
    url='https://seecr.nl',
    license='GPLv3',
    platforms='all',
    classifiers=[
        #https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
)
