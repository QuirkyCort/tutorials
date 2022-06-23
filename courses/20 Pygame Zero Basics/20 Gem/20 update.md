update()
===
Earlier, we created the ```draw()``` function. This is a special function that Pygame Zero runs regularly to draw what you see on the screen. Another special function is ```update()```. Pygame Zero will regularly run our ```update()``` function to update the position of the various actors in the game.

Let's add in the ```update()``` function and program it to react to keypresses.

```python hl_lines="10 11 12 13 14"
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

def draw():
    ship.draw()

pgzrun.go() # Must be last line
```

Whenever Pygame Zero runs our ```update()``` function, we will check if the **left key** is pressed. If it is, we'll **reduce** the **x position** by **5**. If the **right key** is pressed, we'll **increase** the **x position** by **5**.

Try out the program! Write it in **IDLE** and run it using **F5** or **Run -> Run Module**. Did that work the way you expected?

Clearing Screen
===
If you tried the previous program, you should have gotten something funky like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/funky.png)

That's because we told Pygame Zero to update the ship's position and draw it to screen, but we didn't tell it to erase what was drawn before!

To erase the screen, we'll fill the entire screen with a single color. We'll do this in the ```draw()``` function, using...

```python
screen.fill((80,0,70))
```

The ```(80,0,70)``` is a **tuple** (...a tuple is like a list, but it cannot be changed) representing the color.  The first number (80) is for red, the second number (0) is for green, and the last number (70) is for blue. The largest allowable value for each color is 255 and the smallest is 0. **Try different numbers  and see what color you get!**

Your progam should now look like this...

```python hl_lines="17"
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5
        
def draw():
    screen.fill((80,0,70))
    ship.draw()

pgzrun.go() # Must be last line
```
