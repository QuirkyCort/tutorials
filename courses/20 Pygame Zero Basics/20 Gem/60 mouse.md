Mouse Controls
===
We can also modify our game to make it work with the mouse. Like Scratch, Pygame Zero is events based. This means that when certain events occurs (eg. a mouse button is pressed), Pygame Zero will run the corresponding function (eg. ```on_mouse_down```).

To detect mouse movement, we can use the ```on_mouse_move(pos, rel, buttons)``` function. Try adding this to your game...

```python
def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
```

The purpose of the 3 parameters are...

```pos``` : This provides the position of the mouse. You can get the x position using pos[0] and the y position using pos[1].

```rel``` : This provides the change in position since the last mouse move. rel[0] is the change in x position and rel[1] the change in y position.

```buttons``` : This provides a list of mouse buttons that are pressed. For example, if you want to check if the left button is pressed...

```python
def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
        print('left click')
```

***This is just an example. Don't add it to your game***

Other Events
===
Besides mouse move, there are also other functions that will be run by Pygame Zero when their corresponding events occurs. They are...

**on_mouse_down(pos, buttons)** : Run when a mouse button is pressed.


**on_mouse_up(pos, buttons)** : Run when a mouse button is released.

```pos``` : This provides the position of the mouse. You can get the x position using pos[0] and the y position using pos[1].

```buttons``` : This provides a list of mouse buttons that are pressed.

**on_key_down(key, mod, unicode)** : Run when a keyboard key is pressed.

**on_key_up(key, mod)** : Run when a keyboard key is release.

```key``` : An integer indicating the key that was pressed. See the [Pygame Zero website](https://pygame-zero.readthedocs.io/en/stable/hooks.html#buttons-and-keys) for a full list of keys.

```mod``` : A bitmask of modifier keys that were depressed. You can check them as follows...

```python
def on_key_down(key, mod, unicode):
    if mod & keymods.LSHIFT:
        print('Left shift button pressed')
```

```unicode``` : Where relevant, the character that was typed. You can check it like this...

```python
def on_key_down(key, mod, unicode):
    if unicode == 'e':
        print('e button pressed')
```
