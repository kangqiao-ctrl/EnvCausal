from setuptools import setup, find_packages

with open('README.md',encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='EnvCausal',
    packages=find_packages(),
    version='0.3.4',
    description = "A Causal Inference Framework for Environmental Data Analysis",
    long_description = long_description,
    long_description_content_type='text/markdown', 
    author = 'kangqiao-ctrl',
    author_email = "qiaok@mun.ca",
    url = "https://github.com/kangqiao-ctrl/EnvCausal",
    license='MIT',
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