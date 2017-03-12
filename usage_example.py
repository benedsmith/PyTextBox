import pygame
import TextBox

pygame.init()

width, height = 800, 700
screen = pygame.display.set_mode((width, height))

textbox1 = TextBox.TextBox((0, 0, 100, 35))
textbox2 = TextBox.TextBox((0, 50, 100, 35))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if textbox1.active:
                textbox1.text_input(event)
            if textbox2.active:
                textbox2.text_input(event)
        textbox1.test_collide(event)
        textbox2.test_collide(event)

    screen.fill((0, 0, 0))
    textbox1.draw(textbox1.text, screen)
    textbox2.draw(textbox2.text, screen)
    pygame.display.flip()
    clock.tick(60)
