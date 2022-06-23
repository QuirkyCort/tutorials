Jump Physics
===
Which of these look more realistic?

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/jump.gif)

In real life, objects are affected by gravity. To make our ninja jump realistically, we'll need to simulate the effects of gravity in our game.

Let's start by adding in a variable for ```velocity_y``` and ```gravity```.

```python
velocity_y = 0
gravity = 1
```

Explanation for each line...

```velocity_y = 0``` : This represents how fast our ninja should be moving in the up/down direction. It starts at zero, as our ninja isn't jumping yet.

```gravity = 1``` : Gravity will change our velocity. We can change this later and see its effects, but leave it at 1 for now.


Next, in ```update()``` we are going to change the velocity when the up arrow is pressed.

```python
def update():
  global velocity_y
  runner.next_image()

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
```

This is what each line does...

```global velocity_y``` : We need to use global if we change a variable that comes from outside of a function.

```if keyboard.up;``` : When the up arrow is pressed...

```velocity_y = -15``` : Set the up/down velocity to -15. A negative number means it's going upwards.

```runner.y += velocity_y``` : Change our ninja's position using the velocity. The ```+=``` means to add ```velocity_y``` to ```runner.y```.

```python
# Tips
a += 1      # This line is the same as...
a = a + 1   # ...this line.

```

Try it out! If you programmed it correctly, the ninja should fly up into the sky when you press up. That's because we haven't added gravity yet!

Gravity
===
Gravity will change our velocity. Under the ```runner.y += velocity_y``` line, let's add it in ```velocity_y += gravity```.

Now our ninja falls straight down! We haven't tell our ninja when to stop falling yet! Let's add that in next...

```python
if runner.y > 400:
  velocity_y = 0
  runner.y = 400
```

Here we are treating ```y = 400`` as the "ground", and if the ninja is at a y position that's greater than 400, we will set her velocity_y to 0 and her y position to 400. This will prevent her from falling through the ground.

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

def update():
  global velocity_y
  runner.next_image()

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

pgzrun.go() # Must be last line
```