Lists
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

A **list** is a special type of variable. Normally, a variable can only hold a single value, but a list can hold **many values**.

This is an example of a list...

<div class="skulpt_box" console_only>
a = ["cat", "dog", "monkey", "elephant"]
print(a[2])
</div>

```a = ["cat", "dog", "monkey", "elephant"]``` : Set the values for a list. It needs to start and end with the square brackets **[]**, and each item is separated by a comma **,**.

```print(a[2])``` : Prints the value of index 2 in the list. The **index starts from zero**, so index 2 is actually the third item.

### Try

Can you modify the program to output **cat** instead?

Using a variable as index
===
Lists are most useful when you use a variable for the index. Here's an example...

<div class="skulpt_box" console_only>
animals = ["cat", "dog", "monkey", "elephant"]

choice = input("Choose a number from 0 to 3")
choice = int(choice)

print("Your favourite animal is a " + animals[choice])
</div>

Random
===
We can generate a random number using the **random** module. Combine that with the use of a variable as the index allows us to choose a random item from a list.

<div class="skulpt_box" console_only>
import random

style = ["fried", "baked", "steamed"]
food = ["chicken", "fish", "ice cream", "tofu"]

choice1 = random.randrange(3)
choice2 = random.randrange(4)

print("We are having " + style[choice1] + " " + food[choice2] + " for dinner.")
</div>
