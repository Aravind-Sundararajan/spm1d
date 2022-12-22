"""
Statistics modulespm1d.stats

This module contains functions for conducting classical hypothesis testing on a set of 1D continuaspm1d.stats

For all tests the dependent variable **Y** must be a NumPy array, with dimensions::

* J :  number of observations
* Q :  number of field nodes
* I :  number of vector components

Specifically:

* Univariate 0D tests:  **Y** should be ( J x 1 )
* Multivariate 0D tests:  **Y** should be ( J x I )
* Univariate 1D tests:  **Y** should be ( J x Q )
* Multivariate 1D tests:  **Y** should be ( J x Q x I )

"""

# Copyright (C) 2021  Todd Pataky


from spm1d.stats import _spm

from spm1d.stats.t import ttest, ttest_paired, ttest2, regress, glm
from spm1d.stats.ci import ci_onesample, ci_pairedsample, ci_twosample

from spm1d.stats.anova import anova1, anova1rm
from spm1d.stats.anova import anova2, anova2nested, anova2rm, anova2onerm
from spm1d.stats.anova import (
    anova3,
    anova3nested,
    anova3rm,
    anova3tworm,
    anova3onerm,
)

from spm1d.stats.hotellings import hotellings, hotellings_paired, hotellings2
from spm1d.stats.cca import cca
from spm1d.stats.manova import manova1
from spm1d.stats.var import eqvartest

from spm1d.stats import nonparam
from spm1d.stats import normality
