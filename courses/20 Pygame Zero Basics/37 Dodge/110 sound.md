# Sound and Music

We have previously added two sound files to our **sounds** folder; **footsteps** and **sneakingaround**. We'll play the second sound at the beginning of the program, and the first sound everytime our character moves.

## Background Music

Playing the background music is easy, we'll use the command...

```python
sounds.sneakingaround.play(-1)
```

**sounds** : This means to use the sounds object that is provided by Pygame Zero.

**sneakingaround** : This is the name of my sound file. You may have a different filename, so change this accordingly. You don't need to include the file extension.

**play(-1)** : This tells it to repeat the sound forever. You can also use ```play()``` if you want it to play only once.

This line should be outside of any functions. We want it to start playing at the start of the game, and repeat forever.

## Footsteps

The footstep sound is a little more tricky. We want it to play only if these two conditions are met...

1. Player is moving
2. Footstep sound isn't already playing

We can fulfill the first condition by modifying the movement code into this...

```python
play_walking_sound = False
if keyboard.up:
    player.y -= 5
    play_walking_sound = True
if keyboard.down:
    player.y += 5
    play_walking_sound = True
if keyboard.left:
    player.x -= 5
    play_walking_sound = True
if keyboard.right:
    player.x += 5
    play_walking_sound = True
```

Now we can check if **play_walking_sound** is true. It will be true if the player has pressed any of the arrow keys.

For the second condition, we can use the **get_num_channels()** function of the sound. This will tell us how many channels it is playing on. If it is not playing at all, this value will be zero. Now we can combine both conditions together...

```python
if play_walking_sound:
    if sounds.footsteps.get_num_channels() == 0:
        sounds.footsteps.play()
```

## Completed Code

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="18 28 31 34 37 40 42 43 44"
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

sounds.sneakingaround.play(-1)

def update():
    global score, game_over
    
    if game_over:
        return

    score += 1 / 60
    
    play_walking_sound = False
    if keyboard.up:
        player.y -= 5
        play_walking_sound = True
    if keyboard.down:
        player.y += 5
        play_walking_sound = True
    if keyboard.left:
        player.x -= 5
        play_walking_sound = True
    if keyboard.right:
        player.x += 5
        play_walking_sound = True

    if play_walking_sound:
        if sounds.footsteps.get_num_channels() == 0:
            sounds.footsteps.play()

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