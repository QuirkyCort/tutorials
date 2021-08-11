TwinBee
===
For this game, we'll be using **TwinBee** as our inspiration.

TwinBee is a **vertical-scrolling shoot 'em up** arcade game made in 1985.
While it may not be the most famous example of its genre, it is one of the most successful (...and cutest).

<iframe width="560" height="315" src="https://www.youtube.com/embed/HgKMtl-_gW4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this game, the background and enemies will be scrolling from top down.
The player's ship can move in all directions, but always faces and shoots upwards.

This is how my game looks like when it is completed.

<iframe width="560" height="315" src="https://www.youtube.com/embed/tykMXG-5aLU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

How your game will turn out depends on you, but we'll be teaching you how the above game was built. With a little effort and inspiration, you can easily create something better than that!

New Project
===
To keep our files organized, we'll need to create a new folder for the new game.

### Windows
1) Open up file explorer

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/explorer.jpg)

2) Navigate to your flash drive or network drive, right click, and create a new folder.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/new-folder.jpg)

3) Name the new folder (...for this project, I recommend **tank_game**)

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/new-folder-name.jpg)

### Images and Sounds
Within this new folder, we will need to create two more folders; **images** and **sounds**.

Your final folder structure should look like this...

```
tank_game
\_ images
\_ sounds
```

We will put our Python game file in the **tank_game** folder, our images in the **images** folder, and all music and sound effects in the **sounds** folder.

**Important** : This game uses a wall image that isn't in the previous image pack. I've prepared a mini-image pack [here](https://www.aposteriori.com.sg/wp-content/uploads/2020/09/tank_game_images.zip) that contains the images you'll need for this game. Put all of these images into your **images** folder.

IDLE
===
Look for this icon on your desktop. If it's not on your desktop, click the search icon on your taskbar (...looks like a magnifying glass) and search for **idle**.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/idle.jpg)

This should open up the IDLE window that looks like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/idle-window.jpg)

Click on **File** and **New File**. This will open a blank window for you to write Python code!