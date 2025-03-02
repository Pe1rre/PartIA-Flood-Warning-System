from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    tuples = stations_level_over_threshold(stations, tol)
    print(tuples)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
