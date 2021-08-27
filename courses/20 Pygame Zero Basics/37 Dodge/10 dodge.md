# Dodge the Creep

**Dodge the Creep** is based on a [Godot](https://godotengine.org/) tutorial. Godot is a professional quality game engine used to create both 2D and 3D games, but we'll be using Python and Pygame Zero to make our own version. You can see a video of the Godot version of Dodge the Creep here..

<iframe width="560" height="315" src="https://www.youtube.com/embed/uPoLKQG0gmw?start=19" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Pygame Zero is easier to use than Godot, but isn't as powerful. It'll be difficult to achieve the same level of quality, but we will aim to achieve roughly the same gameplay.

In this game, the player must dodge the incoming monsters and survive for as long as possible. The guided part of the game will be deliberately kept simple so everyone can follow along easily, but there will be some challenges at the end that you can try out to make the game more complete.

The background and the player movement part of this game is the same as in **Grab the Coin**, so if you're confident of handling it on your own, try writing it yourself then skip ahead to the **Enemies** section.

## New Project

To keep our files organized, we'll need to create a new folder for the new game.

### Windows

1) Open up file explorer

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/explorer.jpg)

2) Navigate to your flash drive or network drive, right click, and create a new folder.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/new-folder.jpg)

3) Name the new folder (...for this project, I recommend **dodge**)

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/new-folder-name.jpg)

### Images and Sounds

Within this new folder, we will need to create two more folders; **images** and **sounds**.

Your final folder structure should look like this...

```
dodge
\_ images
\_ sounds
```

We will put our Python game file in the **dodge** folder, our images in the **images** folder, and all music and sound effects in the **sounds** folder.

## IDLE

Look for this icon on your desktop. If it's not on your desktop, click the search icon on your taskbar (...looks like a magnifying glass) and search for **idle**.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/idle.jpg)

This should open up the IDLE window that looks like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/idle-window.jpg)

Click on **File** and **New File**. This will open a blank window for you to write Python code!

### Save

Click on **Save** and select the folder you have created earlier. Give your programe a file name (...I suggest **dodge.py**) and click **Ok**.