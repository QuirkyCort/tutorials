Enemy Bullets
===
It's not very fair if you can shoot the enemy, but they can't shoot back. So let's give our enemy the ability to shoot!

Since we can have more than one enemy bullet at a time, we'll start by creating a list for it...

```
enemy_bullets = []
```

For my strawberry enemy, I just want them to shoot in a random direction. I also do not want them to be shooting non-stop (...it'll make the game too hard).

We'll add the following code to the ```for enemy in enemies:``` loop inside ```update```.

```
if random.randint(0, 1000) > 990:
    bullet = Actor('enemy_bullet')
    bullet.x = enemy.x
    bullet.y = enemy.y
    bullet.angle = random.randint(0, 359)
    enemy_bullets.append(bullet)
```

For each enemy, we'll pick a random number between 0 and 1000, and shoot only if the number is above 990. If we are shooting, we'll create a new bullet, set the x and y to the same as the enemy, and pick a random direction from 0 to 359 (...we skip 360, as that is the same as 0 degrees). Finally, we add the bullet to the enemy_bullets list.

The code to make the bullet move is almost the same as the player bullet, but we'll make it slower.

```
for bullet in enemy_bullets:
    bullet.move_forward(5)
```

Unlike the player bullet, the enemy bullet may fly in any direction, so to remove it from screen, we need to check for more conditions. Modify the previous code to this...

```
for bullet in enemy_bullets:
    bullet.move_forward(5)
    if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
        enemy_bullets.remove(bullet)
```

At this point, the enemy can shoot at us, but nothing happens even if we get hit. Eventually, we should create a game over if we are hit by the enemy, but we'll leave that for last.