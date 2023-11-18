import numpy as np
import hashlib
from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
import matplotlib.pyplot as plt
from reading_file import File
from bellman_ford import bellman_ford
from mst import kruskal, print_undirected_edges, get_total_weight
from bfs import bfs
import random

class ShortPath():
    
    def __init__(self):
        self.file = File()
        self.vertices, self.edges = self.file.read_file()
        
        self.graph1 = AdjacencyListGraph(len(self.vertices), False, True)
        self.graph2 = AdjacencyListGraph(len(self.vertices), False, True)
        # Insert the edges to the graph
        for edge in self.edges:
            self.graph1.insert_edge(self.vertices[edge[0]], self.vertices[edge[1]],
                            self.edges[edge])
            self.graph2.insert_edge(self.vertices[edge[0]], self.vertices[edge[1]],
                            1)
            
        # The users starting point
        self.start = self.validate_start(self.vertices)
        # The users ending point
        self.arrive = self.validate_arrive(self.vertices)

        # The index of the users starting point
        self.start_index = self.vertices[self.start]
        # The index of the users ending point
        self.arrive_index = self.vertices[self.arrive]
    

    


    # Validating the users input for the starting point (station)
    def validate_start(self, list_of_stops):
        while True:
            starting_station = input("Insert you starting point: ").title().strip()
            if starting_station in list_of_stops:
                return starting_station
            else:
                print("Invalid input. Please try again.")
        # startingstation = random.choice(self.file.list_of_stations)
        # return startingstation


    # Validating the users input for the ending point (station)
    def validate_arrive(self, list_of_stops):
        while True:
            arriving_station = input("Insert you arriving station: ").title().strip()
            if arriving_station in list_of_stops:
                return arriving_station
            else:
                print("Invalid input. Please try again.")
        # startingstation = random.choice(self.file.list_of_stations)
        # return startingstation


    def retrieve_path(self, d, pi, arriving_index):
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
                f"From {self.file.list_of_stations[pi[step[0]]]} To the {self.file.list_of_stations[step[0]]}"
                f"({step[1]} minutes)."
            )
        print()
        # return the total time
        print(f"The trip will take in total {total} minutes.")
        print()
        # return the number of steps
        print(f"The best path has {counter} steps.")

    def retrive_path_bfs(self, pi, arriving_index):
        path = []
        counter = 0
        while pi[arriving_index] != None:
            path.append(arriving_index)
            arriving_index = pi[arriving_index]
            counter += 1
        for step in path[::-1]:
            print(
                f"From {self.file.list_of_stations[pi[step]]} To the {self.file.list_of_stations[step]}"
            )
        print()
        print(f"The best path has {counter} steps.")


    # Implement Dijkstra Algorithm
    def dijkstra_algorithm_time(self, G):
        # Implementation on Dijkstra with the graph and the starting point (station)
        d, pi = dijkstra(G, self.start_index)

        # Function to return the path with times between stations, total time and number of steps
        return self.retrieve_path(d, pi, self.arrive_index)
    
    def dijkstra_algorithm_stops(self, G):
        d, pi = dijkstra(G, self.start_index)
        return self.retrive_path_bfs(pi, self.arrive_index)

    # Implement Bellman Ford Algorithm
    def bellman_ford_algorithm(self, G):
        d, pi, circle = bellman_ford(G, self.start_index)
        return self.retrieve_path(d, pi, self.arrive_index)

    def bfs_algo(self, G):
        d, pi = bfs(G, self.start_index)
        return self.retrive_path_bfs(pi, self.arrive_index)



    # Implement Kruskal Algorithm
    def kruskal_algorithm(self, G):
        mst = kruskal(G)
        stations_that_can_be_closed = []

        for link in self.graph1.get_edge_list():
            if link not in mst.get_edge_list():
                stations_that_can_be_closed.append(link)

        for e in stations_that_can_be_closed:
            print(f"The link between '{self.file.list_of_stations[e[0]]} -- {self.file.list_of_stations[e[1]]}' can be shut down.")
        print(f"\nThe number of edges: {len(self.graph1.get_edge_list())}")
        print(f"The number for links you can close: {len(stations_that_can_be_closed)}")
        print(f"The number of links still operating: {len(self.graph1.get_edge_list()) - len(stations_that_can_be_closed)}")