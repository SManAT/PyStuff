"""
setup.py
Usage: sudo pip3 install .
"""
__author__ = 'Mag. Stefan Hagmann'

from distutils.core import setup

if __name__ == '__main__':

    setup(
        name="CodeHighlighter",
        description="Convert Source Code to Html",
        author=__author__,
        maintainer=__author__,
        license="GPLv3",
        install_requires=[
            'PyYAML',
            'click',
            'Pygments',
            'cx_Freeze',
            'PyQt6',
            'PySide6',
        ],
        python_requires='>=3.8',
    )
