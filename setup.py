from setuptools import setup, find_packages

with open('requirements.txt') as reqs_file:
    requirements = reqs_file.read().splitlines()

setup(
    name="mujava",
    version='0.1',
    description="MuJava Command Line Program",
    author="Clinton Yeboah",
    author_email="clintonyeb@gmail.com",
    url="https://github.com/clintonyeb/mujava-cli",
    packages=find_packages('.'),
    py_modules=[],
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        mujava=src.app:cli
    ''',
)