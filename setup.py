from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='cryptocli',
    version='0.1.0',
    author='dave.',
    author_email='hello@davedot.dev',
    description='A simple commandline app for encrypt / decrypt files in Python 3.',
    long_description=long_description,
    url='https://github.com/Matte478/cryptocli',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pycryptodome >= 3.9.8'
    ],
    python_requires='>=3.8',
    packages=['cryptocli', 'cryptocli.helpers'],
    entry_points={
        'console_scripts': [
            'cryptocli = cryptocli.__main__:main'
        ]
    }
)
