import pygame
from bresenham import get_coordinates
from math import sin, cos, pi, floor, ceil


class App:
    def __init__(self):
        self.background_colour = (47, 79, 79)
        (width, height) = (800, 600)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Draw Line')
        self.screen.fill(self.background_colour)
        self.main_loop()

    @staticmethod
    def get_polygon_coordinates(n, r=50, x_c=400, y_c=300):
        coordinates = []
        omega = pi / 2
        for i in range(0, n):
            x = x_c + r*cos(omega)
            y = y_c + r*sin(omega)
            omega += 2*pi / n
            coordinates.append((ceil(x), ceil(y)))
        coordinates.append(coordinates[0])
        return coordinates

    def draw_line(self, coordinates):
        color = (124, 252, 0)
        for coordinate in coordinates:
            self.screen.set_at(coordinate, color)

    def main_loop(self):
        """ Run the app """
        running = True
        count = 0

        pygame.display.flip()
        n = input('Please enter number of vertices for the polygon:\n')
        polygon = self.get_polygon_coordinates(int(n), r=150)

        for i in range(0, len(polygon) - 1):
            points = get_coordinates(polygon[i], polygon[i + 1])
            self.draw_line(points)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                """
                Drawing a line with mouse clicks.
                """
                """
                if event.type == pygame.MOUSEBUTTONUP:
                    if count == 0:
                        pos1 = pygame.mouse.get_pos()
                        count += 1
                    else:
                        pos2 = pygame.mouse.get_pos()
                        coordinates = get_coordinates(pos1, pos2)
                        self.draw_line(coordinates)
                        count = 0
                """

                pygame.display.flip()

    @staticmethod
    def quit():
        """ cleanup the app, run exit code """
        pygame.quit()


if __name__ == "__main__":
    myApp = App()
