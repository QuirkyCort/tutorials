Player Ship
===
As usual, we'll start with an empty window.

```python
import pgzrun

WIDTH=800
HEIGHT=600

pgzrun.go() # Must be last line
```

You can use a different width and height if you wish.
Just be aware that if you do so, you may need to adjust the X and Y position of various actors later in the program.

Run (Press F5 or click "Run -> Run Module") and make sure it works.

Drawing the Ship
===
Next, we're going to draw the player ship.

### Vectr

Visit [Vectr](https://vectr.com/) and click on the **"Use Online"** button (You may optionally create an account and login). You should see the following.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/vectr.png)

To start, I like to set the page to the same size as my game window.
This isn't strictly necessary, but it makes it easy for me to gauge how large my ship will appear on screen.

Click on **"Pages"** (top-left), and under **"Page Settings"**, set the page size to 800 by 600.
**Make sure the lock button between Width and Height is not checked.**

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/pagesize.png)

### Ship Body

Let's start by drawing an ellipse... (Tip. Don't worry about the size. We can change it later.)

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship1.png)

Set the color to whatever you want. Feel free to play around with the different color and border effects.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/color.png)

I want the bottom of my ship to look a little more pointy, so to do that, I'll need to edit the points on my ellipse.
The ellipse is made of 4 points.
To edit them, double click on the ellipse.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship2.png)

You can now see the 4 points (...white circles).
Click on the bottom most point and edit it to look like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship3.png)

When you're done, just click anywhere on screen to exit the points edit mode.

### Cockpit

To create the cockpit, just draw a couple more ellipses, one on-top of the other.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship4.png)

### Wings

First create one wing.
This one was created using just a rectangle and a rounded rectangle.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship5.png)

Next, we'll select the wing and duplicate it by right clicking and selecting "Duplicate"... (Tip. To select multiple objects, you can either drag a selection box or hold shift and click)

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship6.png)

Flip the wings horizontally...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship7.png)

...then position it on the other side of the ship.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship8.png)

### Tail

The tail isn't a regular shape, so we'll be drawing it with the pen tool.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/pen.png)

With the pen tool selected, click to draw this shape...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship9.png)

Then with the tail selected, set the background color and remove the border.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/color2.png)

Your ship should now look like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship10.png)

Duplicate the tail, flip it, then place it on the other side.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship11.png)

### Scaling

Select the entire ship and scale it to an appropriate size.
You won't want a ship that's as big as the entire screen!
Something like this should be fine...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/ship12.png)

Exporting Images
===
To use your image in your game, you'll need to export it.

**Important: We will export the image twice!**

Select your ship and click the **"Export"** button.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/export.png)

### SVG

First, we'll export it to SVG format.
Change the settings to **Selection** and **SVG**, then click **"Download"**".

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/svg.png)

Drag the downloaded file from your browser into your your game's images folder.

The SVG format won't be directly used in your game, but will be used if you need to edit your ship in the future.

### PNG

Next, change the settings to **Selection** and **PNG**, then click **"Download"**".

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/png.png)

Again, drag the downloaded file from your browser into your your game's images folder.

Make sure you change the names of both the svg and png files to something suitable.
**The filenames must not contain spaces, capital letters, or special characters other than underscore.**
In this case, I would recommend using "player_ship" as a filename.