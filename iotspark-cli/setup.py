"""
IotSpark tool
-------------

The tool that helps to manage the infrastructure

"""
from setuptools import setup

setup(
    name="iotspark",
    version="0.1",
    license="MIT",
    author="Yury Kovalev",
    author_email="qualiapps@gmail.com",
    description="Management tool",
    long_description=__doc__,
    packages=["iotspark", "iotspark.commands", "iotspark.utils"],
    zip_safe=False,
    include_package_data=True,
    platforms="linux",
    tests_require=[
        "nose",
    ],
    test_suite='nose.collector',
    keywords=['iot', 'microservices', 'infrastructure'],
    entry_points={
        'console_scripts': ['iotspark=iotspark.cli:main']
    }
)
