Moving the Tank
===
Remember how we moved the spaceship in Gem Catcher? We used **keyboard.left** and **keyboard.right** to detect if those keys are pressed. Let's start with that, but change it to tank. I also reduced the speed a little as I don't want my tank to move too fast.

```python
def update():
    if keyboard.left:
        tank.x = tank.x - 2
    if keyboard.right:
        tank.x = tank.x + 2
```

Don't forget to erase the screen by filling it with a color (...I'm using black here).

```python
screen.fill((0,0,0))
```

To detect up and down, we can use **keyboard.up** and **keyboard.down**. For the full list of keys you can use, you can refer to the [Pygame Zero documentations](https://pygame-zero.readthedocs.io/en/stable/hooks.html#buttons-and-keys).

To move left and right, we changed **x**. To move up and down, we should change **y**.

```python
def update():
    if keyboard.left:
        tank.x = tank.x - 2
    if keyboard.right:
        tank.x = tank.x + 2
    if keyboard.up:
        tank.y = tank.y - 2
    if keyboard.down:
        tank.y = tank.y + 2
```

Face where you're going
===
Now our tank can move in all directions, but it's not facing the right way! We should turn our tank so that it always faces the direction it is travelling in. I've done the first two below (..for left and right), can you do the rest?

```python
def update():
    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    if keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    if keyboard.up:
        tank.y = tank.y - 2
    if keyboard.down:
        tank.y = tank.y + 2
```

if and elif
===
If we press two buttons (eg. up and left) at the same time, the tank will move diagonally. That can be good for some games, but we don't want that here. Even if two buttons are pressed at the same time, we only want the tank to move in a single direction. To do that, we'll change the second to fourth **if** into **elif**.

```python
def update():
    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
    elif keyboard.down:
        tank.y = tank.y + 2
```

### elif
**elif** is Python's short form for **else if**. The statements under an **elif**, will only run if the previous **if** are not true. So in the latest example, only one of the conditions will run, no matter how many buttons you press simultaneously.