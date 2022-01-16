#!/usr/bin/env python3

"""
read a list of points from a CSV file and print out the length of the perimiter of the shape that is formed by joining the points in their listed order
"""

import csv
import sys

def perimiter(points: list) -> float:
    """ returns the length of the perimiter of some shape defined by a list of points """
    distances = get_distances(points)
    length = 0
    for distance in distances:
        length = length + distance

    return length


def get_distances(points: list) -> list:
    """ convert a list of points into a list of distances """
    i = 0
    distances = []
    for i in range(len(points)):
        point = points[i]
        if i == len(points)-1:
            next_point = points[0]
        else:
            next_point = points[i+1]
        x0 = point[0]
        y0 = point[1]
        x1 = next_point[0]
        y1 = next_point[1]

        point_distance = get_distance(x0, y0, x1, y1)
        distances.append(point_distance)
    return distances


def get_distance(x0: float, y0: float, x1: float, y1: float) -> float:
    """ use pythagorean theorm to find distance between 2 points """
    a = x0 - x1
    b = y0 - y1
    c_2 = a*a + b*b
    return c_2 ** (1/2)

def main(file_name: str):
    with open(file_name, 'r') as fp:
        reader = csv.reader(fp)
        next(reader)

        points = []
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            points.append((x,y))

        length = perimiter(points)

        print (f'Perimeter of {file_name} = {length}')


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        main(file_name)
    except IndexError:
        print("No CSV File Provided.")
        print("Program Exiting.")
    except FileNotFoundError as err:
        print(f'Invalid File source name.\n error ={err}')
        print("Program Exiting.")
    except ValueError as err:
        print(f'File seems to have invalid data.\n error: {err}')
        print("Program Exiting.")