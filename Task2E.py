from floodsystem import datafetcher
from datetime import timedelta
from floodsystem import plot, flood, stationdata


def run():
    N = 5
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    station_list = flood.stations_highest_rel_level(stations, N)
    for station in station_list:
        dates, levels = datafetcher.fetch_measure_levels(station[0].measure_id,
                                                         timedelta(days=10))
        plot.plot_water_levels(station[0], dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
