Introduction
==
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Welcome to the **Introduction to Python** program! Python is a programming language, kind of like Scratch which many of you have learned. Unlike Scratch, Python requires you to type in text like this...

```
a = "Hello "
b = "World"
print(a + b)
```

...and it doesn't like it if you make any spelling errors.

```
a = "Hello "
b = "World"
prind(a + b)  # This will not work because "print" was spelled incorrectly!
```

Python also cares about whether you are using UPPERCASE letters, or lowercase letters. So this will work...

```
print("Hi!")
```

...but this will not...

```
Print("Hi!")
```
Notice the capital 'P'? Python requires **print** to be spelled with only lowercase letters.

ALl these may make Python a little harder to start with compared with graphical programming languages like Scratch, but once you have learned it well, you can use Python to create games, websites, robots, and many more!

---

Most basic program
===
What you see below is a Python **trinket**.
The area on the left is the **code editor**; It allows you to type in and run Python code.
On the right is the **terminal**; It shows you the output from your program.

<div class="skulpt_box" console_only>
print("Hello World")
</div>

This program will **print** the string "Hello World" to the output, and you can see the result on the right. In Python, **print()** is a function that outputs whatever you put inside the brackets. **"Hello World"** is a string. A string is a word or sentence. To tell Python that it is a string, we enclose it with quotation marks "".

Let's make the program a little more complicated.
Edit the code in the **code editor** above, and change it to look like this...

```
print("Hello")
print("Cort")
print("How are you today?")
```

...then click the **"Run"** button to run the program.

Python will run your commands in **sequence**. This means that it will run the first line, then the second line, then the third line, and so on....

***Tips : *** *To get back the original code, click on the ☰ icon on the left of the trinket, and select Reset*
