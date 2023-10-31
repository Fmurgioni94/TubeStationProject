# get the data

import csv

# Open the CSV file for reading
with open('LondonUnderground.csv', 'r') as f:
    # Create a reader object
    reader = csv.reader(f)
    list_of_stops = []
    list_of_edges = []
    for row in reader:
        if row[1] not in list_of_stops:
            list_of_stops.append(row[1])
        if len(row) == 4 and row[2] != "":
            list_of_edges.append((row[1], row[2], row[3]))

    # print(list_of_stops)
    print(list_of_edges)
