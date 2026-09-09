Variables
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Here's an empty trinket...

<div class="skulpt_box" console_only>
</div>

Type in the following, **Run** it, and see what happens.

```
a = 1
b = 2
print(a + b)
```

What output did you get? Was it a 3? Congratulations! You have just done algebra (...or at least you had Python do it for you...)!

Let's look at what you just did...

```
a = 1   # This creates a variable named "a" and gave it the value of 1
b = 2   # This creates another variable named "b" and gave it the value of 2
print(a + b)  # Finally, we tell Python to add "a" and "b", then print the result
```

**Variables** stores **values**. This can be a number or a string. When we give a variable a value, Python will remember it for us. We can then use the variable in place of the value.

Here's another empty trinket...

<div class="skulpt_box" console_only>
</div>

Type in the following, **Run** it, and see what happens.

```
print("Hi there!")
a = "Hi there!"
print(a)
```

In the above program, both of the ```print``` lines do the same thing. In the first ```print```, we told Python to output ```"Hi there!"```, while in the second ```print``` we first store the value of ```"Hi there!"``` in a variable ```a``` then tell Python to output the value of ```a```.

We can do math with variables as well! Try the following

```
a = 2
b = 3
c = a + b
print(c)

a = 5
b = a * 2
print(b)
```

We can also use variables with strings!

```
a = "Hello"
b = "World"
print(a + b)
```

Now that probably didn't come out right. Can you add a space in between "Hello" and "World"?