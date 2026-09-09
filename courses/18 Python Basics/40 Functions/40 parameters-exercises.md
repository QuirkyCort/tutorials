Parameters Exercises
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Now that we know how to use parameters, we can use that to make our earlier functions more capable. Here's an example...

<div class="skulpt_box">
import turtle

def square(size):
    for a in range(4):
        turtle.forward(size)
        turtle.left(90)
    
square(10)
turtle.forward(50)
square(20)
turtle.forward(50)
square(40)
</div>

### Ex 1. Shapes with parameters

Create functions for the following shapes, but with a `size` parameters. The first one is done for you...

* Square
* Triangle
* Pentagon
* Hexagon

*Hint: You can copy the program you have written in the previous exercise.*

<div class="skulpt_box">
import turtle

def square(size):
    for a in range(4):
        turtle.forward(size)
        turtle.left(90)
    
square(50)
</div>

### Ex 2. Houses

Create a function that draws a house that looks like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/house.png)

Then use it to create a row of houses like this...

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/houses.png)

We've prepare the start of the program for you...

<div class="skulpt_box">
import turtle

def house(size):
    turtle.forward(size)

house(50)
</div>