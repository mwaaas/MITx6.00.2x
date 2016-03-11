"""
In this problem and the next, we will explore how to make sense of a collection of data by first parsing the data, and then producing a meaningful plot that visually explains what the raw numbers say.

The file julyTemps.txt contains the daily maximum and minimum temperatures for each day in Boston for the 31 days of July 2012. Open the file in a text editor and look at how it is formatted. The goal of this exercise is to produce a plot that shows the difference between the high and the low temperature for each day.

First, we will write a function to load the data out of this file (for a review of file loading and processing, see Problem Set 1 - Review of IO. You may also wish to read up on the Python docs on file objects, particularly how to read multiple lines in a file).

We want this function to return a tuple of 2 lists: one for high temperatures and one for low temperatures.

"""

def extract_data():
    inFile = open('julyTemps.txt', 'r', 0)

    high_temps = []

    low_temps = []

    with inFile as f:
        for line in inFile:
            fields = line.split()
            if len(fields) != 3 or 'Boston' == fields[0] or \
                            'Day' == fields[0]:
                high_temps.append(fields[1])
                low_temps.append(fields[2])

    return (high_temps, low_temps)

