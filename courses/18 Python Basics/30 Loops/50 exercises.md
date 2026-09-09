More Fun with Turtles
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

### Wrong Angles
In the last exercise, we told you that the angle of turn is equal to ```360 / number_of_sides```. What happens if you use the wrong angle?

<div class="skulpt_box">
import turtle
turtle.speed(10)

for a in range(100):
   turtle.forward(100)
   turtle.left(92)   # Try a different angle and see the effect!
</div>

Here we are repeating 100 times, so to speed things up, we are using the **speed** function.

```
turtle.speed(1)   # Slowest speed
turtle.speed(6)   # Normal speed
turtle.speed(10)  # Very fast
turtle.speed(0)   # Fastest speed
```

### Ex 1.
Modify the program to make it change color as it draws each line. You may use any colors you like.

### Ex 2.
In the above program, we didn't use the variable ```a```. Try using it in the loop, by replacing the ```forward(100)``` with ```forward(a)```. How else can you use ```a``` in the loop?

### Circles
We can also draw circles using the **circle** command...

<div class="skulpt_box">
import turtle

turtle.circle(50)
</div>

### Ex 3.
Write a program to draw this figure...

![Loops 1](https://www.aposteriori.com.sg/wp-content/uploads/2020/01/loop1.png)
Hint: You should use a loop.

### Ex 4.
This one is a little harder...

![Loops 2](https://www.aposteriori.com.sg/wp-content/uploads/2020/01/loop2.png) 
Hint: You should use a loop, as well as the **up** and **down** commands.
