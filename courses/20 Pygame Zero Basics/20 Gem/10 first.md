First Program
===
This is the structure of a Pygame Zero program...

```
import pgzrun

WIDTH = 800
HEIGHT = 600

pgzrun.go() # Must be last line
```

The first line, ```import pgzrun```, loads the Pygame Zero module, and the last line, ```pgzrun.go()```, is a function that starts Pygame Zero. In the middle we have ```WIDTH = 800``` and ```HEIGHT = 600``` which sets the width and height of the game window.

Type the above into **IDLE** and press **F5** or click **Run -> Run Module** to run the program! **Try changing WIDTH and HEIGHT and see the effects.**

Actor
===
Now that wasn't very interesting, so let us add in a spaceship. To do so, we need to first provide an image for the spaceship. You can use any images you want, but to make it easy for you, I have prepared a zip file containing a variety of images. [Download it here](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/image_pack.zip).

Remember the **images** folder I told you to create inside your project folder? That's where your spaceship image need to go. Open the zip file, choose a suitable image, and copy it into the **images** folder. I'm using this image...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/playership1_blue.png)

**IMPORTANT: Your image filename must only contain lowercase letters, numbers and underscores.**

Once that is done, you can add the spaceship to your Python program...

```
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

def draw():
    ship.draw()

pgzrun.go() # Must be last line
```

This is what each line does...

```ship = Actor('playership1_blue')``` : Create a new **Actor** using the *playership1_blue* image file. If you are using a different file, you'll need  to change this.

```ship.x = 370``` : Set the x position of the ship to 370. **Try changing this!**

```ship.y = 550``` : Set the y position of the ship to 550. **Try changing this!**

```def draw():``` : This is a special function. We don't need to run it ourselves; Pygame Zero will run it for us regularly.

```ship.draw()``` : This tells the ship **Actor** to draw itself on the screen. It needs to be indented under ```def draw():```, so that  it will run whenever Pygame Zero run  the ```draw()``` function.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/xy.png)
