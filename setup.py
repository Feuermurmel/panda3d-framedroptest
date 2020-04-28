import setuptools


setuptools.setup(
    name='framedroptest',
    entry_points=dict(console_scripts=['framedroptest = framedroptest:main']),
    install_requires=['Panda3D'],
    packages=setuptools.find_packages())
