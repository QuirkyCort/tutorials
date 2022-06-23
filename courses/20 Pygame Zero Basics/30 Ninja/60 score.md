Keeping Score
===
Just like in the gem catcher program, we'll use a variable named ```score```  to keep track of our score.

```python
score = 0
```

We'll increase our score each time the obstacle disappears off the left side of the screen. Inside ```update()```, let's change this...

```python
  for actor in obstacles:
    actor.x -= 8
```

...into this...

```python
  for actor in obstacles:
    actor.x -= 8
    if actor.x < -50:
      obstacles.remove(actor)
      score += 1
```

This is what each line means...

```if actor.x < -50``` : When the x position is less than -50, the actor is most probably outside of the screen. So we will...

```obstacles.remove(actor)``` : Remove the actor from the obstacles list...

```score += 1``` : ...and increase score by 1. **Remember to declare ```score``` as a global!**.

Drawing Obstacles and Score
===
The obstacles won't appear on screen if we don't draw it inside the ```draw()``` function. So let's add in...

```python
for actor in obstacles:
  actor.draw()
```

This will go through the list of obstacles and draw each one.

We should also display the score on screen using...

```python
screen.draw.text('Score: ' + str(score), (15,10), color=(0,0,0), fontsize=30)
```

Feel free to change the color, position, or fontsize.