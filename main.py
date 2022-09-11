import pygame
from bresenham import Bresenham


class App:
    def __init__(self):
        self.background_colour = (229, 255, 255)
        (width, height) = (800, 600)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Draw Line')
        self.screen.fill(self.background_colour)
        self.main_loop()

    def main_loop(self):
        """ Run the app """
        running = True
        count = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    color = (24, 28, 28)
                    if count == 0:
                        pos1 = pygame.mouse.get_pos()
                        count += 1
                    else:
                        pos2 = pygame.mouse.get_pos()
                        bresenham = Bresenham(pos1[0], pos1[1], pos2[0], pos2[1])
                        coordinates = bresenham.get_coordinates()
                        for coordinate in coordinates:
                            self.screen.set_at(coordinate, color)
                        count = 0
                pygame.display.flip()

    @staticmethod
    def quit():
        """ cleanup the app, run exit code """
        pygame.quit()


if __name__ == "__main__":
    myApp = App()
