# Enemies (Part 3)

For this last part of **Enemies**, we'll be letting the enemies appear from the top and bottom as well. The changes to the code is very much like what we did in **part 2 of Enemies**, and you might have already figured it out yourself.

Try working out this part on your own. When you're ready, you can test it out to see if it works, then compare it with my code below. Don't worry if your code isn't exactly the same as mine; there are many ways to solve this challenge, and you may have simply found a different way. Test out the code to make sure it's working correctly.

## At this point...

Right now your code should look like this (new and modified lines are highlighted in yellow)...

```python hl_lines="26 37 38 39 40 41 42 43 44 53 54 55 56 58"
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

background = Actor('water')

player = Actor('p1_front')
player.x = 400
player.y = 300

enemies = []

def update():
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
    
def draw():
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()

pgzrun.go()
```