# PyTextBox
A little module for creating text boxes in Pygame and Python 2.7

Requires pygame (obviously)

https://benedsmith.wordpress.com/

# Documentation

####Import the module
```python
Import TextBox 
```
####Create a textbox object
```python
textbox1 = TextBox.TextBox(rect, text, background_colour, text_colour, font, font_size)
```
The rect - (x, y, width, height) 
Note: x and y are the top left corner of the textbox. Set to (0, 0, 400, 25) as default.

##In the Pygame event loop:

####This bit of code handles keyboard input
```python  
  if event.type == pygame.KEYDOWN:
    if textbox1.active == True:
       textbox1.text_input(event)
```
####This tests if the textbox has been clicked
```python
  textbox1.test_collide(event)
```
##In the Pygame main loop:

####Draw your textbox, after screen.fill and before display.flip
```python
textbox1.draw(textbox1.text, screen)
```
