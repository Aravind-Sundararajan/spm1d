"""
Non-parametric hypothesis tests for 1D data (Statistical non-Parametric Mapping)
"""

# Copyright (C) 2016  Todd Pataky

__all__ = ["stats"]


from spm1d.stats.nonparam import metrics, permuters, calculators, stats, _snpm

from spm1d.stats.nonparam.stats import (
    anova1,
    anova1rm,
    anova2,
    anova2nested,
    anova2onerm,
    anova2rm,
    anova3,
    anova3nested,
    anova3onerm,
    anova3tworm,
    anova3rm,
)
from spm1d.stats.nonparam.stats import regress, ttest, ttest_paired, ttest2
from spm1d.stats.nonparam.stats import (
    cca,
    hotellings,
    hotellings_paired,
    hotellings2,
    manova1,
)
from spm1d.stats.nonparam.ci import ci_onesample, ci_pairedsample, ci_twosample
