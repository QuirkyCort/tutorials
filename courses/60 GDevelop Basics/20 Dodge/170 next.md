# What's Next?

We kept this game simple as it is meant to be a basic introduction to GDevelop.
Once you're done with this tutorial, you can move on to another tutorial to learn how to make a different type of game, or you can try some of the following challenges to practice and improve your understanding of GDevelop.

### Bug Fix 1. Remove Enemy

In our game, we add a new enemy every 1 second, but we never remove the enemy!
The enemy may leave the screen (...so we don't see it), but it's still in the game, consuming CPU time and memory.
It's generally not a big problem as a modern computer can easily handle thousands of enemies without slowing down, but it's good practice to remove it when it's no longer needed.
This is particularly important if we have a more complex games where we might end up with so many off-screen objects that it ends up slowing down the computer.

<div class="tip" markdown="span">
There is an **Destroy when outside of screen** behavior that you can add to the enemy.
</div>

### Challenge 1. Random direction

Instead of always moving straight, make the direction of the enemy random.

<div class="tip" markdown="span">
Instead of setting the force using a speed on the X and Y axis, you can also set the force using an angle and speed.
</div>

### Challenge 2. Variable Speed

Make the speed of the enemy variable, such that some are faster while others are slower.

### Challenge 3. Add a Background Image

Right now our game uses the default gray background.
Try adding a new object and using it as a background image.

<div class="tip" markdown="span">
You may need to adjust the **Z Order** property to move the background object behind the other objects.
Alternatively, you can create a new layer (...we haven't learned this yet), move it below the base layer, then place the background object in this new layer.
</div>

<div class="info" markdown="span">
You can play around with adding **Effects** to the background object.
Try the **Reflection** effect.
</div>

### Challenge 4. Translucent Buttons

If your player move under the buttons, it may be covered by it.
Make the buttons translucent, so that you can see through it.

<div class="tip" markdown="span">
There is an action for changing opacity.
</div>

### Challenge 5. Different Enemies

Our current game only have a single type of enemy.
Can you add in more types of enemies?

### Challenge 6. Behaviors

Play around with the available behaviors.
Some of them may be useful in providing interesting effects for your game.

## Demo

Here's an example with the challenges implemented.

<iframe width="800" height="600" src="https://games.accelerateworkshop.com/dodgeAdv/" title="Dodge the Creep" frameborder="0" allowfullscreen></iframe>

[Click here to play the game in a page of its own.](https://games.accelerateworkshop.com/dodgeAdv)
