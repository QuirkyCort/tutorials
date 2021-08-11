Enemies
===
We'll start by drawing an enemy image in [Vectr](http://vectr.com/). You can design your own enemy, but I want mine to look like a strawberry...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/enemy1_1.png) ![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/enemy1_2.png)

I have two images here, because I want to animate the enemy. The second image is just a slightly modified version of the first one. It's easy to create, and makes the game look better.

**IMPORTANT** When creating the two images, make sure that they are **exactly the same size**. While the game will run even if the sizes are not the same, it will cause the enemy to move slightly everytime we change image, and that won't look right.

**Take your time to create your own enemy, and make sure it's something that you are proud of.**

When you are done, export the images and put them in your game's images folder. I've named mine "enemy1_1.png" and "enemy1_2.png".

### Adding Enemies to the Game

We can have more than one enemy at a time, so just like the bullet, we'll create a list to store these enemies...

```
enemies = []
```

We want to add the enemy randomly, so we'll use ```random.randint(0, 1000)``` to pick a random number from 0 to 1000, and we'll create an enemy if it is greater than 980 (...try changing this number and see what it does). At the end, we'll add this new enemy to the enemies list. All these need to be added to the ```update()``` function.

```
if random.randint(0, 1000) > 980:
    enemy = Actor('enemy1_1')
    enemies.append(enemy)
```

I want my enemy to start at above the top of the screen, so I'll set y to a negative value. I also want the x position to be random, so I'll use randint to pick a value.

```
enemy.y = -50
enemy.x = random.randint(100, 700)
```

Since I have two images for the enemy, I'll set them both in ```images```. I'll also set fps (frames per second) to 5. This will make the image change 5 times per second.

```
enemy.images = ['enemy1_1', 'enemy1_2']
enemy.fps = 5
```

Finally, I want the direction of the enemy to be random, so I'll use randint to pick a random direction from -100 degrees to -80 degrees (...remember that 0 degrees means move to the right, so -90 is to move down). Feel free to change this angle range and see the effects.

```
enemy.direction = random.randint(-100, -80)
```

Your completed enemy adding code should look like this...

```
if random.randint(0, 1000) > 980:
    enemy = Actor('enemy1_1')
    enemy.images = ['enemy1_1', 'enemy1_2']
    enemy.fps = 5
    enemy.y = -50
    enemy.x = random.randint(100, 700)
    enemy.direction = random.randint(-100, -80)
    enemies.append(enemy)
```

### Drawing the Enemies

As always, the enemy won't appear if we don't draw them, so we'll add this to the ```draw()``` function.

```
for enemy in enemies:
    enemy.draw()
```

### Moving and Animating the Enemies

Now we have code to create the enemies and display them on screen, but they don't move yet. In the Gem Catcher game, we moved the gems downwards by changing y, but that will only make it move straight down. To make our enemy move in the random direction we have set earlier, we'll use ```move_in_direction()```.

Since we have multiple enemies, we'll need to use a for loop to apply this to all of them...

```
for enemy in enemies:
    enemy.move_in_direction(4)
```

Within the same loop, I should also run the ```animate()``` function. This will make its appearance switch between the two enemy images.

```
enemy.animate()
```

Like the bullet, we don't want our enemies to stick around forever, so we'll remove them when the leave the screen...

```
if enemy.y > 700:
    enemies.remove(enemy)
```

Note that although our screen height is only 600 pixels, we are only removing the enemy when it reaches a y of 700. This is because at y=600, half of the enemy is still within the screen.

The completed enemy movement code should look like this...

```
for enemy in enemies:
    enemy.move_in_direction(4)
    enemy.animate()
    if enemy.y > 700:
        enemies.remove(enemy)
```

At this Point...
===
Your program should now have a scrolling background, random enemies, and a player ship that can move and shoot. The code should look like this...

```
import pgzrun
import random
from pgzhelper import *

WIDTH=800
HEIGHT=600

player = Actor('player')
player.x = 400
player.y = 500

bullets = []
bullet_delay = 0

background_images = ['background1','background2','background3']
backgrounds = []
background = Actor(random.choice(background_images))
background.x = 400
background.y = 300
backgrounds.append(background)
background = Actor(random.choice(background_images))
background.x = 400
background.y = -300
backgrounds.append(background)

enemies = []

sounds.main_theme.play(-1)

def update():
    global bullet_delay
    
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x -= 5

    if player.x < 25:
        player.x = 25
    if player.x > 775:
        player.x = 775
    if player.y < 30:
        player.y = 30
    if player.y > 570:
        player.y = 570

    if keyboard.space and bullet_delay == 0:
        sounds.sfx_sounds_interaction25.play()
        bullet_delay = 5
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)

    if bullet_delay > 0:
        bullet_delay -= 1

    for bullet in bullets:
        bullet.move_forward(15)
        if bullet.y < 0:
            bullets.remove(bullet)

    for background in backgrounds:
        background.y += 3
        if background.y > 900:
            background.y -= 1200
            background.image = random.choice(background_images)

    if random.randint(0, 1000) > 980:
        enemy = Actor('enemy1_1')
        enemy.images = ['enemy1_1', 'enemy1_2']
        enemy.fps = 5
        enemy.y = -50
        enemy.x = random.randint(100, 700)
        enemy.direction = random.randint(-100, -80)
        enemies.append(enemy)

    for enemy in enemies:
        enemy.move_in_direction(4)
        enemy.animate()
        if enemy.y > 700:
            enemies.remove(enemy)

def draw():
    screen.clear()
    for background in backgrounds:
        background.draw()
    for enemy in enemies:
        enemy.draw()
    player.draw()
    for bullet in bullets:
        bullet.draw()

pgzrun.go() # Must be last line

```