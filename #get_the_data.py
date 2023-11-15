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
from bfs import bfs
from generate_random_graph import generate_random_graph
import time

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
    for step in path[::-1]:
        print(
            f"From {station_list[pi[step[0]]]} To the {station_list[step[0]]}"
            f" station is going to take {step[1]} minutes.")

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


# # The users starting point
# start = validate_start(vertices)
# # The users ending point
# arrive = validate_arrive(vertices)
#
# # The index of the users starting point
# start_index = vertices[start]
# # The index of the users ending point
# arrive_index = vertices[arrive]


# Implement Dijkstra Algorithm
def dijkstra_algorithm(G):
    # Implementation on Dijkstra with the graph and the starting point (station)
    d, pi = dijkstra(G, start_index)

    # Function to return the path with times between stations, total time and number of steps
    return retrieve_path(d, pi, arrive_index)


# Implement Bellman Ford Algorithm
def bellman_ford_algorithm(G):
    d, pi, circle = bellman_ford(G, start_index)
    print(d)
    print(pi)
    retrieve_path(d, pi, arrive_index)


def bfs_algo(G):
    d, pi = bfs(G, start_index)
    print(d)
    print(pi)
    retrieve_path(d, pi, arrive_index)


# Implement Kruskal Algorithm
def kruskal_algorithm(G):
    mst = kruskal(G)
    stations_that_can_be_closed = []

    for link in graph1.get_edge_list():
        if link not in mst.get_edge_list():
            stations_that_can_be_closed.append(link)

    for e in stations_that_can_be_closed:
        print(f"The link between '{station_list[e[0]]} -- {station_list[e[1]]}' can be shut down.")
    print(f"\nThe number of edges: {len(graph1.get_edge_list())}")
    print(f"The number for links you can close: {len(stations_that_can_be_closed)}")
    print(f"The number of links still operating: {len(graph1.get_edge_list()) - len(stations_that_can_be_closed)}")


# def test_run(func):
#     def inner(*args):
#         total_time = 0
#         for j in range(3):
#             start = time.time()
#             func(*args)
#             end = time.time()
#             time_elapsed = end - start
#             total_time += time_elapsed
#             print("Run", j + 1, "elapsed time:", time_elapsed)
#         return "Average elapsed time:", total_time / 3
#
#     return inner

def average_execution_time(func, graph, start):
    total_time = 0

    for _ in range(3):
        start_time = time.time()
        func(graph, start)
        end_time = time.time()
        total_time += end_time - start_time

    average_time = total_time / 3
    return average_time


# Test the average_execution_time function


inputs = [100, 500, 2500]
res_d = []
res_b = []

# @test_run
# def test_d():
#     res_d.append(dijkstra(graph2, 4))
#
#
# @test_run
# def test_b():
#     res_b.append(bfs(graph2, 4))



import random

edge_list = [0.1, 0.35, 0.8]
for j in edge_list:
    for i in inputs:
        val = random.randint(1, i)
        card_V = i
        min_w = 0
        max_w = 15
        graph2 = generate_random_graph(card_V, j, True, False, True, min_w, max_w)
        res_d.append(average_execution_time(dijkstra, graph2, val))
        res_b.append(average_execution_time(bfs, graph2, val))

print(res_d)
print(res_b)

# # Test results
# space = "-" * 50
# print()
# print("Dijkstra's Algorithm")
# print(space)
# dijkstra_algorithm(graph1)
# print()
# print("Dijkstra's Algorithm after Kruskal's Algorithm")
# print(space)
# dijkstra_algorithm(kruskal(graph1))
# print()
# print("Bellman-Ford's Algorithm")
# print(space)
# bellman_ford_algorithm(graph1)
# print()
# print("Bfs")
# print(space)
# bfs_algo(graph1)
# print()
# print("Bellman-Ford's Algorithm after Kruskal's Algorithm")
# print(space)
# bellman_ford_algorithm(kruskal(graph1))
# print()
# print(space)
# kruskal_algorithm(graph1)
# print(space)
# print()
