Background
===
To draw the background, we create a new actor using the background image.

```
background = Actor('grass')
```

...and remember to **draw** it inside the **draw()** function.

```
background.draw()
```
Remember I told you not to change the width and height of the game window? That's because our background image is 800 pixels by 600 pixels. If you had changed the game window size, you'll need a different background image that will fit the size you choose.

Your full program should now look like this...

```
import pgzrun

WIDTH=800
HEIGHT=600

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

background = Actor('grass')

def update():
    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
        tank.angle = 90
    elif keyboard.down:
        tank.y = tank.y + 2
        tank.angle = 270

def draw():
    screen.fill((0,0,0))
    background.draw()
    tank.draw()

pgzrun.go() # Must be last line
```

The **screen.fill((0,0,0))** that we added earlier was to erase the screen by covering the entire window in black. But since our background image now fills the entire screen, we don't need the **screen.fill** anymore. You can remove that line.