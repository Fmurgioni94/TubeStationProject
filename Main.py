from ShortPath import ShortPath
# Import the ShortPath class from the ShortPath module.
from mst import kruskal
# Import the kruskal function from the mst module.

# Create an instance of the ShortPath class
s = ShortPath()
# Print the starting and arriving stations
print(s.start, s.arrive)

# Generate the minimum spanning tree using Kruskal's algorithm
kruskal_minumim_spanning_tree = kruskal(s.graph1)

# Create a line of dashes for better output formatting
space = "-" * 50
print()
# Print results for Dijkstra's Algorithm Time
print("Dijkstra's Algorithm Time")
print(space)
s.dijkstra_algorithm_time(s.graph1)
print()
# Print results for Dijkstra's Algorithm Stops
print("Dijkstra's Algorithm Stops")
print(space)
s.dijkstra_algorithm_stops(s.graph2)
print()
# Print results for BFS Algorithm
print("Bfs Algorithm")
print(space)
s.bfs_algo(s.graph2)
print()
# Print the list of edges that is possible to close
print("List of edges that is possible to close:")
print(space)
s.kruskal_algorithm(s.graph1)
print()
# Print results for Dijkstra's Algorithm Time after Kruskal's Algorithm
print("Dijkstra's Algorithm time after Kruskal's Algorithm")
print(space)
s.dijkstra_algorithm_time(kruskal_minumim_spanning_tree)
print()
# Print results for Dijkstra's Algorithm Stops after Kruskal's Algorithm
print("Dijkstra's Algorithm stops after Kruskal's Algorithm")
print(space)
s.dijkstra_algorithm_stops(kruskal_minumim_spanning_tree)
print()
# Print results for BFS Algorithm after Kruskal's Algorithm
print("Bfs Algorithm after Kruskal's Algorithm")
print(space)
s.bfs_algo(kruskal_minumim_spanning_tree)