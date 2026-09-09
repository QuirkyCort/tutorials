Drawing with Loops
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Finally, we are back to turtles! Let's start with a program that draws a octagon (8 sides)...

<div class="skulpt_box">
import turtle

turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
</div>

That's a lot of forward and left! An octagon has 8 sides, so we need to repeat that 8 times. Can we use a **for** loop to shorten the program? Here's an example using a **for** loop...

<div class="skulpt_box">
import turtle

for a in range(8):
    turtle.forward(40)
    turtle.left(45)
</div>

The **range** will generate a list with 8 items, so the **for** loop will repeat 8 times. Each time, we will make the turtle go forward and turn left by 45 degrees. We are not using the variable ```a```, so you can just ignore it.

### Ex 1. Other shapes (part 2)
In an earlier challenge, we drew different shapes using the turtle module. Let's do that again, but this time, use a **for** loop to simplify it. Can you draw...

* Triangle
* Square
* Pentagon (5 sides)
* Hexagon (6 sides)

<div class="skulpt_box">
</div>


### Ex 2. Any shapes
Can you write a program that asks the user for a number, then draw a shape with that number of sides? Here's a hint: The ```turn``` command should use an angle that is equal to ```360 / number_of_sides```. The first line has been written for you.

<div class="skulpt_box">
number_of_sides = input("How many sides?")
</div>
