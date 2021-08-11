Power Ups
===
For this game, we'll create two types of power-ups...

**More Bullets (Green)** : This lets us fire out more bullets with every shot. If you pick it up once, you'll shoot two bullets at a time. If you pick it up again, you'll shoot three bullets at a time, and so on.

**Drone (Pink)** : This creates a drone that follows your main ship and shoot together with you. For this game, we'll only have one drone, but you can add more if you wish.

Every power-up starts as brown, which doesn't have any effects when picked-up. When it is hit by a bullet, the power-up will change color randomly. It'll also get knocked upwards when hit.

Power Up Image
===
We'll start by creating an image for our power up. In the Twin Bee game, the power up is a bell. For me, I'm fond of donuts, so let's have our ship powered up by those sugary rings of goodness.

To make my donut, I'm using a couple of new technique in Vectr. First, I'll create two ellipses, one for the base donut, and the second for the toppings...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut3.png)

For the topping, we'll double click on it to go into points mode, then add points by clicking on the line.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut4.png)

Move the points so that it looks wavy like the above image.

It won't be a donut without a hole, so create another ellipse. It should look like the one below. Make a copy of it, then move one copy to the center of the frosting.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut7.png)

Previously, we have learned how to "Unite/Add" two shapes together. For my donut, I'll be doing a "Subtract" to create the hole in the middle. Select the pink ellipses and the frosting and click the **"Subtract"** button.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut6.png)

Move the second ellipse to this position...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut5.png)

Then select the pink ellipse and the base donut, then click **"Subtract"**.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut8.png)

Add some sprinkles on it...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/donut9.png)

Finally, scale it to a suitable size, make a few versions with different colors (...I'm using Chocolate, Matcha, and Strawberry flavors) and we are done!

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/powerup1.png)
![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/powerup2.png)
![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/powerup3.png)

After exporting these files, I renamed them "powerup1.png", "powerup2.png", and "powerup3.png".

Adding to Game
===
We can have more than one powerup at a time, so we'll start with an empty list.

```
powerups = []
```

Just like with our enemies, we are going to make the power-ups appear randomly, but with much lower frequency.

```
if random.randint(0, 1000) > 998:
    powerup = Actor('powerup1')
    powerup.y = -50
    powerup.x = random.randint(100, 700)
    powerups.append(powerup)
```

Unlike the enemy, I'm going to make my power go straight down, so I won't need a direction for it. Feel free to change the 998 to a different number and see how that affects the frequency of powerups appearing.

When a bullet hits the powerup, I want to make it jump up a little, and change to a random color. To help with that, I'll start by creating a variable that contains a list of all the powerup image names.

```
powerup_images = ['powerup1', 'powerup2', 'powerup3']
```

Next, we'll iterate through the powerups and see if any of them are colliding with a player bullet. If they are, we'll...

* Make it jump up by 40 px
* Change the image to a random image
* Remove the bullet

```
for powerup in powerups:
    hit = powerup.collidelist(bullets)
    if hit != -1:
        powerup.y -= 40
        powerup.image = random.choice(powerup_images)
        bullets.remove(bullets[hit])
```

Picking up
===
When our player ship touches the powerup, it should disappear.

```
hit = player.collidelist(powerups)
    if hit != -1:
        powerups.remove(powerups[hit])
```

I'm also going to add a sound, to let the player know that they have successfully picked up a powerup. I'm using the "sfx_sounds_fanfare3.wav" soundfile, but you can use whatever you like.

```
sounds.sfx_sounds_fanfare3.play()
```

At this Point...
===
Right now, your player ship can shoot the powerup to change it, and can pick up the powerups, but they don't do anything yet. We'll implement them in the next topic.

Your code should look like this now...

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

explosions = []

enemy_bullets = []

powerups = []
powerup_images = ['powerup1', 'powerup2', 'powerup3']

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

    if random.randint(0, 1000) > 998:
        powerup = Actor('powerup1')
        powerup.y = -50
        powerup.x = random.randint(100, 700)
        powerups.append(powerup)

    for powerup in powerups:
        powerup.y += 4

    for enemy in enemies:
        enemy.move_in_direction(4)
        enemy.animate()
        if random.randint(0, 1000) > 990:
            bullet = Actor('enemy_bullet')
            bullet.x = enemy.x
            bullet.y = enemy.y
            bullet.angle = random.randint(0, 359)
            enemy_bullets.append(bullet)
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

    for bullet in enemy_bullets:
        bullet.move_forward(5)
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            enemy_bullets.remove(bullet)

    for explosion in explosions:
        explosion.animate()
        explosion.life -= 1
        if explosion.life == 0:
            explosions.remove(explosion)

    for powerup in powerups:
        hit = powerup.collidelist(bullets)
        if hit != -1:
            powerup.y -= 40
            powerup.image = random.choice(powerup_images)
            bullets.remove(bullets[hit])

    hit = player.collidelist(powerups)
    if hit != -1:
        sounds.sfx_sounds_fanfare3.play()
        powerups.remove(powerups[hit])

def draw():
    screen.clear()
    for background in backgrounds:
        background.draw()
    for explosion in explosions:
        explosion.draw()
    for bullet in enemy_bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    for powerup in powerups:
        powerup.draw()
    player.draw()
    for bullet in bullets:
        bullet.draw()

pgzrun.go() # Must be last line
```