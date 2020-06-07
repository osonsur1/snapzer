from setuptools import setup

setup(
    name='snapzer',
    version='0.1',
    author='osonsur1',
    author_email="osonsur1@binghamton.edu",
    description='Manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['snappy'],
    url='https://github.com/osonsur1/snapzer',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snappy=snappy.snappy:cli
    ''',

)