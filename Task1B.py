from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance


def run():
    list_of_stations = stations_by_distance(stations=build_station_list(), p=(52.2053, 0.1218))
    closest_stations = list_of_stations[:10]
    furthest_stations = list_of_stations[:-10]
    print(closest_stations, furthest_stations) 




if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()