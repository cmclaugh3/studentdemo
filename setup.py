from setuptools import setup, find_packages

setup(
    name='studentdemo',
    version='0.1.0',
    url='https://github.com/cmclaugh3/studentdemo',
    author='Conor McLaughlin',
    description='Package containing Python Scripts for DS5100 in-class M09',
    packages=find_packages(),
    license='MIT',
    install_requires=['pandas >= 1.1.3']
)