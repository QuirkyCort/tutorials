# Ending the Game

We'll know that the time is up when **timer** is less than or equal to zero. When that happens, we'll need to do two things...

1. Display the words "Game Over" and "Your score is XXX".
2. Stop the player from moving.

### 1) Display "Game Over"

In **draw()**, we'll check if **timer** is less than or equal to zero. If it is, we'll clear the screen and draw the game over message. If it is not, we'll draw everything else.

```python
def draw():
    if timer <= 0:
        screen.clear()
        screen.draw.text('Game Over', (350,270), color=(255,255,255), fontsize=30)
        screen.draw.text('Score: ' + str(score), (350,330), color=(255,255,255), fontsize=30)
    else:
        background.draw()
        player.draw()
        coin.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Time: ' + str(round(timer, 2)), (330,10), color=(255,255,255), fontsize=30)
```

### 2) Stop player movement

To stop the player movement, we can simply skip all the code in the **update()** function. When inside a function, we can immediately end the function and skip all the remaining lines by using the **return** command.

We'll check if **timer** is less than or equal to zero. If it is, we'll run the **return** command and skip everything else.

```python
if timer <= 0:
    return
```

## At this point...

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="24 25 44 45 46 47 48"
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

background = Actor('grass')

player = Actor('p3_front')
player.x = 400
player.y = 300

coin = Actor('coingold')
coin.x = random.randint(0, 800)
coin.y = random.randint(0, 600)

score = 0
timer = 10

def update():
    global score
    global timer

    if timer <= 0:
        return

    timer -= 1 / 60
    
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    if player.colliderect(coin):
        coin.x = random.randint(0, 800)
        coin.y = random.randint(0, 600)
        score += 1

def draw():
    if timer <= 0:
        screen.clear()
        screen.draw.text('Game Over', (350,270), color=(255,255,255), fontsize=30)
        screen.draw.text('Score: ' + str(score), (350,330), color=(255,255,255), fontsize=30)
    else:
        background.draw()
        player.draw()
        coin.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Time: ' + str(round(timer, 2)), (330,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line

```