from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup( 
    name = "xrayimg",
    version = "0.0.2",
    description = 'A library for convert Rigaku img file to csv or png file',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url="https://github.com/kytk-03/xrayimg",
    author="Kiyotaka Mukasa",
    author_email="kytk.khhut.328@gmail.com",
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.7, <4',
    install_requires=['numpy >= 1.17.4', 'Pillow >= 6.2.1', 'fabio'],
)

