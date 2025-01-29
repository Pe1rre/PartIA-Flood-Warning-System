# Copyright (C) 2025 Ethan J. Marshall (em2017@cam.ac.uk)
#
# SPDX-License-Identifier: MIT
"""Unit tests for the geo package."""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius


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

# Centre to use for test for stations_within_radius. This is the location of London Bridge.
# London Bridge is 0.9km from Tower Bridge and 0.87km from The Tower of London.
radius_test_centre = (51.507877, -0.087732)


def test_stations_within_radius():
    finds = stations_within_radius(dummy_stations, radius_test_centre, 1.0)
    for find in finds:
        assert find.river == "1", f"Station outside testing radius was returned (station: {find.station_id})"
