#!/usr/bin/env python3
# reading_file.py

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

import csv

class File:
    def __init__(self, vertices=None, edges=None, list_of_stations=None):
        """
        Initialize a File object with optional vertices and edges dictionaries.

        Args:
            vertices (dict, optional): A dictionary to store vertices. Defaults to an empty dictionary.
            edges (dict, optional): A dictionary to store edges. Defaults to an empty dictionary.
        """
        if edges is None:
            edges = dict()
        if vertices is None:
            vertices = dict()
        if list_of_stations is None:
            list_of_stations = list()
        self.vertices = vertices
        self.edges = edges
        self.list_of_stations = list_of_stations
        self.file_name = 'LondonUnderground.csv'

    def read_file(self):
        """
        Read data from a CSV file and populate the vertices and edges dictionaries.

        Returns:
            Tuple[dict, dict]: A tuple containing two dictionaries - edges and vertices.
        """
        # Open the CSV file for reading
        with open(self.file_name, 'r') as f:
            # Create a reader object
            reader = csv.reader(f)
            i = 0  # Initialize i
            for row in reader:
                if row[1].strip() not in self.vertices:
                    self.vertices[row[1].strip()] = i
                    self.list_of_stations.append(row[1].strip())
                    i += 1
                if len(row) == 4 and row[2] != "":
                    if (row[2].strip(), row[1].strip()) not in self.edges and (
                            row[1].strip(), row[2].strip()) not in self.edges:
                        self.edges[(row[1].strip(), row[2].strip())] = int(row[3].strip())
        return self.vertices, self.edges
