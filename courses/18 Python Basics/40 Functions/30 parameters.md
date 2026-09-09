Parameters
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

Functions can also have inputs, called **parameters**. We have already used functions with paramentes before! When we run `print("Hello World")`, we are running the **print** function with the parameter **"Hello World"**. Here's how to create a function with a parameter.

<div class="skulpt_box" console_only>
def make_something(thing):
    print("Here's your " + thing)
    
make_something("cake")
make_something("ice cream")
make_something("ice kachang")
</div>

In the above example, `thing` is a special variable. It contains the input provided when we run `make_something` and it only exist inside the `make_something` function.

We can also have more than one parameters. To do so, separate them with a comma `,`. Here's an example.

<div class="skulpt_box" console_only>
def make_many_things(thing, number):
    for a in range(number):
        print("Here's your " + thing)
    
make_many_things("cake", 3)
</div>