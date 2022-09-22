import pygame
from bresenham import get_coordinates
from polygon import Polygon
from math import pi

clock = pygame.time.Clock()


class App:
    def __init__(self):
        self.background_colour = (16, 24, 32)
        (width, height) = (800, 600)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Draw Polygon')
        self.screen.fill(self.background_colour)
        self.main_loop()

    def draw_line(self, coordinates):
        """Change the color of points on screen."""
        color = (254, 231, 21)
        for coordinate in coordinates:
            self.screen.set_at(coordinate, color)

    def draw_polygon(self, polygon):
        for edge in polygon.edges:
            coordinates = get_coordinates(edge[0], edge[1])
            self.draw_line(coordinates)

    def update(self, obj):
        self.screen.fill(self.background_colour)
        self.draw_polygon(obj)
        pygame.display.update()

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
                        polygon.scale(0.05)
                        self.update(polygon)
                    if event.key == pygame.K_d:
                        polygon.scale(-0.05)
                        self.update(polygon)
                    if event.key == pygame.K_t:
                        polygon.counter_clockwise(pi/10)
                        self.update(polygon)
                    if event.key == pygame.K_r:
                        polygon.clockwise(pi/10)
                        self.update(polygon)
                    if event.key == pygame.K_RIGHT:
                        polygon.move(15)
                        self.update(polygon)
                    if event.key == pygame.K_LEFT:
                        polygon.move(-15)
                        self.update(polygon)
                    if event.key == pygame.K_DOWN:
                        polygon.move(15, 1)
                        self.update(polygon)
                    if event.key == pygame.K_UP:
                        polygon.move(-15, 1)
                        self.update(polygon)
                if event.type == pygame.QUIT:
                    running = False
                pygame.display.flip()

    @staticmethod
    def quit():
        """ cleanup the app, run exit code """
        pygame.quit()


if __name__ == "__main__":
    myApp = App()
