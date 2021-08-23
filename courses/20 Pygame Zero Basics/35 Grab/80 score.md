# Score

To keep track of the score, we'll start by creating a new variable and start it at zero. This is a **global variable** so make sure to put it outside of the **update()** and **draw()** functions.

```python
score = 0
```

We'll increase it by one everytime we touch the coin...

```python
score += 1
```

**IMPORTANT!** We should only increase the score if we touch the coin, so make sure to put the above code indented under ```if player.colliderect(coin):```.

If you try to run this now, it will give you an error. That's because **score** is a global variable, and we are trying to change it inside the **update()** function. Whenever we want to change a global variable inside a function, we need to add...

```python
global score
```

...to the top of the function.

## Display the score

To display the score, we will use the ```screen.draw.text()``` function.

```python
screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
```

The parameters are...

```'Score: ' + str(score)``` : This is the string that we want to draw.

```(15,10)``` : This is the position to draw; x=15 and y=10.

```color=(255,255,255)``` : This is the color of the text, in this case, it is white

```fontsize=30``` : The size of the font.

Like all the other drawing functions, we'll need to put this inside the ```draw()``` function.

## At this point...

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="17 20 34 40"
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

def update():
    global score
    
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
    background.draw()
    player.draw()
    coin.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line
```

You should now see the score increase everytime you touch the coin.