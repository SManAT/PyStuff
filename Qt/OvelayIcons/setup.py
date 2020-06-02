"""
setup.py for life-exam
sudo pip3 install .
"""
__author__ = 'Stefan Hagmann'

if __name__ == '__main__':

    setup(
        author=__author__,
        maintainer=__author__,
        license="GPLv3",
        install_requires=[
            'opencv-python',
        ],
        python_requires='>=3.8',
    )
