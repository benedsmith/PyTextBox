import pygame
pygame.init()
pygame.font.init()

class TextBox(object):
    def __init__(self, rect=None, text=[], bgcolour=(222,222,222), text_colour=(0,0,0), font=None):
        if rect is None:
            self.rect = pygame.Rect(0,0,400,25)
        else:
            self.rect = pygame.Rect(rect)

        self.text = text
        self.bgcolour = bgcolour
        self.text_colour = text_colour

        self.active = False

        if font is None:
            self.font = pygame.font.Font(None, 25)
        else:
            self.font = font

    def draw(self, message, screen):
        pygame.draw.rect(screen,self.bgcolour,self.rect, 0)
        if len(message) > 0:
            screen.blit(self.font.render("".join(message), True, self.text_colour), (self.rect.left+10, self.rect.top))
        pygame.display.flip()

    def text_input(self, event):
        key_input = event.key
        if key_input == pygame.K_BACKSPACE:
            if len(self.text) > 0:
                self.text.pop()
        elif key_input == pygame.K_RETURN:
            self.active = False
            self.bgcolour = (222,222,222)
        elif key_input <= 127:
            self.text.append(chr(key_input))

    def test_collide(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            print "click!"
            self.active = True
            self.bgcolour = (128,128,128)
