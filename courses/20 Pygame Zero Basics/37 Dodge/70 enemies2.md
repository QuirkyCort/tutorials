# Enemies (Part 2)

Right now, our enemies only come from the right. In this section, we will modify the code so that the enemies can come from either left or right.

Look for this code in your program, we'll be making some changes to it.

```python
if random.randint(0, 60) == 0:
    enemy = Actor('worm.png')
    enemy.y = random.randint(0, 600)
    enemy.x = 850
    enemies.append(enemy)
```

As long as the **if** condition is true, we'll be creating an new enemy, so the ```enemy = Actor('worm.png')``` can remain unchanged.

Next, we'll pick a random number from 1 to 2, and store it in a variable **side**. This random number will represent which side the enemy should appear from.

```python
if random.randint(0, 60) == 0:
    enemy = Actor('worm.png')
    side = random.randint(1, 2)
```

If the random number is a 1, we'll make the enemy appear on the right. If it's a 2, we'll make it appear on the left. We will also need to rotate the enemy by setting the angle, so that it is facing the right direction.

```python
if side == 1:
    enemy.y = random.randint(0, 600)
    enemy.x = 850
    enemy.angle = 0
elif side == 2:
    enemy.y = random.randint(0, 600)
    enemy.x = -50
    enemy.angle = 180
```

**IMPORTANT** This set of **if** should be inside the earlier set of **if**. Make sure the indentations are correct.

Next, we'll add the enemy to the list of enemies. This is the same as before.

```python
enemies.append(enemy)
```

## Move the enemies

Since the enemy can appear on the right or left, the direction of movement will not be the same. We'll check the angle to decide which way to move.

```python
for enemy in enemies:
    if enemy.angle == 0:
        enemy.x -= 3
    elif enemy.angle == 180:
        enemy.x += 3
```

If the angle is 0 (...enemy starts from the right side), we'll decrease the x position (...move it to the left). If the angle is 180 (...enemy starts from the left side), we'll increase the x position (...move it to the right).

## Remove the enemy

Now the enemy may leave the screen from the left or right side. We'll need to check for both when removing the enemy.

```python
if enemy.x < -50 or enemy.x > 850:
    enemies.remove(enemy)
```

## At this point...

Right now your code should look like this (new and modified lines are highlighted in yellow)...

```python hl_lines="27 29 32 33 34 35 36 41 43 44 46"
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
        enemy = Actor('worm.png')
        side = random.randint(1, 2)

        if side == 1:
            enemy.y = random.randint(0, 600)
            enemy.x = 850
            enemy.angle = 0
        elif side == 2:
            enemy.y = random.randint(0, 600)
            enemy.x = -50
            enemy.angle = 180

        enemies.append(enemy)

    for enemy in enemies:
        if enemy.angle == 0:
            enemy.x -= 3
        elif enemy.angle == 180:
            enemy.x += 3

        if enemy.x < -50 or enemy.x > 850:
            enemies.remove(enemy)
    
def draw():
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()

pgzrun.go()
```