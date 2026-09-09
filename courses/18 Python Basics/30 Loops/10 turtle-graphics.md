Import and Turtle
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Just as cooks don't catch their own fish and teachers don't write their own textbooks, programmers don't create their entire program themselves. Instead, they rely on **modules** that are written by others to help provide added capabilities.

In this lesson, we'll be learning to use the **turtle** module. The turtle module is used to do simple drawings. Try out the following...

```
import turtle

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
```

<div class="skulpt_box">
</div>

This is what each of the line does...

```import turtle``` : Load the **turtle** module, allowing us to use it in our program.

```turtle.forward(50)``` : Run the **forward** function in the **turtle** module. Moves forward by 50 steps.

```turtle.left(90)``` : Run the **left** function in the **turtle** module. Turn left by 90 degrees.

### Challenge 1. Complete the Square

Here's the first challenge. Modify the program above to make the turtle complete drawing the square.

### Challenge 2. Experiment!

Experiment with the following functions. See if you can figure out what they do!

```
turtle.right(45)
turtle.pendown()
turtle.penup()
turtle.color('lightgreen')
```

### Challenge 3. Other shapes

What other shapes can you draw? Can you draw...
* Triangle
* Square
* Rectangle
* Pentagon (5 sides)
* Hexagon (6 sides)
