Solutions
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

### Ex 1.

<div class="skulpt_box">
import turtle
import random

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

turtle.speed(10)

for a in range(100):
    choice = random.randrange(4)
    turtle.color(colors[choice])
    turtle.forward(100)
    turtle.left(92)
</div>

### Ex 2.

<div class="skulpt_box">
import turtle
import random

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

turtle.speed(10)

for a in range(100):
    choice = random.randrange(4)
    turtle.color(colors[choice])
    turtle.forward(a)
    turtle.left(92)
</div>

### Ex 3.

<div class="skulpt_box">
import turtle

for a in range(20):
    turtle.circle(a * 5)
</div>

### Ex 4.

<div class="skulpt_box">
import turtle

for a in range(20):
    turtle.circle(a * 5)
    turtle.up()
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.down()
</div>
