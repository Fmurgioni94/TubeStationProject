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


def main():
    print(f'Welcome to London Underground Journey Planner!')
    read_csv("underground_data.csv")


# read CSV file with data
def read_csv(filename):
    print(f'Reading CSV file:', filename)

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        stations_set = set()
        station_dict = dict()
        index = 0
        for row in csv_reader:
            line_count += 1
            if row[2] == '' and row[3] == '':
                station = row[1].strip()
                stations_set.add(station)
                if station not in station_dict.values():
                    station_dict[index] = station
                    index += 1
                continue
            else:
                print(f'\t Line: {row[0]}, From Station: {row[1]}, To Station: {row[2]}, time: {row[3]} mins.')
                row_index = int(hashlib.sha256(row[1].strip().encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
                col_index = int(hashlib.sha256(row[2].strip().encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
                stations_matrix[row_index][col_index] = int(row[3].strip())
        print(station_dict)
        print(f'Found {len(stations_set)} stations.')
        print(f'Processed {line_count} lines.')

        test_row = int(hashlib.sha256("Moor Park".encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
        test_col = int(hashlib.sha256("Harrow-on-the-Hill".encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
        print(f'Time is {stations_matrix[test_row][test_col]} min.')
        print(stations_matrix)
        edges = set()
        for i in range(len(stations_matrix)):
            for j in range(len(stations_matrix[0])):
                if stations_matrix[i][j] != 0:
                    edges.add((i, j, stations_matrix[i][j]))
                    # edges.add((j, i, stations_matrix[i][j]))
        graph1 = AdjacencyListGraph(len(stations_set), False, True)

        for edge in edges:
            graph1.insert_edge(edge[0], edge[1], edge[2])
        d, pi = dijkstra(graph1, 0)
        for i in range(len(stations_set)):
            print(station_dict[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else station_dict[pi[i]]))
        print()
        print(d, pi)
        print(sorted(stations_set))
        print(sorted(station_dict.values()))
        print(len(stations_set), len(station_dict))
        print(station_dict[269], station_dict[11])
        # m = [
        #     [0, 3, 0, 1, 0, 0], [0, 0, 2, 4, 0, 2], [0, 0, 0, 0, 5, 0], [0, 0, 0, 0, 8, 0], [0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0]
        # ]
        # edges = set()
        # vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        # for i in range(len(m)):
        #     for j in range(len(m[0])):
        #         if m[i][j] != 0:
        #             edges.add((i, j, m[i][j]))
        #             # edges.add((j, i, m[i][j]))
        # graph1 = AdjacencyListGraph(len(stations_set), False, True)
        # for edge in edges:
        #     graph1.insert_edge(edge[0], edge[1], edge[2])
        # print(edges)
        # d, pi = dijkstra(graph1, 0)
        # for i in range(len(m)):
        #     print(vertices[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else vertices[pi[i]]))
        # print()
        # print(d, pi)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
