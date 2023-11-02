# reading file
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