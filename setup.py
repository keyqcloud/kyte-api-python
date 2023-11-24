from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Python module for interfacing KytePHP'
LONG_DESCRIPTION = 'Python module for interacting with a KytePHP API'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="kyte", 
        version=VERSION,
        author="Kenneth P. Hough",
        author_email="<kenneth@keyqcloud.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['datetime','requests','hmac'],
        url="https://github.com/keyqcloud/kyte-api-python",
        license="MIT",
        keywords=['python', 'kyte', 'kyte api'],
        classifiers= [
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
        ]
)