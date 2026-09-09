Functions with Turtles
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Let's use functions to simply our turtle drawing programs.

<div class="skulpt_box">
import turtle

def square():
    for a in range(4):
        turtle.forward(50)
        turtle.left(90)
    
square()
turtle.forward(100)
square()
</div>

Here we created a `square` function that draws a square. We can run this function as many times as we like using the `square()` command.

### Challenge 1. Family of shapes

In the trinket below, write a program that contains the following functions...

* square
* triangle
* pentagon
* hexagon

The first one has already been done for you.

<div class="skulpt_box">
import turtle

def square():
    for a in range(4):
        turtle.forward(50)
        turtle.left(90)
    
square()
</div>
