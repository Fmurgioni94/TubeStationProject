# get the data

import csv
import numpy as np
import hashlib
from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
import networkx as nx
import matplotlib.pyplot as plt


# Open the CSV file for reading
with open('LondonUnderground.csv', 'r') as f:
    # Create a reader object
    reader = csv.reader(f)
    list_of_stops = []
    list_of_edges = []
    for row in reader:
        if row[1].strip() not in set(list_of_stops):
            list_of_stops.append(row[1].strip())
        if len(row) == 4 and row[2] != "":
            if (row[2].strip(), row[1].strip(), row[3].strip()) not in set(list_of_edges) and (row[1].strip(), row[2].strip(), row[3].strip()) not in set(list_of_edges):
                list_of_edges.append((row[1].strip(), row[2].strip(), row[3].strip()))
    for i in range(len(list_of_edges)):
        list_of_edges[i] = (list_of_edges[i][0],list_of_edges[i][1],int(list_of_edges[i][2]))

    graph1 = AdjacencyListGraph(len(list_of_stops), False, True)

    #insert the starting and ending stations
    starting_station = input("Insert you starting point.")
    arriving_station = input("Insert you arriving station.")

    #we retrive the index now with the command index, but will be implemented with dictionary
    starting_index = list_of_stops.index(starting_station)
    arriving_index = list_of_stops.index(arriving_station)


    # thi part needs an update that consider the edges are now dictionary
    for edge in list_of_edges:
        graph1.insert_edge(list_of_stops.index(edge[0]), list_of_stops.index(edge[1]), edge[2])
    d, pi = dijkstra(graph1, list_of_stops.index(starting_station))

    # for i in range(len(list_of_stops)):
    #     print(list_of_stops[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else list_of_stops[pi[i]]))
    # print(pi)
    # print(d)
    #
    # for i in range(len(list_of_stops)):
    #     print(i, list_of_stops[i])
    path = []
    while pi[arriving_index] is not None:
        time = d[arriving_index]
        next_station = pi[arriving_index]
        path.append(())


