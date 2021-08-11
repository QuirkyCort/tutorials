Player Bullets
===
Let's use [Vectr](https://vectr.com/) to draw the bullet.

The first step is to open the player ship image.
This is optional, but it helps me gauge a suitable size for the bullet.
Click on the "Upload image" button...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/upload.png)

...and select your player ship image.

Next, we are going to draw the bullet.
I'm just going with a simple circle this time.

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/player_bullet.png)

Since you already know how to use Vectr, I'll leave it to you to decide how you'll like your bullet to look.
Due to the way Pygame detects collisions, its recommended to keep your images close to either a circle or a square.

If your bullet is not symmetrical in all directions, make sure it is **pointed to the right, not the top**. Kind of like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2021/01/bulletblue2.png)

### Export
Same as before, make sure to export your bullet to both svg and png formats.
Make sure you give the downloaded files a suitable name and put them in the game's images folder.

Adding bullets to the game
===

We want to create a new bullet everytime we press the space bar. Since we can have more than one bullet at a time, we'll use a list to hold all our bullets. Start by creating an empty list...

```
bullets = []
```

Next, in **update()**, check if the space key is pressed and add a bullet if it is.

```
if keyboard.space:
    bullet = Actor('player_bullet')
    bullet.x = player.x
    bullet.y = player.y
    bullet.angle = 90
    bullets.append(bullet)
```

We set the bullet angle to be 90, so that it'll point upwards. We also set the x and y of the bullet to be the same as the player, so that the bullet will start from the player.

Don't forget to draw the bullets in the **draw()** function...

```
for bullet in bullets:
    bullet.draw()
```

When you try out the program, you'll see a bullet created each time you press the space bar. But the bullet just stays there and don't do anything, so next, we'll make the bullet fly.

Moving the Bullet
===

### pgzhelper
In our previous programs, we are moving the bullet by changing x and y. That works, but only if we are moving horizontally or vertically. What if we need the bullet to move at an angle? We won't be doing that now, but once power-ups are added, we will have some bullets that are moving at an angle.

To solve this, we can use some simple trigonometry (...sin, cos), but since you probably haven't learnt that yet, we'll solve it using Pygame Zero Helper.

* Download [Pygame Zero Helper](https://www.aposteriori.com.sg/pygame-zero-helper/) zip file.
* Extract the Python file inside
* Place the extracted Python file in your game folder

First thing to do is to import the Pygame Zero Helper module. Add this to your program, just under "import pgzrun".

```
from pgzhelper import *
```

This will provide us with the ```move_forward``` method on the Actor.

### Updating position

We should move the bullet in the **update()** function. Using a **for** loop.

```
for bullet in bullets:
    bullet.move_forward(15)
```

### Removing Bullet
As it is, your ship should be able to shoot bullets, but these bullets lasts forever. They will continue to exists even if they are outside of the screen! To prevent that, we should remove bullets that has left the screen.

```
for bullet in bullets:
    bullet.move_forward(15)
    if bullet.y < 0:
        bullets.remove(bullet)
```

```bullets.remove(bullet)``` simply removes **"bullet"** from the **"bullets"** list.

Hold-Off
===
Now our bullet looks more like a laser! That's because when we press the space bar, it creates a LOT of bullets very rapidly. We should add a hold-off. This is some code that stops the player for shooting for a while after each bullet. We'll start by creating a new variable.

```
bullet_delay = 0
```

Then modify our shoot code...

```
if keyboard.space and bullet_delay == 0:
    bullet_delay = 5
    bullet = Actor('player_bullet')
    bullet.x = player.x
    bullet.y = player.y
    bullet.angle = 90
    bullets.append(bullet)

if bullet_delay > 0:
    bullet_delay -= 1
```

There is also a bullet hold-off in the tank game, but it was implemented differently. In programming, there are many ways to solve a problem. Can you compare the two and figure out the good and bad of each of these implementations?

If you try to run the code now, you'll get an error. Do you know why? See if you can figure out what's missing!

What the above code does is...

```if keyboard.space and bullet_delay == 0:``` Only fire if space key is pressed **and** bullet_delay is 0.

```bullet_delay = 5``` Set the bullet_delay to 5. This will prevent firing since it is no longer zero. You can try changing this value and see what effects it has.

```
if bullet_delay > 0:
    bullet_delay -= 1
```

If the bullet_delay is greater than zero, we'll decrease it by one. This will gradually reduce it until it reaches zero again.

Your code should now look like this...

```
import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

player = Actor('player')
player.x = 400
player.y = 500

bullets = []
bullet_delay = 0

def update():
    global bullet_delay
    
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.right:
        player.x += 5
    if keyboard.left:
        player.x -= 5

    if player.x < 25:
        player.x = 25
    if player.x > 775:
        player.x = 775
    if player.y < 30:
        player.y = 30
    if player.y > 570:
        player.y = 570

    if keyboard.space and bullet_delay == 0:
        bullet_delay = 5
        bullet = Actor('player_bullet')
        bullet.x = player.x
        bullet.y = player.y
        bullet.angle = 90
        bullets.append(bullet)

    if bullet_delay > 0:
        bullet_delay -= 1

    for bullet in bullets:
        bullet.move_forward(15)
        if bullet.y < 0:
            bullets.remove(bullet)

def draw():
    screen.clear()
    player.draw()
    for bullet in bullets:
        bullet.draw()

pgzrun.go() # Must be last line

```

### What's missing?
We need to add ```global bullet_delay```.

The **bullet_delay** variable is declared outside of the update() function, but we are trying to write it from inside the update() function. In Python, we can read variables that are outside a function (...these are called global variables), but cannot write to them unless we declare them as global inside the function.