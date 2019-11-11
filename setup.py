from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup( 
    name = "Ximg_converter",
    version = "0.0.1",
    description = 'A library for convert Rigaku img file to csv or png file',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url="https://github.com/kytk-03/Ximg_converter",
    author="Kiyotaka Mukasa",
    author_email="kytk.khhut.328@gmail.com",
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6, <4',
    install_requires=['fabio', 'numpy', 'Pillow'],


)

