# get the data

import numpy as np
import hashlib
from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
# import networkx as nx
import matplotlib.pyplot as plt
from reading_file import File
from bellman_ford import bellman_ford

ReadFile = File()
vertices, edges = ReadFile.read_file()
station_list = ReadFile.list_of_stations

# insert the starting and ending stations
def validate_start(list_of_stops):
    while True:
        starting_station = input("Insert you starting point: ").title().strip()
        if starting_station in list_of_stops:
            return starting_station
        else:
            print("Invalid input. Please try again.")


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


graph1 = AdjacencyListGraph(len(vertices), False, True)

for edge in ReadFile.read_file()[1]:
    graph1.insert_edge(vertices[edge[0]], vertices[edge[1]],
                       edges[edge])

start = validate_start(vertices)
arrive = validate_arrive(vertices)
# we retrieve the index now with the command index, but will be implemented with dictionary
start_index = vertices[start]
arrive_index = vertices[arrive]
# d, pi = dijkstra(graph1, start_index)

# retrieve_path(d, pi, arrive_index)

d, pi, cycle = bellman_ford(graph1, start_index)
retrieve_path(d, pi, arrive_index)
print("No negative-weight cycle:", cycle)
