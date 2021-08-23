# Moving the Player

To move the player, we'll check if any of the arrow keys are pressed, and change the player's **x** and **y** value.

**x** : Controls the left-right position of the player.

**y** : Controls the up-down position of the player.

Code for controls should be in the **update()** function, so let's create the function and add in the code.

```python
def update():
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
```

```def update():``` : Starts the **update()** function. Every indented line under it is part of this function.

```if keyboard.up:``` : This means "if the up arrow key is pressed", run the code that is indented under this line.

```player.y -= 5``` : Subtract 5 from **player.y**. This moves the player upwards. Note that this is indented under ```if keyboard.up:```, so it will only run if the up arrow is pressed.

## At this point...

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="12 13 14 15 16 17 18 19 20"
import pgzrun

WIDTH = 800
HEIGHT = 600

background = Actor('grass')

player = Actor('p3_front')
player.x = 400
player.y = 300

def update():
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

def draw():
    background.draw()
    player.draw()

pgzrun.go() # Must be last line

```

Your game should look the same as before, but you should be able to move the player using the arrow keys on your keyboard. Test and make sure it's working correctly!