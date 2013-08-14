#!/usr/bin/env python

#############################################################################
#    surrealism.py - Surreal sentence generator
#    Copyright (C) 2013  Ian Havelock
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

# This is a derivative work (used with permission) from www.ravenblack.net
# Credit also goes to Kevan Davis on whose work the surrealism generator at
# Ravenblack.net is based on.

#############################################################################

from setuptools import setup

long_desc = open('readme.rst').read()

setup(name = 'surrealism',
      version = '0.3',
      py_modules = ['surrealism'],
      author = 'Morrolan',
      author_email = 'morrolan@icloud.com',
      url = 'https://github.com/Morrolan/surrealism',
      license = 'GNU General Public License (GPL)',
      description = 'Surreal sentence and error message generator.',
      long_description = long_desc,
      platforms = ['Windows','Unix','OS X'],
      download_url = "https://pypi.python.org/pypi/surrealism/",
      keywords = ["surreal", "surrealism", "error message"],
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
         ],
      install_requires=['setuptools'],
      
      )