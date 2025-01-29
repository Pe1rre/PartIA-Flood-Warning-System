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


def stations_by_distance(stations, p):
    list_of_tuples = []
    for station in stations:
        distance_from_p = haversine(p, station.coord)
        # making the tuple
        z = (station.station_id, distance_from_p)
        list_of_tuples.append(z)
    list_of_tuples = sorted_by_key(list_of_tuples, 1)
    return list_of_tuples
