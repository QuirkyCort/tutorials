Keeping Score
===
We can track the score easily using a variable. Let's add a variable named ```score``` and give it the value of 0 at the start of the program.

```
score = 0
```

Now everytime the spaceship catches the gem, we'll increase ```score``` by 1.

```
if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1
```

If you try out this program, you'll get an error...

```
UnboundLocalError: local variable 'score' referenced before assignment
```

That's because the ```score``` variable is declared outside of the ```update()``` function, but we are trying to write it from inside the ```update()``` function. In Python, we can read variables that are outside a function (...these are called global variables), but cannot write to them unless we declare them as global inside the function.

```
global score
```

After this change, your ```update()``` function should now look like this...

```
def update():
    global score
    
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
        score = score + 1
```

Displaying Score
===
To display the score, we will use the ```screen.draw.text()``` function.

```
screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
```

The parameters are...

```'Score: ' + str(score)``` : This is the string that we want to draw.

```(15,10)``` : This is the position to draw; x=15 and y=10.

```color=(255,255,255)``` : This is the color of the text, in this case, it is white

```fontsize=30``` : The size of the font.

Like all the other drawing functions, we'll need to put this inside the ```draw()``` function. After this is done, your program should look like this...

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

score = 0

def update():
    global score

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
        score = score + 1

def draw():
    screen.fill((80,0,70))
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line

```
