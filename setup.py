import os
from setuptools import setup
from setuptools import find_packages


long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='ndspeed',
    version='0.1',
    author='karlind',
    author_email='karlind@users.noreply.github.com',
    description='A python package to display network and disk speed',
    long_description=long_description,
    url='https://github.com/karlind/ndspeed',
    license='GPL2.0',
    packages=find_packages(),
    install_requires = [
        'psutil',
        'terminaltables',
    ],
    entry_points = {
        'console_scripts': ['ndspeed=ndspeed.main:main'],
    }
)