Blocking Movements
===
Right now the walls don't do much; you can drive right through them! To prevent that, we'll need to check if the tank is colliding with the wall. Previously, we had used **colliderect** to detect collision. We can still use that to check if the tank collided with the wall pieces one-by-one, but since we have a big list of walls, it's easier to use **collidelist** instead.

If we collide with the wall when moving the tank, we will cancel the movement.

```python
def update():
    # Save the original position of the tank
    original_x = tank.x
    original_y = tank.y
    
    # Move the tank if keys are pressed
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
    
    # Return tank to original position if colliding with wall
    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y
```

This is what the code does...

```python
original_x = tank.x
original_y = tank.y
```

This saves the original position of the tank into the **original_x** and **original_y** variable.

```python
if tank.collidelist(walls) != -1:
    tank.x = original_x
    tank.y = original_y
```

The **tank.collidelist(walls)** will return a number that tells us which piece of wall the tank is colliding with. If the tank isn't colliding with any pieces of wall, it will return **-1**. So if the value isn't **-1**, we know that a collision has occured, and we'll restore the original position before the move.

Off Screen
===
Now our tank can't move through the walls anymore, but it can still drive off the screen! To prevent that, we need to check the position of the tank after movement, and return it back to the original position if it is off the screen.

```python
if tank.x < 0 or tank.x > 800 or tank.y < 0 or tank.y > 600:
    tank.x = original_x
    tank.y = original_y
```

Try it out.

You'll see that the tank can still move about halfway off screen. That's because the position of the tank is based on it's center. What can we do to prevent that? Think about it and attempt it on your own.