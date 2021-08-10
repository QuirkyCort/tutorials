Drawing the Cannon Bullet
===
We want to create a new cannon bullet everytime we press the space bar. Since we can have more than one bullet at a time, we'll use a list to hold all our bullets. Start by creating an empty list...

```
bullets = []
```

Next, in **update()**, check if the space key is pressed and add a bullet if it is.

```
if keyboard.space:
    bullet = Actor('bulletblue2')
    bullet.angle = tank.angle
    bullet.x = tank.x
    bullet.y = tank.y
    bullets.append(bullet)
```

We set the bullet angle to be the same as the tank so that they'll face the same direction. We also set the x and y of the bullet to be the same as the tank, so that the bullet will start from the tank.

Don't forget to draw the bullets in the **draw()** function...

```
for bullet in bullets:
    bullet.draw()
```

When you try out the program, you'll see a bullet created each time you press the space bar. But the bullet just stays there and don't do anything, so next, we'll make the bullet fly.

Moving the Bullet
===
In update, we can move the bullet by changing x or y. To decide which direction to move towards, we can look at the bullet's angle.

| Angle | Direction | x or y |
|-|-|-|
| 0   | Right | x+ |
| 90  | Up    | y- |
| 180 | Left  | x- |
| 270 | Down  | y+ |

We should move the bullet in the **update()** function. Using a **for** loop.

```
for bullet in bullets:
    if bullet.angle == 0:
        bullet.x = bullet.x + 5
    elif bullet.angle == 90:
        bullet.y = bullet.y - 5
    elif bullet.angle == 180:
        bullet.x = bullet.x - 5
    elif bullet.angle == 270:
        bullet.y = bullet.y + 5
```

Hold-Off
===
Now our bullet looks more like a laser! That's because when we press the space bar, it creates a LOT of bullets very rapidly. We should add a hold-off. This is some code that stops the tank for shooting for a while after each bullet. We'll start by creating a new variable.

```
bullet_holdoff = 0
```

Then modify our shoot code...

```
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
```

If you try to run the code now, you'll get an error. Do you know why? Look at the **Score** section in Gem Catcher and see if you can figure out what's missing! (Answer is at the bottom of this page, but try to figure it out on your own!)

What the above code does is...

```if bullet_holdoff == 0:``` Only allow firing if bullet_holdoff is 0.

```bullet_holdoff = 100``` Set the bullet_holdoff to 100. This will prevent firing since it is no longer zero. You can try changing this value and see what effects it has.

```
else:
    bullet_holdoff = bullet_holdoff - 1
```

If the bullet_holdoff is not zero, we'll decrease it by one. This will gradually reduce it until it reaches zero again.

Your code should now look like this...

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

### What's missing?
We need to add ```global bullet_holdoff```.

The **bullet_holdoff** variable is declared outside of the update() function, but we are trying to write it from inside the update() function. In Python, we can read variables that are outside a function (...these are called global variables), but cannot write to them unless we declare them as global inside the function.
