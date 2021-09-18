# What's Next?

We kept this game simple as it is meant to be a basic introduction to GDevelop.
Once you're done with this tutorial, you can move on to another tutorial to learn how to make a different type of game, or you can try some of the following challenges to practice and improve your understanding of GDevelop.

### Bug Fix 1. Remove Enemy

In our game, we add a new enemy every 1 second, but we never remove the enemy!
The enemy may leave the screen (...so we don't see it), but it's still in the game, consuming CPU time and memory.
It's generally not a big problem as a modern computer can easily handle thousands of enemies without slowing down, but it's good practice to remove it when it's no longer needed.
This is particularly important if we have a more complex games where we might end up with so many off-screen objects that it ends up slowing down the computer.

**TIP** There is a **Is On Screen** behavior that you can add to the enemy.
Once added, you'll have a new condition to detect if an enemy is on-screen, and you can use that condition to delete the enemy when it is off-screen.

### Challenge 1. Random direction

Instead of always moving straight, make the direction of the enemy random.

**TIP** Instead of setting the force using a speed on the X and Y axis, you can also set the force using an angle and speed.

### Challenge 2. Variable Speed

Make the speed of the enemy variable, such that some are faster while others are slower.

### Challenge 3. Add a Background Image

Right now our game uses the default gray background.
Try adding a new object and using it as a background image.

**TIP** You may need to adjust the **Z Order** property to move the background object behind the other objects.
Alternatively, you can create a new layer (...we haven't learned this yet), move it below the base layer, then place the background object in this new layer.

**Explore** You can play around with adding **Effects** to the background object.
Try the **Reflection** effect.

### Challenge 4. Translucent Buttons

If your player move under the buttons, it may be covered by it.
Make the buttons translucent, so that you can see through it.

**TIP** There is an action for changing opacity.

### Challenge 5. Different Enemies

Our current game only have a single type of enemy.
Can you add in more types of enemies?