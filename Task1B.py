from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    # prints a list of tuples for the ten closest and ten furthest stations from Cambridge City centre
    list_of_stations = stations_by_distance(stations=build_station_list(), p=(52.2053, 0.1218))
    closest_stations = list_of_stations[:10]
    furthest_stations = list_of_stations[-10:]

    for closest in closest_stations:
        print(closest[0], closest[1])
    for furthest in furthest_stations:
        print(furthest[0], furthest[1])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IB Flood Warning System ***")
    run()
