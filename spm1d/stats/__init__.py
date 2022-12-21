'''
Statistics module.

This module contains functions for conducting classical hypothesis testing on a set of 1D continua.

For all tests the dependent variable **Y** must be a NumPy array, with dimensions::

* J :  number of observations
* Q :  number of field nodes
* I :  number of vector components

Specifically:

* Univariate 0D tests:  **Y** should be ( J x 1 )
* Multivariate 0D tests:  **Y** should be ( J x I )
* Univariate 1D tests:  **Y** should be ( J x Q )
* Multivariate 1D tests:  **Y** should be ( J x Q x I )

'''

# Copyright (C) 2021  Todd Pataky
