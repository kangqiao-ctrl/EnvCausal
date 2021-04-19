# EnvCausal
A Causal Inference Framework for Environmental Data Analysis

This repository contains all the necessary data and custom Python scripts to reproduce the results in the paper "Machine Learning–Aided Causal Inference Framework for Environmental Data Analysis: A COVID-19 Case Study".

Jupyter Notebook examples will be uploaded in future releases.

## Install
`pip install EnvCausal`

## Script descriptions:
  _clustering.py_ -- A PCA-then-k-means clustering pipeline.</br>
  _causal_estimate.py_ -- A dowhy package wrapper, results will be written in a txt file<sup>1</sup>. </br>
  _recover_network.py_ -- A SAM model for Bayesian network recovery, adjacent matrix will be returned.  </br>
  _result_plot.py_ -- A couple of functions for result visualization.</br>

<sup>1</sup>Inspired by [Dowhy example: Iterating over multiple refutation tests](https://github.com/microsoft/dowhy/blob/master/docs/source/example_notebooks/dowhy_refuter_notebook.ipynb)</br>
