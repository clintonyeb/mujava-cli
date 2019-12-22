from setuptools import setup, find_packages

with open('requirements.txt') as reqs_file:
    requirements = reqs_file.read().splitlines()

setup(
    name="mujava",
    version='0.1',
    description="Python Git Library",
    author="Sebastian Thiel, Michael Trier",
    author_email="byronimo@gmail.com, mtrier@gmail.com",
    url="https://github.com/gitpython-developers/GitPython",
    packages=find_packages('.'),
    py_modules=[],
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        mujava=src.app:cli
    ''',
)