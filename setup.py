
from setuptools import setup, find_packages

setup(
    name='pyidd',
    version='0.1',
    packages=find_packages(exclude=['tests*', 'examples*']),
    license='MIT',
    description='Identify the Distribution of Data',
    long_description=open('Description.txt').read(),
    install_requires=['numpy', 'pandas', 'scipy', 'matplotlib'],
    url='https://github.com/MasoudKaviani/pyidd',
    author='Masoud Kaviani',
    author_email='kaviani.masoud@gmail.com'
)
