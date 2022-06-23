Adding a Gem
===
The game won't be called "Gem Catcher" without a gem! We can add in a gem the same way we added the spaceship.

First, add a gem image to the **images** folder. I'm using this one...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/gemgreen.png)

Next, add a new gem **Actor**...

```python
gem = Actor('gemgreen')
gem.x = 350
gem.y = 0
```

Setting x to 350 will place it roughly in the middle horizontally, while setting y to 0 will place it at the top. Don't forget to also draw the gem in the ```draw()``` function.

```python
gem.draw()
```

Your program should now look like this...

```python hl_lines="10 11 12 22"
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = 350
gem.y = 0

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5
        
def draw():
    screen.fill((80,0,70))
    gem.draw()
    ship.draw()

pgzrun.go() # Must be last line
```

Moving the Gem
===
Previously, we have written code in the ```update()``` function to make the ship move by changing its x position when the left or right key is pressed. For the gem, we'll make it move continuously downwards by changing the y position.

```python
gem.y = gem.y + 4
```

We also want the gem to return to the top when it reaches the bottom. To do that, we'll set the y position to 0 (top), when it exceeds 600 (bottom most position).

```python
if gem.y > 600:
    gem.y = 0
```

Add that into your program!

```python hl_lines="20 21 22"
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = 350
gem.y = 0

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 4
    if gem.y > 600:
        gem.y = 0
        
def draw():
    screen.fill((80,0,70))
    gem.draw()
    ship.draw()

pgzrun.go() # Must be last line
```
