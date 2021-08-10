Enemy Bullets
===
Just like with our player bullet, there can be more than one enemy bullet, so we'll create a list to store all of them.

```
enemy_bullets = []
```

To shoot, we'll create a new bullet and add it to the **enemy_bullets** list. This is similar to how the player shoots.

Replace this line...

```
print('shoot')
```

...with this...

```
bullet = Actor('bulletred2')
bullet.angle = enemy.angle
bullet.x = enemy.x
bullet.y = enemy.y
enemy_bullets.append(bullet)
```

You'll also need to draw the bullet. Add this into the **draw()** function...

```
for bullet in enemy_bullets:
    bullet.draw()
```

If you run the program now, you'll see the enemy tank creating bullets, but the bullets will just stay there and not move.

Moving the bullets
===
We want the enemy bullets to move. And just like the player bullet, it should destroy the walls and disappear when it hits the wall or the edge of the screen. The code is the same as for the player bullet, but with the list variable changed to **enemy_bullets**.

```
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
```

