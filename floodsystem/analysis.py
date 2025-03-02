# Copyright (C) 2025 Ethan. J. Marshall
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
the analysis of existing station data.

"""

import numpy as np
from matplotlib.dates import date2num


def polyfit(dates, levels, p):
    # Convert all dates to a numerical form
    numdates = np.array(date2num(dates))
    # Subtract the value of the first element from all
    # to avoid unnecessarily large values.
    shift = numdates[0]
    numdates -= shift

    pfit = np.polyfit(numdates, levels, p)
    poly = np.poly1d(pfit)

    return (poly, shift)
