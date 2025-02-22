from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
def run():
    stations = build_station_list()
    N = 10
    tuples = stations_highest_rel_level(stations, N)
    return tuples

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()