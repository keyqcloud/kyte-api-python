from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Python module for interfacing Kyte API'

with open("README.md") as file:
    long_description = file.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="kyte", 
        version=VERSION,
        author="Kenneth P. Hough",
        author_email="<kenneth@keyqcloud.com>",
        description=DESCRIPTION,
        long_description=long_description,
        packages=find_packages(include=['mypythonlib']),
        install_requires=['requests'],
        url="https://github.com/keyqcloud/kyte-api-python",
        license="MIT",
        keywords=['python', 'kyte', 'kyte api'],
        classifiers= [
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Software Development :: Libraries :: Tools",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)