import pygame
pygame.init()
pygame.font.init()


class TextBox(object):
    def __init__(self, rect=None, text="", background_colour=(222, 222, 222), text_colour=(0, 0, 0), font="Arial",
                 font_size=14):
        # If no rectangle is specified, then a default one is chosen
        if rect is None:
            self.rect = pygame.Rect(0, 0, 400, 25)
        else:
            self.rect = pygame.Rect(rect)

        # Set the options (defaults if not specified by user)
        self.text = text
        self.background_colour = background_colour
        self.text_colour = text_colour
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        # Set the default state to False
        self.active = False

    def draw(self, message, screen):
        # Draw the box
        pygame.draw.rect(screen, self.background_colour, self.rect, 0)
        # If there is a message, render it and draw it over the box. Update the display.
        if len(message) > 0:
            screen.blit(self.font.render(("".join(message)), True, self.text_colour),
                        (self.rect.left+10, self.rect.top+(self.font_size/2)))

    def text_input(self, event):
        # Grab the pressed key, do the relevant process with it
        key_input = event.key
        if key_input == pygame.K_BACKSPACE:
            if len(self.text) > 0:
                self.text = self.text[:-1]
        elif key_input == pygame.K_RETURN:
            self.active = False
            self.background_colour = (222, 222, 222)
        elif key_input <= 127:
            self.text += chr(key_input)

    def test_collide(self,event):
        # Check to see if the box gets clicked, set true and  change colour
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.active = True
            self.background_colour = (128, 128, 128)
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
            self.active = False
            self.background_colour = (222, 222, 222)
