Animation
===
In Scratch, you can make your sprites animate by changing its costumes. In Pygame Zero, we do the same by changing the images. One way to do this is...

```
def update():
    if runner.image == 'run__000':
      runner.image == 'run__001'
    elif runner.image == 'run__001':
      runner.image == 'run__002'
    elif runner.image == 'run__002':
      runner.image == 'run__000'
```

This checks what is the current image and switches to the next one. It works, but it's a lot more troublesome than Scratch. To help with this, we can use the [Pygame Zero Helper](https://www.aposteriori.com.sg/pygame-zero-helper) module.

Pygame Zero Helper
===
First, download it from [here](https://www.aposteriori.com.sg/pygame-zero-helper/).

Next, open up the downloaded zip file and copy the ```pgzhelper.py``` file that's inside. Paste it into your ```ninja_runner``` folder.

Finally, we need to load the ```pgyhelper.py``` module. Add ```from pgzhelper import *``` to your Python game file. It should now look like this...

```
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

pgzrun.go() # Must be last line
```

Save and run it, just to make sure that everything is done correctly.

Ninja Images
===
Before we can start programming our ninja, we need to put the ninja images in the ```images``` folder.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/run__000.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/run__002.png)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/run__004.png)

Go to the image_pack that you have downloaded previously, and look for the ```ninja``` folder. Inside, you can find many run images, ranging from ```run__000``` to ```run__009```. Copy all of the run images from the ninja folder and paste them into your own images folder.

**Options: There are many other sets of running images that you can use. Try ```dino```, ```knight```, or ```zombies```.**

Programming the Ninja
===
We'll add in the ninja into our game using...

```
runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images
```

This is what each line does...

```runner = Actor('run__000')``` : This creates a new ```Actor``` using the first run image. It's the same as what we have done in our gem catcher game.

```run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']``` : This creates a new list in the variable ```run_images```. The list is filled with the names of the run images. If you are not using the ninja, you will need to change these names.

```runner.images = run_images``` : This tells our ```Actor``` to use the images in ```run_images``` for its animation.

We'll also need to add ```runner.draw()``` into the ```draw()``` function. Once completed, your program should look like this...

```
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

runner = Actor('run__000')
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
runner.images = run_images

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
  runner.draw()

pgzrun.go() # Must be last line
```

That should display your ninja on screen, but it's not running yet! Add in the update function like this...

```
def update():
  runner.next_image()
```

This tells Pygame Zero to switch to the next image everytime it updates. With this, you should now have a running ninja!

### Adjusting Position
You can adjust the position of the ninja using ```runner.x``` and ```runner.y```. Try the following...

```
runner.x = 100
runner.y = 400
```

**Try: Adjust the position of the ninja by changing ```runner.x``` and ```runner.y``` until you have her at the position you want.**