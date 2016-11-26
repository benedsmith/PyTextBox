# PyTextBox
A little module for creating text boxes in Pygame and Python 2.7

# Documentation

####Import the module
```python
Import TextBox 
```
####Create a textbox object
```python
textbox1 = TextBox.TextBox(rect, text, bgcolour, text_colour, font)
```
The rect - (x, y, width, height) 
Note: x and y are the top left corner of the textbox. Set to (0, 0, 400, 25) as default.

##In the Pygame event loop:

####This bit of code handles keyboard input
```python  
  if event.type == pygame.KEYDOWN:
    if text.active == True:
       textbox1.text_input(event)
```
####This tests if the textbox has been clicked
```python
  text.test_collide(event)
```
##In the Pygame main loop:

####Draw your textbox, after screen.fill and before display.flip
```python
textbox1.draw(textbox1.text, screen)
```
