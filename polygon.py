from math import cos, sin, ceil, pi


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
            coordinates.append((ceil(x), ceil(y)))
        return coordinates

    def get_polygon_edges(self):
        """Set the edges of the polygon."""
        coordinates = self.vertices
        coordinates.append(coordinates[0])
        edges = []
        for i in range(0, len(coordinates) - 1):
            edges.append((coordinates[i], coordinates[i + 1]))
        return edges

