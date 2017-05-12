from setuptools import setup

setup (
    name = "log",
    version = "0.0.1",
    packages = ["log"],
    entry_points = {
        'console_scripts': ['log=log.__main__:main']
    }
)

