import pygame
from bresenham import get_coordinates
from polygon import Polygon


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

    def main_loop(self):
        """ Run the app """
        running = True

        pygame.display.flip()
        n = input('Please enter number of vertices for the polygon:\n')
        polygon = Polygon(150, int(n), 400, 300)
        for edge in polygon.edges:
            coordinates = get_coordinates(edge[0], edge[1])
            self.draw_line(coordinates)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pygame.display.flip()

    @staticmethod
    def quit():
        """ cleanup the app, run exit code """
        pygame.quit()


if __name__ == "__main__":
    myApp = App()
