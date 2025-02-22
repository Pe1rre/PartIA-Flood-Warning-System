

#Task 2B
def stations_level_over_threshold(stations, tol):
    list_of_tuples = []
    for station in stations:
        if station.typical_range_consistent():
            relative_level = station.relative_water_level()
            if relative_level > tol:
                z = (station, relative_level)
                list_of_tuples.append(z)
    return sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
#Unit testing for this could just be to double check that the station levels are consistent OR that it is in the right order?

#Task 2C
def stations_highest_rel_level(stations, N):
    list_of_tuples = []
    for station in stations:
        if stations.typical_range_consistent(station):
            relative_level = stations.relative_water_level(station)
            z = (station, relative_level)
            list_of_tuples.append(z)
    list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1], reverse=False)
    #Use a slice to get the first N
    return (list_of_tuples[0:N+1])
