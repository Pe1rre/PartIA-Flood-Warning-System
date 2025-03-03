# Copyright (C) 2025 Ethan J. Marshall (em2017@cam.ac.uk)
# Copyright (C) 2025 Peter J. Kelly (pk578@cam.ac.uk)
#
# SPDX-License-Identifier: MIT
"""Unit tests for the flood submodule"""

from floodsystem import stationdata, flood


def test_station_level_over_threshold():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    check = flood.stations_level_over_threshold(stations, 0.6)
    for i in range(1, len(check) - 1):
        assert check[i][1] <= check[i - 1][1], f"Element {i} and {i - 1} where in the wrong order!"
        assert check[i][0].relative_water_level() >= 0.6


def test_stations_highest_rel_level():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    check = flood.stations_highest_rel_level(stations, 10)
    for i in range(1, len(check) - 1):
        assert check[i][1] <= check[i - 1][1], f"Element {i} and {i - 1} where in the wrong order!"
