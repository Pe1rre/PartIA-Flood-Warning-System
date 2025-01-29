# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


from haversine import haversine, Unit
from station import MonitoringStation
def stations_by_distance(stations, p):
    list_of_tuples = []
    for station in stations:
        distance_from_p = haversine(p, station.coord)
        #making the tuple#
        z = ( station.station_id, distance_from_p)
        list_of_tuples.append(z)
    list_of_tuples = sorted_by_key(list_of_tuples)
    return list_of_tuples