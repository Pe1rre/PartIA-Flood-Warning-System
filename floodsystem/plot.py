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
    high_low = station.typical_range

    # Plot
    plt.plot(dates, levels)
    # How do I work out the typical high and low ranges of a rivers water level?
    plt.plot(high_low[0])
    plt.plot(high_low[1])

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.station_id)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

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
