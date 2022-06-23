Obstacles
===
In our gem catcher game, we only have a single gem at a time and it returns to the top everytime we catch it. In our ninja runner game, we are going to have multiple obstacles appear on screen at the same time. To do so, we are going to make use of **lists**.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/cactus.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/cactus.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/cactus.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/cactus.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

First, let's add an empty list called ```obstacles``` and a integer variable ```obstacles_timeout```

```python
obstacles = []
obstacles_timeout = 0
```

Now in our ```update()``` function, we are going to increase out timeout by 1 each time.

```python
obstacles_timeout += 1
```

Next, if the timeout is greater than 50, we'll add in an obstacle and reset the timeout to zero.

```python
if obstacles_timeout > 50:
  actor = Actor('cactus')
  actor.x = 850
  actor.y = 430
  obstacles.append(actor)
  obstacles_timeout = 0
```

The only thing new here is ```obstacles.append(actor)```. This adds ```actor``` to the ```obstacles``` list.

**IMPORTANT: You'll need to move the ```cactus``` image into your ```images``` folder first! If you decide to use a different image, change the image name accordingly.**

Now to make the obstacles move across the screen...

```python
for actor in obstacles:
  actor.x -= 8
```

This will go through the entire obstacles list and reduce the x position for obstacle. Reducing x will make the obstacle move to the left.

Finally, we need to draw the obstacles on screen. In the ```draw()``` function, add...

```python
for actor in obstacles:
  actor.draw()
```

Your program should now look like this...

```python
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
runner.x = 100
runner.y = 400

velocity_y = 0
gravity = 1

obstacles = []
obstacles_timeout = 0

def update():
  global velocity_y, obstacles_timeout
  runner.next_image()

  obstacles_timeout += 1
  if obstacles_timeout > 50:
    actor = Actor('cactus')
    actor.x = 850
    actor.y = 430
    obstacles.append(actor)
    obstacles_timeout = 0

  for actor in obstacles:
    actor.x -= 8

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
  velocity_y += gravity
  if runner.y > 400:
    velocity_y = 0
    runner.y = 400

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
  runner.draw()
  for actor in obstacles:
    actor.draw()

pgzrun.go() # Must be last line
```