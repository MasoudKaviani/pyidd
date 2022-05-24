
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='pyidd',
    version='0.3.1',
    packages=find_packages(exclude=['tests*', 'examples*']),
    license='MIT',
    description='Identify the Distribution of Data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['numpy', 'pandas', 'scipy', 'matplotlib'],
    url='https://github.com/MasoudKaviani/pyidd',
    author='Masoud Kaviani',
    author_email='kaviani.masoud@gmail.com'
)
