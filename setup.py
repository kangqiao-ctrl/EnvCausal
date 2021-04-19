from setuptools import setup, find_packages

setup(
    name='EnvCausal',
    packages=find_packages(),
    version='0.3.0',
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
