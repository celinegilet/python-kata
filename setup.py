from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='app',
    version='1.0.0',
    description='Python environment for coding Kata',
    long_description=readme,
    author='Céline GILET',
    author_email='celinegilet@yahoo.fr',
    url='https://github.com/celinegilet/python-kata',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

