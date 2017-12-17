from setuptools import setup, find_packages

ver = "9.9.9"
with open("README.md", mode='r') as f:
    long_description = f.read()

with open("Makefile", mode='r') as f:
    ver = f.read().split('\n')[0].split('=')[1][1:]

setup(
   name='dat_struct_py',
   version=ver,
   url='https://github.com/rachit-ranjan16/dat_struct_py',
   description='Basic Data Structures and Operations Implemented in Python',
   long_description=long_description,
   licence='GNU',
   author='rachit-ranjan16',
   author_email='rachit.ranjan93@gmail.com',
   classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Topic :: Data Structures :: Basic Data Structures and Operations',
        'License :: OSI Approved :: GNU License',
        'Programming Language :: Python :: 3.5',
        ],
   keywords='data structures operations',
   packages=[],  # same as name
   install_requires=[],
   python_requires='~=3.5'
)
