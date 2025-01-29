# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from .utils import sorted_by_key  # noqa


def stations_within_radius(stations, centre, r):
    """Returns a list of stations which have a radial distance of r km or lower from centre.
    Centre is in the form (x, y)."""
    found = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            found.append(station)
    return found
