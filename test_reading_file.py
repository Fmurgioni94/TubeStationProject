import unittest
from reading_file import File

class TestFileClass(unittest.TestCase):
    def test_read_file(self):
        # Create a File object
        file_obj = File()

        # Read the test data from the temporary CSV file
        file_obj.read_file()

        # Verify that the vertices and edges are populated correctly
        vertices, edges = file_obj.read_file()
        self.assertEqual(vertices, {
            'Harrow & Wealdstone': 0,
            'Kenton': 1,
            'South Kenton': 2,
            'North Wembley': 3,
            'Wembley Central': 4,
            'Stonebridge Park': 5,
            'Harlesden': 6,
            'Willesden Junction': 7,
            'Kensal Green': 8,
            "Queen's Park": 9,
            'Kilburn Park': 10,
            'Maida Vale': 11,
            'Warwick Avenue': 12,
            'Paddington': 13,
            'Edgware Road': 14,
            'Marylebone': 15,
            'Baker Street': 16,
            "Regent's Park": 17,
            'Oxford Circus': 18,
            'Piccadilly Circus': 19,
            'Charing Cross': 20,
            'Embankment': 21,
            'Waterloo': 22,
            'Lambeth North': 23,
            'Elephant & Castle': 24
        })

        self.assertEqual(edges, {
            ('Harrow & Wealdstone', 'Kenton'): 2,
            ('Kenton', 'South Kenton'): 2,
            ('South Kenton', 'North Wembley'): 2,
            ('North Wembley', 'Wembley Central'): 2,
            ('Wembley Central', 'Stonebridge Park'): 2,
            ('Stonebridge Park', 'Harlesden'): 2,
            ('Harlesden', 'Willesden Junction'): 2,
            ('Willesden Junction', 'Kensal Green'): 3,
            ('Kensal Green', "Queen's Park"): 2,
            ("Queen's Park", 'Kilburn Park'): 2,
            ('Kilburn Park', 'Maida Vale'): 2,
            ('Maida Vale', 'Warwick Avenue'): 1,
            ('Warwick Avenue', 'Paddington'): 2,
            ('Paddington', 'Edgware Road'): 3,
            ('Edgware Road', 'Marylebone'): 1,
            ('Marylebone', 'Baker Street'): 2,
            ('Baker Street', "Regent's Park"): 2,
            ("Regent's Park", 'Oxford Circus'): 2,
            ('Oxford Circus', 'Piccadilly Circus'): 2,
            ('Piccadilly Circus', 'Charing Cross'): 2,
            ('Charing Cross', 'Embankment'): 1,
            ('Embankment', 'Waterloo'): 2,
            ('Waterloo', 'Lambeth North'): 2,
            ('Lambeth North', 'Elephant & Castle'): 3
        })

        self.assertEqual(file_obj.list_of_stations, [
            'Harrow & Wealdstone', 'Kenton', 'South Kenton', 'North Wembley', 'Wembley Central', 'Stonebridge Park',
            'Harlesden', 'Willesden Junction', 'Kensal Green', "Queen's Park", 'Kilburn Park', 'Maida Vale',
            'Warwick Avenue', 'Paddington', 'Edgware Road', 'Marylebone', 'Baker Street', "Regent's Park",
            'Oxford Circus', 'Piccadilly Circus', 'Charing Cross', 'Embankment', 'Waterloo', 'Lambeth North',
            'Elephant & Castle'

        ])


if __name__ == '__main__':
    unittest.main()
