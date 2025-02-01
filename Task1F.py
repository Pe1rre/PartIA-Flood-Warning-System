# Copyright (C) 2025 Ethan J. Marshall
# Copyright (C) 2025 Peter Kelly
#
# SPDX-License-Identifier: MIT

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()
    matchs = inconsistent_typical_range_stations(stations)
    for match in matchs:
        print(match.name)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
