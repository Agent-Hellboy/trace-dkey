import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="trace-dkey",
    author="Prince Roshan",
    version='0.0.2',
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/Agent-Hellboy/trace-dkey",
    description=("Python library to trace path of a particular key inside a nested dict"),
    long_description=read("README.rst"),
    license="MIT",
    package_dir={'': 'src'},
    packages=['trace_dkey'],
    keywords=[
        "tracer","dict-key-path-finder"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
