#!/usr/bin/env python

"""
This is a setup script for survivalPredictor

@version: 0.1
@author: Aziz Khan
@email: aziz.khan@ncmm.uio.no
"""
import os
from distutils.core import setup
from setuptools import find_packages

VERSION = '0.1'

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
]

install_requires = [
    'scipy',
    'numpy',
    'scikit-learn',
    'pandas',
    'argparse'
]

setup(
    name="survivalPredictor",
    description="survivalPredictor for NORBIS Mini-challenge",
    version=VERSION,
    author="Aziz Khan",
    #Keywords= "bioinformatics,genomics",
    author_email="aziz.khan@ncmm.uio.no",
    url="https://github.com/asntech/survivalPredictor",
    package_dir={'survivalPredictor': 'survivalPredictor'},
    packages=['survivalPredictor'],
    scripts=['survivalPredictor/survivalPredictor',
                   ],
    package_data={'survivalPredictor': ['survivalPredictor/data/*.txt']},
    include_package_data=True,
    install_requires = install_requires,
    classifiers=CLASSIFIERS,
)
