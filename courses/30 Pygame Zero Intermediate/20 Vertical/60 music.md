Music and Sound
===
Adding some sound makes the game more interesting. If you like, you can create and record the sound effects on your own...

<iframe width="560" height="315" src="https://www.youtube.com/embed/k2yAfoHfHIw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

...or you can look for free sound effects that you can download online.

To save time, I have compiled a pack of sound effects and music that you can use in your game. Download it [here](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/sound_pack.zip).

If you prefer to use your own sound, that's ok too. For a start, we want a...

* Shooting sound (...pew pew)
* Background music

When you have selected something suitable, put the selected files in the **sounds** folder of your game. The same rules on filenames apply; no spaces, no capital letters, and no special characters other than underscore. If the filename of your sound does not meet these rules, make sure to rename it.

### Pew Pew

The first sound that I'm adding is the shooting sound. I've selected the file **sfx_sounds_interaction25.wav** (...that's for me. you can use a different sound). I'm going to make this sound play everytime we fire a bullet.

To play a sound, we need to add a Python statement that looks like this...

```python
sounds.sfx_sounds_interaction25.play()
```

**sounds** : This means to use the sounds object that is provided by Pygame Zero.

**sfx_sounds_interaction25** : This is the name of my sound file. You may have a different filename, so change this accordingly. You don't need to include the file extension.

**play()** : This tells it to play once. If you provide a number in the parameter (eg. ```play(3)```), it will repeat the sound for that number of times. You can also set it to -1 if you want it to repeat forever.

Since this sound should play when we shoot a bullet, we'll put it under the code where we detect the space key...

```python
if keyboard.space and bullet_delay == 0:
    sounds.sfx_sounds_interaction25.play()
    .
    .
    .
```

### Music

Playing music is done the same way as the shooting sound. The only difference is that we want the music to repeat forever, so we'll use ```play(-1)```.

I'm using the file **main_theme.wav** which is not from your sound pack. I found this on [OpenGameArt](https://opengameart.org/), which is a popular site for finding game assets. As before, you can pick a suitable music from your sound pack, or find a suitable music online.

**Before you ask...** No. I will not help you download music from YouTube or Spotify.

To play the music and make it repeat forever, we need to add...

```python
sounds.main_theme.play(-1)
```

This should start right from the beginning of the game, so put it **outside** of the update and draw functions. If you put it inside either the update or draw function, it will start everytime these functions run (...which is around 60 times per second), and will sound terrible.