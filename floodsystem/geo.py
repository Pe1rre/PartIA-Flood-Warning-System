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
    """Returns a list of stations which have been sorted by their radial
    distance from the given datum p, which is a tuple in the format (lat,
    long)."""
    list_of_tuples = []
    for station in stations:
        distance_from_p = haversine(p, station.coord)
        # making the tuple
        z = (station.station_id, distance_from_p)
        list_of_tuples.append(z)
    list_of_tuples = sorted_by_key(list_of_tuples, 1)
    return list_of_tuples


def rivers_with_station(stations):
    """Get a list of all the rivers that have a station and then use a set to see only get the unique rivers.
    This gives us all the rivers that have stations."""
    list_of_rivers = []
    for station in stations:
        river = station.river
        list_of_rivers.append(river)
    # making a set
    list_of_rivers = set(list_of_rivers)
    return list_of_rivers


def stations_by_river(stations):
    """produces a dictionary that tells you all the stations on a river
    might need to iterate and do each component individually"""
    stations_on_river = {}
    for station in stations:
        if station.river not in stations_on_river:
            stations_on_river[station.river] = []
        stations_on_river[station.river].append(station)

    return stations_on_river


def rivers_by_station_number(stations, N):
    """Returns a list of N stations with the highest number of stations.
    N must be an integer gt 0.
    Stations are returned in the format (river name, number of stations)."""
    if N <= 0:
        raise ValueError("N must be an integer greater than zero")

    # Extract rivers from objects, mapping river name to
    # number of stations and sorting by the latter.
    rivercounts = {}
    for station in stations:
        if station.river not in rivercounts:
            rivercounts[station.river] = 0
        rivercounts[station.river] += 1
    rivers = list(rivercounts.items())
    rivers.sort(key=lambda x: x[1], reverse=True)

    # Move through the list of rivers, extracting the
    # number of stations needed to have N *different counts*
    # by checking the number of times this count changes.
    i = 1
    changecount = 0
    while changecount < N and i < len(rivers):
        if rivers[i][1] != rivers[i - 1][1]:
            changecount += 1
        i += 1

    return rivers[:i - 1]
