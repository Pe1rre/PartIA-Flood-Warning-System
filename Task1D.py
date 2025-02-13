# Copyright (C) 2025 Ethan J. Marshall (em2017@cam.ac.uk)
# Copyright (C) 2025 Peter J. Kelly (pk578@cam.ac.uk)
#
# SPDX-License-Identifier: MIT

from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river


def run():
    # Print the rivers with atleast one monitoring station, and print the first ten stations in alphabetical order

    # Build list of stations
    stations = build_station_list()
    rivers = stations_by_river(stations)

    print("Number of rivers:", len(rivers))

    rivers_array = rivers.items()
    rivers_array = sorted_by_key(rivers_array, 0)
    print("First 10:")
    for i in range(0, 10):
        print("\t", rivers_array[i][0])
    # Second demonstration
    # Print the names of station in for river aire, river cam and river thames in alphabetical order
    river_aire = rivers["River Aire"]
    river_cam = rivers["River Cam"]
    river_thames = rivers["River Thames"]
    # sort alphabetically by name
    river_aire.sort(key=lambda x: x.name)
    river_cam.sort(key=lambda x: x.name)
    river_thames.sort(key=lambda x: x.name)

    print(river_aire, river_cam, river_thames)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
