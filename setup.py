# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in customization_qct/__init__.py
from customization_qct import __version__ as version

setup(
	name='customization_qct',
	version=version,
	description='customization_qct',
	author='suraj varade',
	author_email='varade.suraj787@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
