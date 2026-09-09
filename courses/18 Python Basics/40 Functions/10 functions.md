Functions
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Functions are like recipes, they store your Python instructions and allow us to reuse them again and again.

To create a function, we start with `def`, a function name, a pair of parentheses `()`, and a colon `:`. We then write the code we want below this line with an indent. Here's an example...

```
def make_a_cake():
    print("Here's your cake!")
```

The code above creates a function named `make_a_cake`, and the function contains the code `print("Here's your cake!")`. To run this function, we would type in the function name followed by the paretheses...

```
make_a_cake()
```

In our previous exercises, we have used `print()`, `turtle.penup()`, `turtle.forward()` and so on. These are all functions.

Here's a complete example...

<div class="skulpt_box" console_only>
def make_a_cake():
    print("Here's your cake!")
    
make_a_cake()
</div>

Once a function is created, we can run it multiple times...

<div class="skulpt_box" console_only>
def make_a_cake():
    print("Here's your cake!")
    
make_a_cake()
make_a_cake()
make_a_cake()
</div>

We can also have more than just print statements inside our function. Everything we have learned can be use in a function as well!

<div class="skulpt_box" console_only>
def count_to_three():
    for a in range(3):
        print(a + 1)
        
count_to_three()
</div>
