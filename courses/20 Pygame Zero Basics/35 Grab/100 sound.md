# Sound and Music

So far, we have not used any sound or music in our game. Let's add some in.

We have previously added two sound files to our **sounds** folder; **sfx_coin_single1** and **sfx_sounds_fanfare1**. We'll play the first sound when we pick up a coin.

## How to Play Sound

Playing a sound is easy, we'll use the command...

```python
sounds.sfx_coin_single1.play()
```

```sounds``` : This means to use the sounds object that is provided by Pygame Zero.

```sfx_coin_single1``` : This is the name of my sound file. You may have a different filename, so change this accordingly. You don't need to include the file extension.

```play()``` : This tells it to play once. If you provide a number in the parameter (eg. ```play(3)```), it will repeat the sound for that number of times. You can also use ```play(-1)``` if you want it to repeat forever.

## When to Play Sound

We want to play the coin sound whenever we touch a coin. So add it under the **if** statement where we check if the player is colliding with the coin.

```python hl_lines="5"
if player.colliderect(coin):
    coin.x = random.randint(0, 800)
    coin.y = random.randint(0, 600)
    score += 1
    sounds.sfx_coin_single1.play()
```

## Completed Code

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="42"
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
        sounds.sfx_coin_single1.play()

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