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
# Import the csv module to handle CSV file operations.

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
        # Set default values for vertices, edges, and list_of_stations, and specify the file name.
        self.__vertices = vertices
        self.__edges = edges
        self.__list_of_stations = list_of_stations
        self.__file_name = 'LondonUnderground.csv'

    @property
    def list_of_stations(self):
        # Property method to access the private attribute __list_of_stations from outside the class.
        return self.__list_of_stations
    
    @property
    def vertices(self):
        # Property method to access the private attribute __vertices from outside the class.
        return self.__vertices
    
    @property
    def edges(self):
        # Property method to access the private attribute __edges from outside the class.
        return self.__edges

    def read_file(self):
        """
        Read data from a CSV file and populate the vertices and edges dictionaries.

        Returns:
            Tuple[dict, dict]: A tuple containing two dictionaries - edges and vertices.
        """
        try:
            # Open the CSV file for reading
            with open(self.__file_name, 'r') as f:
                # Create a reader object
                reader = csv.reader(f)
                i = 0  # Initialize i
                for row in reader:
                    if row:
                        if row[1].strip() not in self.__vertices:
                            # Add vertex to the vertices dictionary
                            self.__vertices[row[1].strip()] = i
                            self.__list_of_stations.append(row[1].strip())
                            i += 1
                        if len(row) == 4 and row[2] != "":
                            # Add edge to the edges dictionary
                            if (row[2].strip(), row[1].strip()) not in self.__edges and (
                                    row[1].strip(), row[2].strip()) not in self.__edges:
                                self.__edges[(row[1].strip(), row[2].strip())] = int(row[3].strip())
        except FileNotFoundError:
            # Handle the case where the file is not found
            raise FileNotFoundError("File not found.")
        except csv.Error as e:
            # Handle CSV errors
            raise ValueError(f"CSV error: {str(e)}")

        if not self.__vertices or not self.__edges:
            # Check if the file is empty or in the wrong structure
            raise ValueError("The file is empty or in the wrong structure.")

        return self.__vertices, self.__edges

