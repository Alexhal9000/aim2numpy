# setup.py
from setuptools import setup, find_packages

# Function to read the requirements.txt file
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='aim2numpy',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    author='Alejandro Gutierrez',
    author_email='alejandro.gutierrez@ucalgary.ca',
    description='A library to convert AIM image files to numpy arrays',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Alexhal9000/aim2numpy', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
