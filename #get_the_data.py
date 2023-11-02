#!/usr/bin/env python3
# get_the_data.py

# Advanced Algorithms and Data Structures
# Nir Peretz, Stefano Veglia, Francesco Murgioni, Nadiia Chernova and Jorge Gomez

#########################################################################
#                                                                       #
# Copyright 2023                                                        #
#                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining #
# a copy of this software and associated documentation files (the       #
# "Software"), to deal in the Software without restriction, including   #
# without limitation the rights to use, copy, modify, merge, publish,   #
# distribute, sublicense, and/or sell copies of the Software, and to    #
# permit persons to whom the Software is furnished to do so, subject to #
# the following conditions:                                             #
#                                                                       #
# The above copyright notice and this permission notice shall be        #
# included in all copies or substantial portions of the Software.       #
#                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS   #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN    #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN     #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
# SOFTWARE.                                                             #
#                                                                       #
#########################################################################

import numpy as np
import hashlib
from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
# import networkx as nx
import matplotlib.pyplot as plt
from reading_file import File
from bellman_ford import bellman_ford
from mst import kruskal, print_undirected_edges, get_total_weight

# Create an instance of the class
ReadFile = File()
# Create the vertices and edges dictionary
vertices, edges = ReadFile.read_file()
# Create the list of stations
station_list = ReadFile.list_of_stations

# Validating the users input for the starting point (station)
def validate_start(list_of_stops):
    while True:
        starting_station = input("Insert you starting point: ").title().strip()
        if starting_station in list_of_stops:
            return starting_station
        else:
            print("Invalid input. Please try again.")


# Validating the users input for the ending point (station)
def validate_arrive(list_of_stops):
    while True:
        arriving_station = input("Insert you arriving station: ").title().strip()
        if arriving_station in list_of_stops:
            return arriving_station
        else:
            print("Invalid input. Please try again.")


def retrieve_path(d, pi, arriving_index):
    path = []
    counter = 0
    total = d[arriving_index]
    while pi[arriving_index] is not None:
        time = d[arriving_index]
        path.append((arriving_index, time - d[pi[arriving_index]]))
        arriving_index = pi[arriving_index]
        counter += 1

    # return the path with times between stations
    for step in path:
        print(f"To the {station_list[step[0]]} station is going to take {step[1]} minutes.")

    # return the total time
    print(f"The trip will take in total {total} minutes.")

    # return the number of steps
    print(f"The best path has {counter} steps.")


# Create a graph implemented by an adjacency list
graph1 = AdjacencyListGraph(len(vertices), False, True)

# Insert the edges to the graph
for edge in edges:
    graph1.insert_edge(vertices[edge[0]], vertices[edge[1]],
                       edges[edge])

# The users starting point
start = validate_start(vertices)
# The users ending point
arrive = validate_arrive(vertices)

# The index of the users starting point
start_index = vertices[start]
# The index of the users ending point
arrive_index = vertices[arrive]


# Implement Dijkstra Algorithm
def dijkstra_algorithm():
    # Implementation on Dijkstra with the graph and the starting point (station)
    d, pi = dijkstra(graph1, start_index)

    # Function to return the path with times between stations, total time and number of steps
    return retrieve_path(d, pi, arrive_index)


# Implement Bellman Ford Algorithm
def bellman_ford_algorithm():
    d, pi, cycle = bellman_ford(graph1, start_index)
    retrieve_path(d, pi, arrive_index)
    print("No negative-weight cycle:", cycle)


# Implement Kruskal Algorithm
def kruskal_algorithm():
    kruskal1 = kruskal(graph1)
    print_undirected_edges(kruskal1, station_list)
    kruskal_weight = get_total_weight(kruskal1)
    print("Kruskal weight =", kruskal_weight)


# Test results

# dijkstra_algorithm()
# bellman_ford_algorithm()
# kruskal_algorithm()
