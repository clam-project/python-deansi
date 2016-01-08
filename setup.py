#!/usr/bin/python
from setuptools import setup, find_packages

readme = open("README.rst").read()

setup(
	name = "deansi",
	version = "0.1",
	description = "ANSI codes to HTML converter",
	author = "David Garcia Garzon",
	author_email = "voki@canvoki.net",
	url = 'https://github.com/GuifiBaix/python-deansi',
	long_description = readme,
	license = 'GNU General Public License v3 or later (GPLv3+)',
	packages=find_packages(exclude=['*[tT]est*']),
	py_modules=[
		'deansi',
		],
	scripts=[
		'deansi.py',
		],
	include_package_data = True,
	test_suite = 'deansi_test',
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: OS Independent',
	],
)

