Comments
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

This is the most useless part of the course! We are going to learn how to write code that does nothing!

**Comments** are lines in your program that doesn't do anything. Python will ignore these lines completely.

<div class="skulpt_box" console_only>
# This line is a comment
print("Good Morning")
#print("Good Afternoon")
print("Good Evening")
</div>

Lines that starts with a **hash** character (**#**), are called **comments**. Python will ignore these lines completely, so you can write whatever you want in them.

Can you change the above programme using **hash**, so that it only says **Good Morning**?

---

In-Line Comments
===
You can also add a comment to the end of a line, like this...

<div class="skulpt_box" console_only>
print("Good Day!")   # This is a comment
</div>

...and Python will ignore everything that comes after the **hash**.

---

Why use comments?
===
When we write programs, we may sometimes get confused or forget what a piece of code is suppose to do. Comments are used as a way to keep notes on our programs. Python may ignore it, but it can be very useful to any humans reading your program (...and this includes yourself!).