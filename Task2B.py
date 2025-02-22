from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    tol = 0.8
    tuples = stations_level_over_threshold(stations, tol)
    return tuples

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()