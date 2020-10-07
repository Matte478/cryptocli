from setuptools import setup

setup(
    name='cryptocli',
    version='0.1.0',
    packages=['cryptocli'],
    entry_points={
        'console_scripts': [
            'cryptocli = cryptocli.__main__:main'
        ]
    })
