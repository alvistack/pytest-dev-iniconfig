# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='iniconfig',
    version='2.0.0',
    description='brain-dead simple config-ini parsing',
    author_email='Ronny Pfannschmidt <opensource@ronnypfannschmidt.de>, Holger Krekel <holger.krekel@gmail.com>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    packages=['iniconfig'],
    package_dir={'': 'src'},
)
