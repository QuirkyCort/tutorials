# Enemies (Part 1)

The earlier part of this game is largely identical to **Grab the Coin**, but here's where things starts to get different.

In **Grab the Coin**, we only have one coin appearing at a time, but in **Dodge the Creep**, we will be having many enemies appear on screen. To handle this, we'll need to put the enemies inside a list.

```python
enemies = []
```

This creates an empty list of enemies. In the rest of this section, we'll be doing four things...

1. Randomly create an enemy on the right side of the screen.
2. Make the enemy move towards the left.
3. Remove the enemy if it exits the left side of the screen.
4. Draw the enemy.

## Create the enemy

For part 1 of **Enemies**, our enemies will only appear on the right side of the screen, but they will appear at random time and at a random y position (up-down).

```python
if random.randint(0, 60) == 0:
    enemy = Actor('worm.png')
    enemy.y = random.randint(0, 600)
    enemy.x = 850
    enemies.append(enemy)
```

In the first line ```if random.randint(0, 60) == 0:```, we pick a random number from 0 to 60. If the random number happens to be a "0", we'll continue on to create a new enemy.

In ```enemy.y = random.randint(0, 600)```, we set the y position of the newly created enemy to a random number between 0 to 600. This will give it a random up-down position. For the x position, we set it to 850, which is just outside the right edge of our screen (...which has a width of 800).

Finally, the ```enemies.append(enemy)``` adds the newly created enemy to the list of enemies.

## Move the enemies

To move the enemy, we just have to change the x position. But since there are many enemies, we'll need a **for** loop to go through the entire list and change each enemy one-by-one.

```python
for enemy in enemies:
    enemy.x -= 3
```

## Remove the enemy

If we don't remove the enemy, it will keep on acculumulating in the **enemies** list. While this may not be a problem for a short game, what if you manage to stay alive in the game for hours? You could end up with thousands of enemies, and almost all of them are outside the screen and no longer visible!

To prevent this problem, we will remove the enemy if its x position is less than -50. At that position, the enemy should be completely outside the left edge of the screen.

```python
if enemy.x < -50:
    enemies.remove(enemy)
```

**IMPORTANT** Notice that we are checking the x position of **enemy** not **enemies**? Since we have many enemies, we'll need a **for** loop to go through each enemy. You can do this by putting the **if** lines under the **for** in the **Move the enemies** task, or you can create a separate **for** loop. Both ways are fine.

## Draw the enemies

Just like before, we need a **for** loop to go through the list of enemies and draw them one-by-one.

```python
for enemy in enemies:
    enemy.draw()
```

## At this point...

Right now your code should look like this (new lines are highlighted in yellow)...

```python hl_lines="2 13 25 26 27 28 29 31 32 34 35 40 41"
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
        enemy.y = random.randint(0, 600)
        enemy.x = 850
        enemies.append(enemy)

    for enemy in enemies:
        enemy.x -= 3
        
        if enemy.x < -50:
            enemies.remove(enemy)
    
def draw():
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()

pgzrun.go()
```