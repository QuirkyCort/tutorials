Power Up: Drone
===
Again, we'll use Vectr to draw the drone. By now, you should be pretty used to Vectr, and I'm not using any new techniques to draw my drone, so I'll just leave you with a sample image and you can go ahead and design your own drone.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/drone.png)

The drone looks best if it's smaller than the player ship. Beyond that, it's really up to you. My own drone isn't exactly fantastic, so I'm sure you can do better.

Adding the Drone
===
Since we are expecting only one drone, we won't need a list for it.

```
drone = Actor('drone')
```

We need to keep track of whether we have picked up the strawberry power up, so we'll add in a new variable. We'll set this variable to ```False``` at the start of the game (...haven't picked up powerup yet).

```
powerup2 = False
```

Look for this code in your program...

```
if powerups[hit].image == 'powerup2':
    powerup1 += 1
```

That's where we detect the type of powerup that we've picked up. We are going to modify it to detect the strawberry powerup.

```
if powerups[hit].image == 'powerup2':
    powerup1 += 1
elif powerups[hit].image == 'powerup3':
    powerup2 = True
```

Since we are modifying ```powerup2```, be sure to declare it as global...

```
global bullet_delay, powerup1, powerup2
```

We only draw our drone if we ```powerup2``` is True. So add this to your ```draw()``` function.

```
if powerup2:  // This is the same as writing: if powerup2 == True:
    drone.draw()
```

We want our drone to follow our ship, so add this to the ```update()``` function.

```
drone.move_towards(player, 3)
```

Making it Shoot
===
The code to make the drone shoot is similar to that for the player. To keep it neat, we should put it inside our ```shoot()``` function, together with the rest of the shoot code.

```
if powerup2:
    bullet = Actor('player_bullet')
    bullet.x = drone.x
    bullet.y = drone.y
    bullet.angle = 90
    bullets.append(bullet)
```

The only difference here is that the bullet's x and y starts at the drone rather than at the player.

At this Point...
===
Right now, both your power ups should be completed. You can add more powerups if you like, and there will be some ideas for that in the challenges section at the end. Your code at this point should look like this.

```
import pgzrun
import random
from pgzhelper import *

WIDTH=800
HEIGHT=600

player = Actor('player')
player.x = 400
player.y = 500

drone = Actor('drone')

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
powerup1 = 0
powerup2 = False

sounds.main_theme.play(-1)

def shoot():
    global bullet_delay

    sounds.sfx_sounds_interaction25.play()
    bullet_delay = 5

    if powerup1 == 0:
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)
        
    elif powerup1 == 1:
        bullet = Actor('player_bullet')
        bullet.x = player.x - 15
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x + 15
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)
        
    elif powerup1 == 2:
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 110
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)

        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 70
        bullets.append(bullet)

    elif powerup1 == 3:
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 110
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x - 15
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x + 15
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)

        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 70
        bullets.append(bullet)

    elif powerup1 >= 4:
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 115
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 100
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)
        
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 80
        bullets.append(bullet)

        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 65
        bullets.append(bullet)

    if powerup2:
        bullet = Actor('player_bullet')
        bullet.x = drone.x
        bullet.y = drone.y
        bullet.angle = 90
        bullets.append(bullet)

def update():
    global bullet_delay, powerup1, powerup2
    
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

    drone.move_towards(player, 3)

    if keyboard.space and bullet_delay == 0:
        shoot()

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
        if powerups[hit].image == 'powerup2':
            powerup1 += 1
        elif powerups[hit].image == 'powerup3':
            powerup2 = True
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
    if powerup2:
        drone.draw()
    player.draw()
    for bullet in bullets:
        bullet.draw()

pgzrun.go() # Must be last line
```