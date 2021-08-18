Moving the Ship
===
First, we'll create the ship actor...

```
player = Actor('player_ship')
```
**If you used a different filename, you'll need to change the 'player_ship' part.**

...then we create the **draw()** function, and add in a draw command for the player.

```
def draw():
    player.draw()
```
With that done, your program should now look like this...
```
import pgzrun

WIDTH=800
HEIGHT=600

player = Actor('player_ship')

def draw():
    player.draw()

pgzrun.go() # Must be last line
```
Run it, and you should see your ship on screen.

Position the ship
===
Now, let's have our ship start at the bottom center of the screen.

Remember that to move the actor downwards, we need to increase y. The width of the screen is 800, so to put it in the center, we should set x to 400.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/xy.png)

Add in the following to your program. It should appear right after the line where you created the tank actor.

```
player.x = 400
player.y = 500
```

That will set the starting position of the ship somewhere near the center bottom of the screen.

Moving the Ship
===
Remember how we moved the spaceship in Gem Catcher? We used **keyboard.left** and **keyboard.right** to detect if those keys are pressed.

```
def update():
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x -= 5
```

Here I'm using a shortform....

```
player.x += 5
```

This is the same as writing...

```
player.x = player.x + 5
```

You can also write...

```
player.x -= 5
```

...which is the same as writing...

```
player.x = player.x - 5
```

To detect up and down, we can use **keyboard.up** and **keyboard.down**. For the full list of keys you can use, you can refer to the [Pygame Zero documentations](https://pygame-zero.readthedocs.io/en/stable/hooks.html#buttons-and-keys).

To move left and right, we changed **x**. To move up and down, we should change **y**.

```
def update():
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x -= 5
```

Limiting the Movement
===
Right now, your ship should be able to move in all directions (...test it out!), but it can also move too far and exit the screen.
To prevent this, we should prevent the x and y from getting too large or too small using a new set of **"if"** conditions.

```
if player.x < 25:
    player.x = 25
if player.x > 775:
    player.x = 775
```

These will force the x position to stay between 25 to 775.
Why didn't I use 0 to 800?
Try it out and see the effect.
The best values to use will be different for everyone, so you'll likely need to tune this.

The above code only limits the x position.
What about y?
Try and implement it yourself.

At this point...
===

At the end of these, your program should look like this...

```
import pgzrun

WIDTH=800
HEIGHT=600

player = Actor('player')
player.x = 400
player.y = 500

def update():
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x -= 5

    if player.x < 25:
        player.x = 25
    if player.x > 775:
        player.x = 775
    if player.y < 30:
        player.y = 30
    if player.y > 570:
        player.y = 570

def draw():
    screen.clear()
    player.draw()

pgzrun.go() # Must be last line
```