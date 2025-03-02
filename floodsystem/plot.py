# Copyright (C) 2025 Peter. J. Kelly
# Copyright (C) 2025 Ethan. J. Marshall
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
plotting water levels and other data graphically.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates

from . import analysis


def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels)
    plt.hlines(station.typical_range[0], dates[0], dates[-1], label='Typical Range - Low', linestyles='dashed',
               color='r')
    plt.hlines(station.typical_range[1], dates[0], dates[-1], label='Typical Range - High', linestyles='dashed',
               color='r')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name + " live water levels")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = analysis.polyfit(dates, levels, p)

    dateints = np.array(matplotlib.dates.date2num(dates))
    x = dateints - d0

    plt.plot(x, levels)
    plt.plot(x, poly(x))

    plt.title(station.name + " - water level prediction")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.show()
