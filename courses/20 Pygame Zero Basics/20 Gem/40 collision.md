Collision
===
We also want the gem to go back to the top if it touches the spaceship. If you had done Scratch before, you might remember the ```if touching sprite``` command. In Pygame Zero, we'll use ```if gem.colliderect(ship):``` or ```if ship.colliderect(gem):``` (...both works the same).

```
if gem.colliderect(ship):
    gem.y = 0
```

...or...

```
if ship.colliderect(gem):
    gem.y = 0
```

**Try it out!**

Random
===
It's not vey interesting to have the gem fall from the same spot everytime. In [Introduction to Python](https://trinket.io/aposteriori/courses/introduction-to-python#/fundamentals-loops/turtle-graphics), you learned to use the ```random``` module. We'll use it here to randomize the x position of the gem.

Before we can use the ```random``` module, we'll need to import it.

```
import random
```

To assign a random x position, we use...

```
gem.x = random.randint(20, 780)
```

The ```random.randint(20, 780)``` function will provide a random number between 20 to 780. This should be added whenever we return the gem to the top of the screen.

Your program should look like this now.

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 4
    if gem.y > 600:
        gem.x = random.randint(20, 780)
        gem.y = 0
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        
def draw():
    screen.fill((80,0,70))
    gem.draw()
    ship.draw()

pgzrun.go() # Must be last line
```