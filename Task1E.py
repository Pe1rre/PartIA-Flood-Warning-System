# Copyright (C) 2025 Ethan J. Marshall
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()
    # Get the top 9 rivers by station count
    matches = rivers_by_station_number(stations, 9)
    print(matches)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
