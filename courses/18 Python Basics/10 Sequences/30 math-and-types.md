Maths
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Python can do maths too!

<div class="skulpt_box" console_only>
print(3 + 5)
</div>

Try changing the ```3 + 5``` in the above program into different math formulas, such as...

```
4 + 1
9 - 2
2 * 3
10 / 2
```

...and remember to click **Run** after making your changes to see the result.

Can you figure out what each operator does?

```
4 + 1   # This is 4 plus 1
9 - 2   # This is 9 minus 2
2 * 3   # This is 2 times 3
10 / 2  # This is 10 divide by 2
```

---

Types
===
Now, let's try something different...

<div class="skulpt_box" console_only>
print("one" + 1)
</div>

That gave an error. When errors occurs, it appears at the bottom of the trinket in red, and the line with the error is also highlighted in red.

Why didn't that work? Well, ```"one"``` is string, and strings are words and sentences. But ```1``` is a number. Trying to add a string and a number is like trying to add apple and oranges; it doesn't make sense!

Let's try changing it...

<div class="skulpt_box" console_only>
print("one" + "one")
print(2 + 2)
</div>

What do you get now? Try adding the line ```print("1" + 1)```, did that work? Remember that anything inside the quotation marks is a string; even if you were to put a number inside!

Try out the following one at a time (...erase everything first before adding the line) and see what happens. Remember to ```print()``` the result or you won't see any outputs!

```
"one" + "two"
"one" - "two"
"one" * "two"
"one" / "two"
"one" + 3
"one" - 3
"one" * 3
"one" / 3
```

