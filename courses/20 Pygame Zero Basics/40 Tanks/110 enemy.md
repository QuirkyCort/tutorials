Adding One Enemy
===
We'll be adding many enemies eventually, but let us start with just one. Create a new actor for the enemy. I'm using the "tank_red" image, but you can use a different one if you want to.

```
enemy = Actor('tank_red')
enemy.y = 25
enemy.x = 400
enemy.angle = 270
```

I'm setting **y** to 25; this will put it at the top, and **angle** to 270 to make it point downwards.

Make sure to draw your enemy in the **draw()** function.

```
enemy.draw()
```

Enemy Behaviour
===
We want our enemy to do three things...

* Move
* Turn
* Shoot

...and we'll get it to randomly choose one of these action. Inside update, we'll add in...

```
choice = random.randint(0, 2)
if choice == 0:
    enemy.move_count = 20
    print('move')
elif choice == 1:
    print('turn')
else:
    print('shoot')
```

What this code does is...

```choice = random.randint(0, 2)``` : This gets a random number and save it to a variable **choice**. The random number can be 0, 1, or 2.

```if choice == 0:``` : Here we check what is the random number choosen. If it is 0, we'll get the tank to move, if it is 1, we'll get it to turn, and if it is 2, we'll get it to shoot.

```enemy.move_count = 20``` : This is something new. Here we are creating a new variable named **move_count** inside the enemy actor and setting it to 20. Later on, we'll see what it is for.

```print('move'), print('turn'), print('shoot')``` : These are just temporary. We'll replace them with the actual code to make the tank move, turn, or shoot later.

Moving
===
First, let's set **enemy.move_count** to zero at the start.

```
enemy = Actor('tank_red')
enemy.y = 25
enemy.x = 400
enemy.angle = 270
enemy.move_count = 0  # Add this line
```

Now, we are going to modify our enemy choice code.

```
choice = random.randint(0, 2)
if enemy.move_count > 0:
    enemy.move_count = enemy.move_count - 1
    if enemy.angle == 0:
        enemy.x = enemy.x + 2
    elif enemy.angle == 90:
        enemy.y = enemy.y - 2
    elif enemy.angle == 180:
        enemy.x = enemy.x - 2
    elif enemy.angle == 270:
        enemy.y = enemy.y + 2
elif choice == 0:
    enemy.move_count = 20
elif choice == 1:
    print('turn')
else:
    print('shoot')
```

Run the code. You should see the tank moving forward (...with an occasional short pause). The pause occurs when the tank chooses "turn" or "shoot" (...which currently does nothing).

How this code works is when the **choice** is 0, we set **move_count** to 20. Then if **move_count** is greater than zero, we ignore the choice, move the tank in the direction it is facing, and reduce **move_count** by 1. This will make it move 20 times before we check for the **choice** again.

Turning
===
Next, we are going to add in turning. Change this part of the code...

```
elif choice == 1:
    print('turn')
```

...into this...

```
elif choice == 1:
    enemy.angle = random.randint(0, 3) * 90
```

This will choose a random number and multiply it by 90. The random number can be 0, 1, 2, or 3. So after multiplying by 90, it will be 0, 90, 180, or 270. That will make it face right, up, left, or down.

Now the enemy tank will move around randomly, but it will drive through the walls! Let's fix that next.

Wall
===
To prevent moving through the wall, we change the enemy movement code to...

```
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
        enemy.move_count = 0
```

This is similar to how the player tank avoids moving through the wall. We first save the tank's x and y position, then check if it is colliding with all of the walls. If it is, we return it to it's original position. The only difference is that we also set **move_count** to zero. This will make the enemy choose a new action immediately.

We should also prevent it from moving off the screen...

```
if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
    enemy.x = original_x
    enemy.y = original_y
    enemy.move_count = 0
```

Now the enemy tank should move around without going through the walls or leaving the screen. The code at this point should look like this...

```
import pgzrun
import random

WIDTH=800
HEIGHT=600

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

enemy = Actor('tank_red')
enemy.y = 25
enemy.x = 400
enemy.angle = 270
enemy.move_count = 0

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

    # This part is for the enemy
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
            enemy.move_count = 0

        if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
            enemy.x = original_x
            enemy.y = original_y
            enemy.move_count = 0

    elif choice == 0:
        enemy.move_count = 20
    elif choice == 1:
        enemy.angle = random.randint(0, 3) * 90
    else:
        print('shoot')
            
def draw():
    screen.fill((0,0,0))
    background.draw()
    tank.draw()
    enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for wall in walls:
        wall.draw()

pgzrun.go() # Must be last line
```