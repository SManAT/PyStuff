"""
Usage: sudo pip3 install .
"""
__author__ = 'Mag. Stefan Hagmann'

from distutils.core import setup

if __name__ == '__main__':

    setup(
        name="RandomCodingTasks",
        description="Create random Task Numbers for Students, and remember them",
        author=__author__,
        maintainer=__author__,
        license="GPLv3",
        install_requires=[
            'pyyaml',
            'click',
            'pandas',
        ],
        python_requires='>=3.8',
    )
