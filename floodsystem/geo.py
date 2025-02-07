# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa


from haversine import haversine, Unit
from .station import MonitoringStation


def stations_by_distance(stations, p):
    list_of_tuples = []
    for station in stations:
        distance_from_p = haversine(p, station.coord)
        #making the tuple#
        z = ( station.station_id, distance_from_p)
        list_of_tuples.append(z)
    list_of_tuples = sorted_by_key(list_of_tuples, 1)
    return list_of_tuples

def rivers_with_station(stations):
    #Get a list of all the rivers that have a station and then use a set to see only get the unique rivers and then that gives us all the rivers that have stations#
    list_of_rivers = []
    for station in stations:
        river = station.river
        list_of_rivers.append(river)
    #making a set#
    list_of_rivers = set(list_of_rivers)
    return list_of_rivers

def stations_by_river(stations):
    #produces a dictionary that tells you all the stations on a river, might need to iterate and do each component individually#
    stations_on_river = {}
    rivers = rivers_with_station(stations)
    for river in rivers:
        #for each river, attach which stations are on it#
        for station in stations:
            if river == station.river:
                list_of_stations = ()
                list_of_stations.append(station) 
        stations_on_river.update({river:list_of_stations})
    return stations_on_river