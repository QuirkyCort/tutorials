Making it harder
===
Right now the game is too easy. Not to brag, but I can score over 300 without breaking a sweat. Let's make it harder by making the gem fall faster the higher your score is.

Look for this line...

```python
gem.y = gem.y + 4
```

...and change it to this...

```python
gem.y = gem.y + 4 + score / 5
```

This will increase the falling speed as your score goes up. When your score is zero, the gem will fall at speed 4. When your score is 10, the gem will fall at speed 6 (4 + 10 / 5).