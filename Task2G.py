# Copyright (C) 2025 Ethan. J. Marshall
#
# SPDX-License-Identifier: MIT

from datetime import timedelta

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood, datafetcher, analysis


class SeverityScore:
    LOW = 0
    MODERATE = 1
    HIGH = 2
    SEVERE = 3

    _severity = LOW

    def __init__(self, score=LOW):
        self._severity = score

    def __repr__(self):
        if self._severity == SeverityScore.LOW:
            return "LOW"
        elif self._severity == SeverityScore.MODERATE:
            return "MODERATE"
        elif self._severity == SeverityScore.HIGH:
            return "HIGH"
        elif self._severity == SeverityScore.SEVERE:
            return "SEVERE"
        else:
            raise ValueError("invalid severity score")

    def __gt__(self, x):
        return self._severity > x._severity

    def __lt__(self, x):
        return self._severity < x._severity


def determine_severity(station, grad_now):
    if station.relative_water_level() >= 2:
        return SeverityScore(SeverityScore.SEVERE)
    elif station.relative_water_level() >= 1.7 or (station.relative_water_level() >= 1.5 and grad_now > 0):
        return SeverityScore(SeverityScore.HIGH)
    elif station.relative_water_level() >= 1.5:
        return SeverityScore(SeverityScore.MODERATE)
    else:
        return SeverityScore(SeverityScore.LOW)


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Stores a town name
    # If a station which indicates an impending flood is found,
    # the value is set to not None with a tuple value indicating
    # the severity (item 0) and the offending station (item 1).
    town_matches = {}

    # Criteria:
    # Severe severity: water level is gt 2x typical high mark
    # High severity: water level is above 1.5x typical high mark with increasing gradient
    # Moderate severity: water level is at 1.5x typical high mark with *any* gradient
    # Low severity: anything else
    #
    # Only include stations with consistent relative levels.
    higheststations = flood.stations_highest_rel_level(stations, 10)

    for station in higheststations:
        dates, levels = datafetcher.fetch_measure_levels(station[0].measure_id,
                                                         timedelta(days=2))
        if len(dates) == 0 or len(levels) == 0:
            continue

        poly, _ = analysis.polyfit(dates, levels, 4)
        grad = poly.deriv(1)
        # The current date is stored at index zero apparently
        grad_now = grad(0)
        severity = determine_severity(station[0], grad_now)
        if station[0].town is None:
            station[0].town = station[0].name
        if station[0].town not in town_matches or severity > town_matches[station[0].town][0]:
            town_matches[station[0].town] = (severity, station[0])

    for match in town_matches.keys():
        print("{} WARNING FOR {}: Water level is {}x typical high!".format(town_matches[match][0],
              match, town_matches[match][1].relative_water_level()))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
