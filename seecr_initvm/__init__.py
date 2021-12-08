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

def initvm(*modules):
    "Init all available VMs"

    import lucene
    import importlib

    cp = [lucene.CLASSPATH]

    mods = []
    for m in modules:
        if isinstance(m, list):
            mods.extend(m)
        else:
            mods.append(m)

    for module in mods:
        cp.append(importlib.import_module(module).CLASSPATH)

    lucene.initVM(classpath=":".join(cp))
