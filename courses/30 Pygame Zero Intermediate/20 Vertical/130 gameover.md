Game Over
===
It's not much of a game if you can't lose. Let's add a game over screen if you get hit by the enemy. We'll start by drawing a game over image in Vectr.

I'm using the **Text** function to write "Game Over"...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/text2.png)

...choosing a different font to make it look cool...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/text.png)

...and adding a background to it using a rounded rectangle...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/game-over.png)

We'll add this to our game, but don't draw it yet.

```
game_over = Actor('game_over')
game_over.x = 400
game_over.y = 300
```

Game States
===
A game can have multiple states, such as...

* Starting screen
* Actual game
* Game over screen

In each of theses states, the program will do and show different things. For example, in the "Game over screen" state, you can't shoot, and the player isn't shown.

To keep track of the game state, we'll create a new variable.

```
game_state = 1
```

We'll use 1 to represent the "Actual game" state, and 2 to represent the "Game over screen" state. When the player touches the enemy bullet or enemy, we'll change the state to 2.

```
if player.collidelist(enemy_bullets) != -1 or player.collidelist(enemies) != -1:
    game_state = 2
```

Since we are changing ```game_state```, remember to declare it as global.

```
global bullet_delay, powerup1, powerup2, game_state
```

Explosion and Sound Effects
===

Let's add in an explosion if the player is destroyed. See if you can figure out where to put this code.

```
explosion = Actor('explosion1')
explosion.x = player.x
explosion.y = player.y
explosion.images = ['explosion1', 'explosion2']
explosion.fps = 8
explosion.life = 100
explosions.append(explosion)
```

This works the same as the enemy explosion, except that we made it last longer (...life = 100).

We'll also have some sound effects...

```
sounds.main_theme.stop()
sounds.sfx_exp_medium12.play()
sounds.subdued_theme.play(-1)
```

This will...

* Stop the background music
* Play an explosion sound
* Start a different background music

They only work if you have the corresponding sound files in your sounds folder. You don't have to use the same sound as me; choose whichever sound and music you like.

Game Over
===
If ```game_state``` is 2, we'll draw the game over screen.

```
if game_state == 2:
    game_over.draw()
```

We should also modify our program, so that it'll only draw the player if ```game_state``` is 1.

```
if game_state == 1:
    player.draw()
```

Similarly, we'll allow shooting only if ```game_state``` is 1.

```
if keyboard.space and bullet_delay == 0 and game_state == 1:
    shoot()
```

Also, we can only pickup powerups if ```game_state``` is 1.

```
hit = player.collidelist(powerups)
if hit != -1 and game_state == 1:
.
.
.
```

Finally, you may have noticed a bug when you test the program. Sometimes after the player is destroyed, you may see another explosion happen out of nowhere. That happens because the player is still able to collide with the enemy even if the player isn't drawn on screen!

Let's modify the player collision code so that the player cannot collide unless the ```game_state``` is 1.

```
if game_state == 1:
    if player.collidelist(enemy_bullets) != -1 or player.collidelist(enemies) != -1:
    .
    .
    .
```
