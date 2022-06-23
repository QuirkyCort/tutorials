Losing
===
It won't be much of a game if the enemy bullets can't hurt us. Let's fix that next. First we create a variable named **game_over** and put it outside of any functions (...I put mine just above **update()**, but you can put it further up if you want to).

```python
game_over = False
```

Next, we will set **game_over** to **True** if the enemy bullet hits our tank.

```python
if bullet.colliderect(tank):
    game_over = True
```

Note that since our tank is not a list, we are using **colliderect** instead of **collidelist**.

Finally, in **draw()**, we check if **game_over** is true...

```python
elif game_over:
    screen.fill((0,0,0))
    screen.draw.text('You Lose!', (260,250), color=(255,255,255), fontsize=100)
```

...and draw "You Lose!" if it is.

Completed!
===
The completed game should look like this...

```python
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

game_over = False

def update():
    global bullet_holdoff
    global game_over

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
        enemy_index = bullet.collidelist(enemies)
        if enemy_index != -1:
            del enemies[enemy_index]
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
        if bullet.colliderect(tank):
            game_over = True
            
def draw():
    if len(enemies) == 0:
        screen.fill((0,0,0))
        screen.draw.text('You Win!', (260,250), color=(255,255,255), fontsize=100)
    elif game_over:
        screen.fill((0,0,0))
        screen.draw.text('You Lose!', (260,250), color=(255,255,255), fontsize=100)
    else:
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