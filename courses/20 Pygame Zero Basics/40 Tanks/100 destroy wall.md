Destroying Walls
===
We want to destroy the wall if the bullet hits it. To detect a hit, we can use the **collidelist** function on the bullet, similar to what we previously did with the tank. Since we have multiple bullets in a list, we will need to go through every bullet using a **for** loop.

```
for bullet in bullets:
    wall_index = bullet.collidelist(walls)
```

If **wall_index** is **-1**, that means that the bullet didn't hit any walls. Else, **wall_index** will contain the index of the wall section that the bullet hit. We can then delete that wall section using **del**.

```
for bullet in bullets:
    wall_index = bullet.collidelist(walls)
    del walls[wall_index]
```

The **del** command tells python to delete **walls[wall_index]** from the **walls** list. Test out the **del** command below. Make sure you understand how it works.

```python.run
animals = ['cat', 'dog', 'monkey', 'elephant']
print(animals)
del animals[1]
print(animals)
```

Destroying Bullet
===
Now everytime you fire a bullet, it will pass through all the walls, destroying every wall section that it touches. That's probably not what you want! Let's make the bullet disappear too when it hits a wall. Another way or removing an item from a list is to use the **remove** function.

```
for bullet in bullets:
    wall_index = bullet.collidelist(walls)
    del walls[wall_index]
    bullets.remove(bullet)
```

Just like **del**, the **remove** function will remove an item from a list. The difference is that **del** requires a list with an index, while **remove** expects the value of the item to be removed. Test it out below...

```python.run
animals = ['cat', 'dog', 'monkey', 'elephant']
print(animals)
animals.remove('monkey')
print(animals)
```

Now everytime your bullet hits a wall, both the bullet and the wall will disappear.

### Reaching the edge
There is one more condition for removing the bullet; and that's when it reaches the edge of the screen.

```
if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
    bullets.remove(bullet)
```

Can you figure out where to insert this piece of code? Try it out!

At this point, your code should look like this...

```
import pgzrun
import random

WIDTH=800
HEIGHT=600

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

background = Actor('grass')

walls = []
for x in range(16):
    for y in range(10):
        if random.randint(0, 100) < 50:
            wall = Actor('wall')
            wall.x = x * 50 + 25
            wall.y = y * 50 + 25 + 50
            walls.append(wall)

bullets = []
bullet_holdoff = 0

def update():
    global bullet_holdoff

    # This part is for the tank
    original_x = tank.x
    original_y = tank.y

    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
        tank.angle = 90
    elif keyboard.down:
        tank.y = tank.y + 2
        tank.angle = 270

    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y

    if tank.x < 0 or tank.x > 800 or tank.y < 0 or tank.y > 600:
        tank.x = original_x
        tank.y = original_y

    # This part is for the bullet
    if bullet_holdoff == 0:
        if keyboard.space:
            bullet = Actor('bulletblue2')
            bullet.angle = tank.angle
            bullet.x = tank.x
            bullet.y = tank.y
            bullets.append(bullet)
            bullet_holdoff = 100
    else:
        bullet_holdoff = bullet_holdoff - 1
        
    for bullet in bullets:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        elif bullet.angle == 90:
            bullet.y = bullet.y - 5
        elif bullet.angle == 180:
            bullet.x = bullet.x - 5
        elif bullet.angle == 270:
            bullet.y = bullet.y + 5

    for bullet in bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            bullets.remove(bullet)
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)

            
def draw():
    screen.fill((0,0,0))
    background.draw()
    tank.draw()
    for bullet in bullets:
        bullet.draw()
    for wall in walls:
        wall.draw()

pgzrun.go() # Must be last line
```

### What happens if we don't remove the bullet when it reaches the edge?
Nothing much. The bullet will just keep flying forever outside of the screen. If you have a lot of bullets, it may eventually slow down your game, but it will likely require many thousands of bullets before that becomes noticeable.