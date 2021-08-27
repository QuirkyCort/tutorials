# Score

To keep track of the score, we'll start by creating a new variable and start it at zero. This is a **global variable** so make sure to put it outside of the **update()** and **draw()** functions.

```python
score = 0
```

We want our score to increase by 1 every second. Since **update()** runs 60 times per second, we'll add 1 / 60 of a point to the score each time **update()** runs.

```python
score += 1 / 60
```

...and don't forget to declare **score** as a global.


```python
global score
```

## Display the score

To display the score, we will use the ```screen.draw.text()``` function.

```python
screen.draw.text('Score: ' + str(round(score)), (15,10), color=(255,255,255), fontsize=30)
```

The parameters are...

```'Score: ' + str(round(score))``` : This is the string that we want to draw. We round it off as we want to display a whole number.

```(15,10)``` : This is the position to draw; x=15 and y=10.

```color=(255,255,255)``` : This is the color of the text, in this case, it is white

```fontsize=30``` : The size of the font.

Like all the other drawing functions, we'll need to put this inside the ```draw()``` function.

We'll also need to draw the score when the game is over; it'll be the same as the above, but in a different x and y position.

## Stopping Controls

When the game is over, we want to stop the players and animals from moving. As before, we can do this easily by calling the **return** function inside **update()**

```python
if game_over:
    return
```

Put this near the top of the **update()** function. If will immediate end the **update()** function and skip all the code below it if **game_over** is **True**.

## At this point...

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="7 19 21 22 71 72 75 76 77 78 79 84"
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

game_over = False
score = 0

background = Actor('water')

player = Actor('p1_front')
player.x = 400
player.y = 300

enemies = []

def update():
    global score, game_over
    
    if game_over:
        return

    score += 1 / 60
    
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    if random.randint(0, 60) == 0:
        side = random.randint(1, 4)
        enemy = Actor('worm.png')

        if side == 1:
            enemy.y = random.randint(0, 600)
            enemy.x = 850
            enemy.angle = 0
        elif side == 2:
            enemy.y = random.randint(0, 600)
            enemy.x = -50
            enemy.angle = 180
        elif side == 3:
            enemy.y = 650
            enemy.x = random.randint(0, 800)
            enemy.angle = 270
        elif side == 4:
            enemy.y = -50
            enemy.x = random.randint(0, 800)
            enemy.angle = 90

        enemies.append(enemy)

    for enemy in enemies:
        if enemy.angle == 0:
            enemy.x -= 3
        elif enemy.angle == 180:
            enemy.x += 3
        elif enemy.angle == 270:
            enemy.y -= 3
        elif enemy.angle == 90:
            enemy.y += 3

        if enemy.x < -50 or enemy.x > 850 or enemy.y < -50 or enemy.y > 650:
            enemies.remove(enemy)

    if player.collidelist(enemies) != -1:
        game_over = True
    
def draw():
    if game_over:
        screen.clear()
        screen.draw.text('Game Over', (350,270), color=(255,255,255), fontsize=30)
        screen.draw.text('Score: ' + str(round(score)), (350,330), color=(255,255,255), fontsize=30)
    else:
        background.draw()
        player.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text('Score: ' + str(round(score)), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go()
```

You should now see the score increase every second.