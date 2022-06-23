Power Up: More Bullets
===
The more bullets powerup should increase our ship's fire power, depending on how many matcha donuts are picked up.

* 0  : One bullet
* 1  : Two bullets
* 2  : Three bullets
* 3  : Four bullets
* 4  : Five bullets
* 5+ : No change.

We need to track how many matcha donuts are picked up, and we'll do so with a new variable.

```python
powerup1 = 0
```

Everytime we pick up a matcha powerup, we'll add one to this number. Don't forget to declare ```powerup1``` as ```global```.

```python
if powerups[hit].image == 'powerup2':
    powerup1 += 1
```

Can you figure out where to place the above code? Hint: It should be when the player collides with a powerup.

Tidying up the Bullets Code
===
This is our current bullet firing code. Look for it in your own program.

```python
if keyboard.space and bullet_delay == 0:
    sounds.sfx_sounds_interaction25.play()
    bullet_delay = 5
    bullet = Actor('player_bullet')
    bullet.x = player.x
    bullet.y = player.y
    bullet.angle = 90
    bullets.append(bullet)
```

We could edit this to add in support for multiple bullets, but our ```update()``` function is getting very long now. It's neater to separate out some portion of the code to keep it neat. I'll start by separating out the bullet firing code.

I'm going to cut out most of the above, and place it in a new function, which I'm naming ```shoot()```.

```python
def shoot():
    global bullet_delay
    
    sounds.sfx_sounds_interaction25.play()
    bullet_delay = 5
    bullet = Actor('player_bullet')
    bullet.x = player.x
    bullet.y = player.y
    bullet.angle = 90
    bullets.append(bullet)
```

Next, I'll change my earlier bullet firing code to...

```python
if keyboard.space and bullet_delay == 0:
    shoot()
```

Test out your program. Everything should still work the same as before.

Two Bullets
===

Next, we are going to start adding in code for two bullets. We'll change the ```shoot()``` code into the following...

```python
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
```

Test it out again. Your ship should fire a single bullet at the beginning, but after picking up a matcha donut, it should start shooting two bullets.

Three Bullets
===
Next up, three bullets. I'm not going to show you the entire code this time. Try and figure out how to incorporate this into your program.

```python
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
```

Four Bullets
===
This is a combination of the two bullets code and the three bullets code. Again, try to figure out how to incorporate this into your program.

```python
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
```

Five Bullets
===
I'm going to leave this to you as a challenge. Be careful! We should fire five bullets not only if we have 4 matcha donuts, but also if we have **more than** 4 matcha donuts.