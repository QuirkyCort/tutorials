Game Over
===
It's not much fun to play a game that you cannot lose. So let's add in a **game over** condition. If the gem touches the bottom of the screen, we'll end the game.

First, add in a new variable called ```game_over``` and set it to ```False```.

```python
game_over = False
```

Inside the ```update()``` function, look for these lines...

```python
if gem.y > 600:
    gem.x = random.randint(20, 780)
    gem.y = 0
```

...and change them to these...

```python hl_lines="2"
if gem.y > 600:
    game_over = True
```

This will set the ```game_over``` variable to ```True``` if the gem touches the bottom of the screen.

You will also need to add ```global game_over``` to the top of the ```update()``` function. Do you remember why? If you can't, refer back to the [keeping score page](https://trinket.io/aposteriori/courses/game-development-with-pygame-zero#/gem-catcher/keeping-score).

Inside the ```draw()``` function, change these lines...

```python
screen.fill((80,0,70))
gem.draw()
ship.draw()
screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
```

...into these (watch out for the indents)...

```python hl_lines="2 3 4 5"
screen.fill((80,0,70))
if game_over:
    screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
    screen.draw.text('Final Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
```

This will make it draw the **game over** text when the ```game_over``` variable is ```True```, otherwise it will draw the gem and the ship as before.

Your final program should look like this...

```python hl_lines="16 22 31 39 40 41 42"
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
game_over = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def update():
    global score, game_over
    
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        game_over = True
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1
        
def draw():
    screen.fill((80,0,70))
    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line
```