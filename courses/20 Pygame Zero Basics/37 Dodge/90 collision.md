# Collision

In **Dodge the Creep**, the game ends if you touch any enemy. So to keep track of whether the game is over, we'll create a new variable...

```python
game_over = False
```

We're calling this variable **game_over** and we'll set it to **False** at the start of the game.

## List Collide

Since we have a list of enemies that we can collide against, we can use the **collidelist** function to check if the player is colliding with any of them.

If the player collided with an enemy, **collidelist** will return the index of this enemy. For example, if the player collided with the first enemy, **collidelist** will return the value 0.

If the player didn't collide with any of the enemies in the list, **collidelist** will return -1. If the return value is **not** -1, it means that there is a collision.

```python
if player.collidelist(enemies) != -1:
    game_over = True
```

This is what the above code is saying: "If the player collided with an enemy, set game_over to True".

Don't forget to declare that **game_over** is a global variable.

```python
global game_over
```

## Drawing Game Over message

If the game is over, we'll clear the screen and draw the words "Game Over" for now.

```python
if game_over:
    screen.clear()
    screen.draw.text('Game Over', (350,270), color=(255,255,255), fontsize=30)
```

## Testing it out

If your game in written correctly, you should now get a "Game Over" message when you touch any one of the enemy. Test it out and make sure it is working correctly.

## At this point...

Right now your code should look like this (new and modified lines are highlighted in yellow)...

```python hl_lines="7 18 65 66 69 70 71 72"
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

game_over = False

background = Actor('water')

player = Actor('p1_front')
player.x = 400
player.y = 300

enemies = []

def update():
    global game_over
    
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
    else:
        background.draw()
        player.draw()
        for enemy in enemies:
            enemy.draw()

pgzrun.go()

```