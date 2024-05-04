from setuptools import setup

setup(
    name='sit727-utilities',
    version='0.1.0',    
    description='A package for common utilities in sit727 project',
    url='https://github.com/AnhNguyen20695/sit727-project-common.git',
    author='Felix Nguyen',
    author_email='s222521972@deakin.edu.au',
    packages=['pyexample'],
    install_requires=['mysql-connector-python==8.3.0',
                      'pandas==2.2.2',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',   
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.11',
    ],
)