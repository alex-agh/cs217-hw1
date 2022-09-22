from math import cos, sin, pi
import numpy as np


class Polygon:
    def __init__(self, r, n, x_c, y_c):
        self.r = r
        self.n = n
        self.x_c = x_c
        self.y_c = y_c

        self.vertices = self.get_polygon_vertices()
        self.edges = self.get_polygon_edges()

    def get_polygon_vertices(self):
        """Set the vertices of the initial created polygon."""
        coordinates = []
        omega = pi / 2
        for i in range(0, self.n):
            x = self.x_c + self.r * cos(omega)
            y = self.y_c + self.r * sin(omega)
            omega += 2*pi / self.n
            coordinates.append([round(x), round(y), 1])
        return coordinates

    def get_polygon_edges(self):
        """Set the edges of the polygon."""
        coordinates = self.vertices
        coordinates.append(coordinates[0])
        edges = []
        for i in range(0, len(coordinates) - 1):
            edges.append([coordinates[i], coordinates[i + 1]])
        coordinates.pop()
        return edges

    def set_center(self):
        """Update the center for the polygon."""
        self.x_c = int(sum([vertex[0] for vertex in self.vertices]) / len(self.vertices))
        self.y_c = int(sum([vertex[1] for vertex in self.vertices]) / len(self.vertices))

    def transform(self, matrix):
        """Apply the transformation matrix."""
        translate = [
            [1, 0, self.x_c],
            [0, 1, self.y_c],
            [0, 0, 1]
        ]

        reverse = [
            [1, 0, -self.x_c],
            [0, 1, -self.y_c],
            [0, 0, 1]
        ]

        final = np.linalg.multi_dot([translate, matrix, reverse])
        self.vertices = [
            [
                int(round(x)) for x in np.dot(final, vertex).tolist()
            ] for vertex in self.vertices
        ]
        self.edges = self.get_polygon_edges()

    def scale(self, increment=0):
        scale = [
            [1 + increment, 0, 0],
            [0, 1 + increment, 0],
            [0, 0,             1]
        ]
        self.transform(scale)

    def counter_clockwise(self, omega=pi/10):
        rotate = [
            [cos(omega), -sin(omega), 0],
            [sin(omega), cos(omega),  0],
            [0,       0,              1]
        ]

        self.transform(rotate)

    def clockwise(self, omega=pi/10):
        rotate = [
            [cos(omega), sin(omega), 0],
            [-sin(omega), cos(omega),  0],
            [0,       0,              1]
        ]

        self.transform(rotate)

    def move(self, increment, index=0):
        for vertex in self.vertices:
            vertex[index] += increment

        if index == 0:
            self.x_c += increment
        if index == 1:
            self.y_c += increment
        self.edges = self.get_polygon_edges()