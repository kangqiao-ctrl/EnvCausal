from setuptools import setup, find_packages

setup(
    name='EnvCausal',
    packages=find_packages(),
    version='0.5.0',
    install_requires=[          
        'pandas',
        'numpy',
        'sklearn',
        'dowhy',
        'econml',
        'matplotlib',
        'seaborn',
        'cdt',
        'networkx',
        'torch'
    ]
)