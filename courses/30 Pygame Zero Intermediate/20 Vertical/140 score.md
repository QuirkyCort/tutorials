Keeping Score
===
Let's keep a score, so we can compare and see who's the better player! Start by adding a ```score``` variable.

```python
score = 0
```

I'm programming in two ways to gain score...

* Destroy enemy: 10 points
* Pickup chocolate donuts: 100 points
* No points for matcha and strawberry donuts, as you already get powerups for them.

Look for this code in your program...

```python
explosions.append(explosion)
enemies.remove(enemies[hit])
```

...and add code for increasing the score...

```python
explosions.append(explosion)
enemies.remove(enemies[hit])
score += 10
```

For the chocolate donuts, look for this code...

```python
if powerups[hit].image == 'powerup2':
    powerup1 += 1
elif powerups[hit].image == 'powerup3':
    powerup2 = True
```

...and change it to this...

```python
if powerups[hit].image == 'powerup2':
    powerup1 += 1
elif powerups[hit].image == 'powerup3':
    powerup2 = True
else:
    score += 100
```

We are changing ```score```  from inside the ```update()``` function, so don't forget to declare it as global.

```python
global bullet_delay, powerup1, powerup2, game_state, score
```

Displaying the score
===
We can draw the score the same way we did in space gems, by adding a ```screen.draw.text()``` fuction in ```draw()```.

```python
screen.draw.text(str(score), (10, 10), color=(255,255,255), fontsize=40)
```

Remember that ```score``` is an integer, so we'll need to change it to a str by using ```str()```.

At this Point
===
You game is now complete! Sort of... No program is ever truly complete, as you can always add more features or improve on it. Take a look at the challenges section to find some ideas on how to improve your game.

Your program should now look like this...

```python
import pgzrun
import random
from pgzhelper import *

WIDTH=800
HEIGHT=600

player = Actor('player')
player.x = 400
player.y = 500

drone = Actor('drone')

game_over = Actor('game_over')
game_over.x = 400
game_over.y = 300

game_state = 1

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

score = 0

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
    global bullet_delay, powerup1, powerup2, game_state, score
    
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

    if keyboard.space and bullet_delay == 0 and game_state == 1:
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
            score += 10

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
    if hit != -1 and game_state == 1:
        sounds.sfx_sounds_fanfare3.play()
        if powerups[hit].image == 'powerup2':
            powerup1 += 1
        elif powerups[hit].image == 'powerup3':
            powerup2 = True
        else:
            score += 100
        powerups.remove(powerups[hit])

    if game_state == 1:
        if player.collidelist(enemy_bullets) != -1 or player.collidelist(enemies) != -1:
            game_state = 2
            explosion = Actor('explosion1')
            explosion.x = player.x
            explosion.y = player.y
            explosion.images = ['explosion1', 'explosion2']
            explosion.fps = 8
            explosion.life = 100
            explosions.append(explosion)
            sounds.main_theme.stop()
            sounds.sfx_exp_medium12.play()
            sounds.subdued_theme.play(-1)

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
    if game_state == 1:
        player.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text(str(score), (10, 10), color=(255,255,255), fontsize=40)

    if game_state == 2:
        game_over.draw()

pgzrun.go() # Must be last line

```