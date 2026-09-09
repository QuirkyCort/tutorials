Exercises
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Let's do some exercises to enhance your understanding.

### Ex 1. Fix the box
This program doesn't work correctly. Can you fix it?

<div class="skulpt_box">
import turtle

for a in 3:
    turtle.forward(100)
    turtle.left(90)
</div>

### Ex 2. Many triangles
This program doesn't work correctly. Can you fix it?

<div class="skulpt_box">
import turtle

number = input("How many triangles do you want?")

for a in range(number):
    for a in range(3):
        turtle.forward(20)
        turtle.left(120)
    turtle.forward(30)
</div>

### Ex 3. Sharing pizzas
Can you make this program work correctly? (Each pizza has 6 slices.)

<div class="skulpt_box" console_only>
pizzas = input("How many pizzas do we have?")
students = input("How many students are in class?")

slices = pizzas * 6
slices_per_student = slices / students

print("Each student gets " + slices_per_student + " slices of pizzas.")
</div>

### Ex 4. Draw a house
Write a program that draw the following house. Some of it has been done for you.

![](https://www.aposteriori.com.sg/wp-content/uploads/2020/02/house-1.png)

<div class="skulpt_box">
import turtle
</div>