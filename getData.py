#

# London Underground Journey Planner.
#

import csv
import numpy as np
import hashlib


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

        test_row = int(hashlib.sha256("Moor Park".encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
        test_col = int(hashlib.sha256("Harrow-on-the-Hill".encode('utf-8')).hexdigest(), 16) % STATIONS_MAX
        print(f'Time is {stations_matrix[test_row][test_col]} min.')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
