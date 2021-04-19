from setuptools import setup, find_packages

setup(
    name='EnvCausal',
    packages=find_packages(),
    version='0.3.0',
    description = "A Causal Inference Framework for Environmental Data Analysis",
    author = "kangqiao-ctrl",
    author_email = "qiaok@mun.ca",
    url = "https://github.com/kangqiao-ctrl/EnvCausal",
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
