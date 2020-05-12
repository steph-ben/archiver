from setuptools import setup, find_packages


setup(
    name="archiver",
    version="0.0.1",
    author="Stephane Benchimol",
    author_email="stephane.benchimol@mfi.fr",
    packages=find_packages(include=['archiver', 'archiver.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.8',
)
