# get the data

import csv

# Open the CSV file for reading
with open('LondonUnderground.csv', 'r') as f:
    # Create a reader object
    reader = csv.reader(f)
    list_of_stops = []
    list_of_edges = []
    for row in reader:
        if row[1].strip() not in list_of_stops:
            list_of_stops.append(row[1].strip())
        if len(row) == 4 and row[2] != "":
            list_of_edges.append((row[1].strip(), row[2].strip(), row[3].strip()))

    # print(list_of_stops)
    print(list_of_edges)
    print(len(set(list_of_edges)))
