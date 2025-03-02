from floodsystem import datafetcher
from datetime import timedelta
from floodsystem import plot, flood, stationdata


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    higheststations = flood.stations_highest_rel_level(stations, 5)

    for station in higheststations:
        dates, levels = datafetcher.fetch_measure_levels(station[0].measure_id,
                                                         timedelta(days=2))
        if len(dates) == 0 or len(levels) == 0:
            continue
        plot.plot_water_level_with_fit(station[0], dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
