Background
===
Same as before, we start programming our game by...

* Importing Pygame Zero
* Setting the window's width and height
* Running ```pgzrun.go()```

```
import pgzrun

WIDTH=800
HEIGHT=600

pgzrun.go() # Must be last line
```

Click **File**, **Save As...** then select the ```ninja_runner``` folder you have previously created. Give your program a filename (eg. ```ninja_runner.py```) then click **Save**.

Draw Sky
===
We can draw different shapes using the functions under ```screen.draw```. We have previously used ```screen.draw.text()```, but there are many more functions, such as...

* ```screen.draw.line()```
* ```screen.draw.circle()```
* ```screen.draw.filled_circle()```
* ```screen.draw.rect()```
* ```screen.draw.filled_rect()```

To learn more about these function, you can refer to the Pygame Zero [documentations here](https://pygame-zero.readthedocs.io/en/stable/builtins.html#screen).

For now, we'll just be using ```screen.draw.filled_rect()```. This draws a rectangle to the screen, so we'll need to add it to the ```draw()``` function.

```
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))

pgzrun.go() # Must be last line
```

This is what the new lines does...

```def draw():``` : This is the draw function that Pygame Zero will run regularly. Anything that draws to the screen should be inside this function.

```screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254)``` : This draws a rectangle on the screen, starting from ```0,0``` (top left corner) and with a width of 800 and a height of 400. The color consists of 163 red, 232 green, and 254 blue.

**Try: Experiment with different colors and see what you get. Remember that each component of the color must be in the range from 0 to 255.**

Draw Ground
===
The previous step drew in the sky. Now let's add a second rectangle to draw the ground.

```
import pgzrun

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

pgzrun.go() # Must be last line
```

Here's what the new line does...

```screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))``` : This time, we'll start the rectangle at ```0,400```. This means x=0 and y=400. The screen is 600 pixels tall, and the previous rectangle was 400 pixels tall, so we only need this rectangle to be 200 pixels tall.

Once completed, run your program. Your screen should look like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/background.png)
