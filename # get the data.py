# get the data

import csv
import numpy as np
import hashlib
from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
# import networkx as nx
import matplotlib.pyplot as plt


# Open the CSV file for reading
with open('LondonUnderground.csv', 'r') as f:
    # Create a reader object
    reader = csv.reader(f)
    vertices = {}
    edges = {}
    i = 0
    for row in reader:
        if row[1].strip() not in vertices:
            vertices[row[1].strip()] = i 
            i += 1  
        if len(row) == 4 and row[2] != "":
            if (row[2].strip(), row[1].strip()) not in edges and (row[1].strip(), row[2].strip()) not in edges:
                edges[(row[1].strip(), row[2].strip())] = int(row[3].strip())

    graph1 = AdjacencyListGraph(len(vertices), False, True)

    #insert the starting and ending stations
    starting_station = input("Insert you starting point.")
    arriving_station = input("Insert you arriving station.")

    #we retrive the index now with the command index, but will be implemented with dictionary
    starting_index = vertices[starting_station]
    arriving_index = vertices[arriving_station]


    # thi part needs an update that consider the edges are now dictionary
    for edge in list_of_edges:
        graph1.insert_edge(vertices[edge[0]], vertices[edge[1]], edges[edge])
    d, pi = dijkstra(graph1, vertices[starting_station])

    
    path = []
    counter = 0
    while pi[arriving_index] is not None:
        time = d[arriving_index]
        next_station = pi[arriving_index]
        path.append(())


