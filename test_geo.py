# Copyright (C) 2025 Ethan J. Marshall (em2017@cam.ac.uk)
# Copyright (C) 2025 Peter J. Kelly (pk578@cam.ac.uk)
#
# SPDX-License-Identifier: MIT
"""Unit tests for the geo package."""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius, stations_by_distance, rivers_with_station, stations_by_river


# Dummy stations using geographical data from Google Maps.
# All stations have coordinates which point to a landmark.
# A station has river set to "1" if it should be found to be within the testing
# radius.
dummy_stations = [
    MonitoringStation("tower-bridge", "", "", (51.505455, -0.075356), "", "1", "London"),
    MonitoringStation("tower-of-london", "", "", (51.508274, -0.076272), "", "1", "London"),
    MonitoringStation("niagara-falls", "", "", (43.082817, -79.074165), "", "", "Niagara Falls"),
    MonitoringStation("tokyo-international-centre", "", "", (35.676788, 139.763535), "", "", "Tokyo"),
]
dummy_stations_for_river_testing = [
    MonitoringStation("tower-bridge", "", "", (51.505455, -0.075356), "", "River Thames", "London"),
    MonitoringStation("tower-of-london", "", "", (51.508274, -0.076272), "", "River Thames", "London"),
    MonitoringStation("niagara-falls", "", "", (43.082817, -79.074165), "", "Niagara River", "Niagara Falls"),
    MonitoringStation("tokyo-international-centre", "", "", (35.676788, 139.763535), "", "Sumida River", "Tokyo"),
]
# Centre to use for tests. This is the location of London Bridge.
# London Bridge is 0.9km from Tower Bridge and 0.87km from The Tower of London.
radius_test_centre = (51.507877, -0.087732)


def test_stations_within_radius():
    finds = stations_within_radius(dummy_stations, radius_test_centre, 1.0)
    seen = {}
    for find in finds:
        assert find.river == "1", f"Station outside testing radius was returned (station: {find.station_id})"
        seen[find.station_id] = True

    for station in dummy_stations:
        if station.station_id not in seen:
            assert station.river != "1", \
                f"Station inside testing radius was NOT returned (station: {station.station_id})"


def test_station_by_distance():
    test_list = stations_by_distance(dummy_stations, radius_test_centre)
    for i in range(1, len(test_list) - 1):
        assert test_list[i][1] >= test_list[i - 1][1], f"Element {i} and {i - 1} where in the wrong order!"


def test_rivers_with_station():
    # test for duplicate entries ie a river comes up more than once
    test_list = rivers_with_station(dummy_stations_for_river_testing)
    assert len(dummy_stations_for_river_testing) > len(set(test_list)), "Duplicates of the same river present!"

def test_stations_by_river():
    # test to ensure stations on the same river have the same river key in the dictionary
    test_list = stations_by_river(dummy_stations_for_river_testing)
    assert len(test_list["River Thames"]) == 2, "Stations are not in the same item in the dictionary!"
