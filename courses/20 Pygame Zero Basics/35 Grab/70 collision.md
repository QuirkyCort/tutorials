# Collision

If the player touches the coin, we want the coin to change to a new random position. We can detect collisions using an **if** statement and the **colliderect()** function. This is part of our game logic, so this code should be placed inside the **update()** function.

```python
if player.colliderect(coin):
    coin.x = random.randint(0, 800)
    coin.y = random.randint(0, 600)
```

Basically, what this code says is... "If the player collides with the coin, set a new random x and y position for the coin."

<video width="800" height="600" autoplay muted loop>
  <source src="../images/grab_collision.mp4" type="video/mp4">
</video>