#!/usr/bin/python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

readme = open("README.rst").read()

setup(
	name = "deansi",
	version = "1.2",
	description = "ANSI codes to HTML converter",
	author = "David García Garzón",
	author_email = "voki@canvoki.net",
	url = 'https://github.com/GuifiBaix/python-deansi',
	long_description_content_type='text/markdown',
	long_description = readme,
	license = 'GNU General Public License v3 or later (GPLv3+)',
	packages=find_packages(exclude=['*[tT]est*']),
	py_modules=[
		'deansi',
	],
	entry_points={
		'console_scripts': [
			'deansi=deansi:main',
		]
	},

	scripts=[
		'deansi.py',
	],
	include_package_data = True,
	test_suite = 'deansi_test',
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: System :: Logging',
		'Topic :: Text Processing :: Filters',
		'Topic :: Text Processing :: Markup :: HTML',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Operating System :: OS Independent',
	],
)

