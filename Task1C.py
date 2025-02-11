# Copyright (C) 2025 Ethan J. Marshall (em2017@cam.ac.uk)
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    # Get those within radius
    matches = stations_within_radius(stations, (52.2053, 0.1218), 10)
    # Sort by the name of each station
    matches.sort(key=lambda x: x.name)
    # Print the name of each match
    for match in matches:
        print(match.name)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
