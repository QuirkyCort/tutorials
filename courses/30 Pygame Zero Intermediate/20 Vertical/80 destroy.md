Destroying Enemies
===
First, we'll draw an explosion...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/explode.png)

Nothing special. Just a bunch of ellipses. I've created two images (...the second one is just a copy of the first but rotated by 45 degrees), so that I can animate it.

My actual explosion is white, with no background, but that won't show up against the white background of this webpage, so I've added a black background to it here. Your explosion image should not have a background color.

You'll be seeing a lot of this explosion in the game, so it's best to keep it small and simple. Mine is approximately the size of my strawberry enemy.

Detecting when Enemy is Hit
===

Same as in previous games, we can detect a hit using ```collidelist()```. If a collision occurs, we'll remove both the bullet and the enemy.

```python
for bullet in bullets:
    hit = bullet.collidelist(enemies)
    if hit != -1:
        bullets.remove(bullet)
        enemies.remove(enemies[hit])
```

The ```for``` loop allows us to iterate through every bullet, and for each bullet we'll check which enemy collided with it. 

The ```collidelist()``` function gives us the **index** of the item that collided with the bullet. If ```hit``` is equal to -1, that means no collision, and we won't need to do anything. If ```hit``` is NOT -1, we'll remove the bullet and remove the enemy.

To remove the enemy, we'll use the ```remove()``` function, and provide it with the enemy that is hit. Since ```collidelist()```, only gives us the index, we'll need to retrieve the collided enemy using ```enemies[hit]```.

Creating an Explosion
===
The explosion effect isn't absolutely necessary, but it makes the game look more professional. We can have multiple explosions on screen at any time, so as usual, we'll create a list for it...

```python
explosions = []
```

Each time a bullet hit an enemy, we'll add an explosion at the spot where the enemy was and add it to the explosions list.

```python
explosion = Actor('explosion1')
explosion.x = enemies[hit].x
explosion.y = enemies[hit].y
explosions.append(explosion)
```

Make sure you place this code **before** the ```enemies.remove()```. If you had removed the enemy first, you won't be able to get it's x and y.

Since I have two explosion images, I'll add both of them to ```images``` and set an fps.

```python
explosion.images = ['explosion1', 'explosion2']
explosion.fps = 8
```

Next, I'll set a variable inside explosion, which I'm calling ```life```. You can use any variable name you want. This variable will store a countdown that represents how long the explosion will be displayed. Feel free to change this number and see what it does.

```python
explosion.life = 15
```

We only want the explosion to appear for a short while, so we'll decrease ```life``` on each update, and when it reaches zero, we'll delete away the explosion. We'll also run the ```animate()``` function here, so that the explosion will look animated.

```python
for explosion in explosions:
    explosion.animate()
    explosion.life -= 1
    if explosion.life == 0:
        explosions.remove(explosion)
```

Finally, we'll need to draw the explosion...

```python
for explosion in explosions:
    explosion.draw()
```

I'm drawing the explosion before the enemies, so that the enemy will appear on top of it (...if they overlap). Depending on the effect you want to achieve, you can also do it the other way round.

At this Point...
===
Now you should be able to destroy the enemies!

```python
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

explosions = []

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

    for bullet in bullets:
        hit = bullet.collidelist(enemies)
        if hit != -1:
            bullets.remove(bullet)
            explosion = Actor('explosion1')
            explosion.x = enemies[hit].x
            explosion.y = enemies[hit].y
            explosion.images = ['explosion1', 'explosion2']
            explosion.fps = 8
            explosion.life = 15
            explosions.append(explosion)
            enemies.remove(enemies[hit])

    for explosion in explosions:
        explosion.animate()
        explosion.life -= 1
        if explosion.life == 0:
            explosions.remove(explosion)

def draw():
    screen.clear()
    for background in backgrounds:
        background.draw()
    for explosion in explosions:
        explosion.draw()
    for enemy in enemies:
        enemy.draw()
    player.draw()
    for bullet in bullets:
        bullet.draw()

pgzrun.go() # Must be last line
```