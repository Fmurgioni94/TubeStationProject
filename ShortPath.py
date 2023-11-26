import numpy as np
# Import the numpy module for numerical operations.
from adjacency_list_graph import AdjacencyListGraph
# Import the AdjacencyListGraph class from adjacency_list_graph module.
from dijkstra import dijkstra
# Import the dijkstra function from dijkstra module.
from reading_file import File
# Import the File class from reading_file module.
from mst import kruskal
# Import kruskal function and related functions from mst module.
from bfs import bfs
# Import the bfs function from bfs module.

class ShortPath():
    def __init__(self):
        # Initialize ShortPath object.
        self.file = File()
        # Create a File object to read and process the CSV file.
        self.vertices, self.edges = self.file.read_file()
        # Retrieve vertices and edges from the CSV file.

        self.graph1 = AdjacencyListGraph(len(self.vertices), False, True)
        self.graph2 = AdjacencyListGraph(len(self.vertices), False, True)
        # Create two graphs using AdjacencyListGraph, one for time and one for stops.

        # Insert the edges to the graphs
        for edge in self.edges:
            self.graph1.insert_edge(self.vertices[edge[0]], self.vertices[edge[1]],
                            self.edges[edge])
            self.graph2.insert_edge(self.vertices[edge[0]], self.vertices[edge[1]],
                            1)
            # Populate the graphs with edges and weights.

        # The users starting point
        self.start = self.validate_start(self.vertices)
        # Validate and set the user's starting point.

        # The users ending point
        self.arrive = self.validate_arrive(self.vertices)
        # Validate and set the user's ending point.

        # The index of the users starting point
        self.start_index = self.vertices[self.start]
        # Retrieve the index of the user's starting point.

        # The index of the users ending point
        self.arrive_index = self.vertices[self.arrive]
        # Retrieve the index of the user's ending point.
    
    # Validating the users input for the starting point (station)
    def validate_start(self, list_of_stops):
        while True:
            starting_station = input("Insert your starting point: ").title().strip()
            if starting_station in list_of_stops:
                return starting_station
            else:
                print("Invalid input. Please try again.")

    # Validating the users input for the ending point (station)
    def validate_arrive(self, list_of_stops):
        while True:
            arriving_station = input("Insert your arriving station: ").title().strip()
            if arriving_station in list_of_stops:
                return arriving_station
            else:
                print("Invalid input. Please try again.")
        # startingstation = random.choice(self.file.list_of_stations)
        # return startingstation

    def retrieve_path(self, d, pi, arriving_index):
        # Function to retrieve the path with times between stations, total time, and number of steps.
        path = []
        counter = 0
        total = d[arriving_index]
        while pi[arriving_index] is not None:
            time = d[arriving_index]
            path.append((arriving_index, time - d[pi[arriving_index]]))
            arriving_index = pi[arriving_index]
            counter += 1

        # Print the path with times between stations.
        for step in path[::-1]:
            print(
                f"From {self.file.list_of_stations[pi[step[0]]]} To the {self.file.list_of_stations[step[0]]}"
                f"({step[1]} minutes)."
            )
        print()
        # Print the total time.
        print(f"The trip will take in total {total} minutes.")
        print()

    def retrive_path_bfs(self, pi, arriving_index):
        # Function to retrieve the path using BFS with the number of steps.
        path = []
        counter = 0
        while pi[arriving_index] is not None:
            path.append(arriving_index)
            arriving_index = pi[arriving_index]
            counter += 1
        for step in path[::-1]:
            print(
                f"From {self.file.list_of_stations[pi[step]]} To the {self.file.list_of_stations[step]}"
            )
        print()
        print(f"The best path has {counter} stops.")

    # Implement Dijkstra Algorithm
    def dijkstra_algorithm_time(self, G):
        # Implementation of Dijkstra with the graph and the starting point (station)
        d, pi = dijkstra(G, self.start_index)

        # Call function to return the path with times between stations, total time, and number of steps.
        return self.retrieve_path(d, pi, self.arrive_index)
    
    def dijkstra_algorithm_stops(self, G):
        # Implementation of Dijkstra with the graph and the starting point (station) for stops.
        d, pi = dijkstra(G, self.start_index)
        return self.retrive_path_bfs(pi, self.arrive_index)

    def bfs_algo(self, G):
        # Implementation of BFS with the graph and the starting point (station)
        d, pi = bfs(G, self.start_index)
        return self.retrive_path_bfs(pi, self.arrive_index)

    # Implement Kruskal Algorithm
    def kruskal_algorithm(self, G):
        # Implementation of Kruskal with the graph
        mst = kruskal(G)
        stations_that_can_be_closed = []

        # Determine stations that can be closed by comparing original and MST edge lists.
        for link in self.graph1.get_edge_list():
            if link not in mst.get_edge_list():
                stations_that_can_be_closed.append(link)

        # Print stations that can be shut down and related statistics.
        for e in stations_that_can_be_closed:
            print(f"The link between '{self.file.list_of_stations[e[0]]} -- {self.file.list_of_stations[e[1]]}' can be shut down.")
        print(f"\nThe number of edges in the original graph: {len(self.graph1.get_edge_list())}")
        print(f"The number for links you can close: {len(stations_that_can_be_closed)}")
        print(f"The number of links needed to connect each stops: {len(self.graph1.get_edge_list()) - len(stations_that_can_be_closed)}")
