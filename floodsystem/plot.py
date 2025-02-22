import matplotlib as plt
from datetime import datetime, timedelta


#Task 2E
#does dates mean that 2 dates are inputed are inputed
def plot_water_levels(station, dates, levels):
    t = dates
    level = levels
    high_low = station.typical_range

    # Plot
    plt.plot(t, level)
    #How do I work out the typical high and low ranges of a rivers water level?
    plt.plot(high_low[0])
    plt.plot(high_low[1])

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.id)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()