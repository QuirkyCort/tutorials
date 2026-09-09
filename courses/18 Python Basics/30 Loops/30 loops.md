Loops
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Another thing we can do with a list, is to **iterate** through it using a loop. This means that we will repeat some steps, once for each item in the list. Here's an example...

<div class="skulpt_box" console_only>
members = ["Tony", "Steve", "Odinson", "Bruce", "Natasha", "Clint"]

for name in members:
    print("Hi " + name + ", please come to my party!")
</div>

The **for** loop will repeat the **print** command, once for every item in members. Each time it repeats, it will assign the next value in **members** into the **name** variable.

Range
===
List don't need to contain only strings, they can also contain numbers like this...

<div class="skulpt_box" console_only>
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for b in a:
    print(b)
</div>

The above program will run the **print** command 10 times, starting from zero and ending with 9. But what if we need it to run 100 times? Do we need to type out ```a = [0, 1, 2, 3, 4...``` all the way until 100?

Python provides a shortcut! We can use the **range** function to generate a list of numbers. Try replacing the above program with the code below...

```
for b in range(10):
    print(b)
```

Did that work? When we use ```range(10)``` it generates a list of 10 numbers, starting from zero and ending at 9. If we use ```range(100)``` it will generate a list of 100 numbers, starting from zero and ending at 99. This is particularly useful when we need to repeat something many times.

### Challenge 1. 
Do you remember your multiplication tables? Write a program that can generate the multiplication table for any numbers up until 100. I've written part of it for you, but it's incomplete and filled with errors! Can you fix and complete it?

<div class="skulpt_box" console_only>
number = input("Choose a number")

for a in [0, 1, 2, 3]:
    print(number + " x " + a + " = " + number * a)
</div>

This is what the result should look like...

```
Choose a number 5
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5 x 11 = 55
.
.
.
.
```