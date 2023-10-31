#

# London Underground Journey Planner.
#

import csv
import numpy as np
import hashlib
from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
import networkx as nx
import matplotlib.pyplot as plt

STATIONS_MAX = 272
stations_matrix = np.zeros((STATIONS_MAX, STATIONS_MAX))
stations = set()


def main():
    print(f'Welcome to London Underground Journey Planner!')
    graph = AdjacencyMatrixGraph(len(stations_matrix), directed=True, weighted=True)

    for u in range(len(stations_matrix)):
        for v in range(len(stations_matrix[u])):
            weight = stations_matrix[u][v]
            if weight != 0:
                graph.insert_edge(u, v, weight=weight)
    # d, pi = dijkstra(graph, 1)
    # print(d, pi)


# read CSV file with data
def read_csv(filename):
    print(f'Reading CSV file:', filename)

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        stations_set = set()
        for row in csv_reader:
            line_count += 1
            if row[2] == '' and row[3] == '':
                stations_set.add(row[1].strip())
                continue
            else:
                print(f'\t Line: {row[0]}, From Station: {row[1]}, To Station: {row[2]}, time: {row[3]} mins.')
                row_index = int(hashlib.sha256(row[1].strip().encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
                col_index = int(hashlib.sha256(row[2].strip().encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
                stations_matrix[row_index][col_index] = int(row[3].strip())

        print(f'Found {len(stations_set)} stations.')
        print(f'Processed {line_count} lines.')
        print(stations_matrix)
        print(stations)

        test_row = int(hashlib.sha256("Moor Park".encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
        test_col = int(hashlib.sha256("Harrow-on-the-Hill".encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
        print(f'Time is {stations_matrix[test_row][test_col]} min.')


# Press the green button in the gutter to run the script.


"""
G = nx.Graph()  # Use nx.DiGraph() for directed graphs

# Get the list of edges from your graph (assumes weighted graph)
for u, v in graph.get_edge_list():
    weight = graph.get_adj_matrix()[u][v]  # Get the weight from the adjacency matrix
    G.add_edge(u, v, weight=weight)

# Use a force-directed layout (spring layout) to minimize overlap
pos = nx.spring_layout(G, iterations=200, seed=42)

# Draw nodes with labels
node_labels = {i: str(i) for i in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

# Draw edges with labels
edge_labels = {(u, v): weight for (u, v, weight) in G.edges(data='weight')}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

# Draw the graph with additional parameters for clarity
nx.draw(G, pos, with_labels=False, node_size=50, node_color='skyblue', font_size=8, font_color='black', linewidths=0.25)
plt.axis('off')
plt.show()
"""

if __name__ == '__main__':
    main()
