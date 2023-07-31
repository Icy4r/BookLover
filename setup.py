from setuptools import setup, find_packages

setup(
    name='funniest',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Ian Yung',
    author_email='IYung419@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)