Many Enemies
===
It's very easy to change our program to have many enemies instead of just one. First we'll create a list to store all the enemy tanks...

```
enemies = []
```

Next, I'll use a loop to create 3 enemies and add them to the list.

```
for i in range(3):
    enemy = Actor('tank_red')
    enemy.y = 25
    enemy.x = i * 200 + 100
    enemy.angle = 270
    enemy.move_count = 0
    enemies.append(enemy)
```

This line...

```
enemy.x = i * 200 + 100
```

...spaces the enemy out, so that they won't all appear at the same spot.

The entire enemy section in **update()** needs to be put in a **for** loop like this...

```
for enemy in enemies:  # This is the only new line!
    choice = random.randint(0, 2)
    if enemy.move_count > 0:
        enemy.move_count = enemy.move_count - 1

        original_x = enemy.x
        original_y = enemy.y
        if enemy.angle == 0:
            enemy.x = enemy.x + 2
        elif enemy.angle == 90:
            enemy.y = enemy.y - 2
        elif enemy.angle == 180:
            enemy.x = enemy.x - 2
        elif enemy.angle == 270:
            enemy.y = enemy.y + 2
        
        if enemy.collidelist(walls) != -1:
            enemy.x = original_x
            enemy.y = original_y
            enemy.moveCount = 0

        if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
            enemy.x = original_x
            enemy.y = original_y
            enemy.move_count = 0

    elif choice == 0:
        enemy.move_count = 20
    elif choice == 1:
        enemy.angle = random.randint(0, 3) * 90
    else:
        bullet = Actor('bulletred2')
        bullet.angle = enemy.angle
        bullet.x = enemy.x
        bullet.y = enemy.y
        enemy_bullets.append(bullet)
```

Only the first line is new. The rest of the lines are the same as what you have before, but remember to indent them so that they are within the **for** loop.

Lastly, we need to put the **enemy.draw()** inside the **draw()** function in a **for** loop as well.

```
for enemy in enemies:  # Only this line is new!
    enemy.draw()
```

The code at this point should look like this...

```
import pgzrun
import random

WIDTH=800
HEIGHT=600

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

enemies = []
for i in range(3):
    enemy = Actor('tank_red')
    enemy.y = 25
    enemy.x = i * 200 + 100
    enemy.angle = 270
    enemy.move_count = 0
    enemies.append(enemy)

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

enemy_bullets = []

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

    # This part is for the enemy
    for enemy in enemies:
        choice = random.randint(0, 2)
        if enemy.move_count > 0:
            enemy.move_count = enemy.move_count - 1

            original_x = enemy.x
            original_y = enemy.y
            if enemy.angle == 0:
                enemy.x = enemy.x + 2
            elif enemy.angle == 90:
                enemy.y = enemy.y - 2
            elif enemy.angle == 180:
                enemy.x = enemy.x - 2
            elif enemy.angle == 270:
                enemy.y = enemy.y + 2
            
            if enemy.collidelist(walls) != -1:
                enemy.x = original_x
                enemy.y = original_y
                enemy.moveCount = 0

            if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
                enemy.x = original_x
                enemy.y = original_y
                enemy.move_count = 0

        elif choice == 0:
            enemy.move_count = 20
        elif choice == 1:
            enemy.angle = random.randint(0, 3) * 90
        else:
            bullet = Actor('bulletred2')
            bullet.angle = enemy.angle
            bullet.x = enemy.x
            bullet.y = enemy.y
            enemy_bullets.append(bullet)

    # This part is for the enemy bullets
    for bullet in enemy_bullets:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        elif bullet.angle == 90:
            bullet.y = bullet.y - 5
        elif bullet.angle == 180:
            bullet.x = bullet.x - 5
        elif bullet.angle == 270:
            bullet.y = bullet.y + 5

    for bullet in enemy_bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            enemy_bullets.remove(bullet)
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            enemy_bullets.remove(bullet)
            
def draw():
    screen.fill((0,0,0))
    background.draw()
    tank.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bullet in enemy_bullets:
        bullet.draw()
    for wall in walls:
        wall.draw()

pgzrun.go() # Must be last line
```