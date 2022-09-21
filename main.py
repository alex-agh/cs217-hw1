import pygame
from bresenham import get_coordinates
from polygon import Polygon
from math import pi

clock = pygame.time.Clock()


class App:
    def __init__(self):
        self.background_colour = (0, 0, 0)
        (width, height) = (800, 600)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Draw Polygon')
        self.screen.fill(self.background_colour)
        self.main_loop()

    def draw_line(self, coordinates):
        """Change the color of points on screen."""
        color = (255, 255, 255)
        for coordinate in coordinates:
            self.screen.set_at(coordinate, color)

    def draw_polygon(self, polygon):
        for edge in polygon.edges:
            coordinates = get_coordinates(edge[0], edge[1])
            self.draw_line(coordinates)

    def transform(self, polygon, increment, t):
        if t == 's' or t == 'd':
            polygon.scale(increment)
        if t == 't':
            polygon.counter_clockwise(increment)
        if t == 'r':
            polygon.clockwise(increment)
        self.screen.fill(self.background_colour)
        self.draw_polygon(polygon)

    def main_loop(self):
        """ Run the app """
        running = True

        pygame.display.flip()
        """Enter number of points for the polygon in the CONSOLE!"""
        n = input('Please enter number of vertices for the polygon:\n')
        polygon = Polygon(
            150, int(n), int(self.screen.get_width() / 2), int(self.screen.get_height() / 2)
        )
        self.draw_polygon(polygon)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.transform(polygon, 0.05, 's')
                    if event.key == pygame.K_d:
                        self.transform(polygon, -0.05, 'd')
                    if event.key == pygame.K_t:
                        self.transform(polygon, pi/10, 't')
                    if event.key == pygame.K_r:
                        self.transform(polygon, pi/10, 'r')
                if event.type == pygame.QUIT:
                    running = False
                pygame.display.flip()

    @staticmethod
    def quit():
        """ cleanup the app, run exit code """
        pygame.quit()


if __name__ == "__main__":
    myApp = App()
