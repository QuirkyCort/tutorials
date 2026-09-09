Using `if` and `else`
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

So far, Python has been pretty stupid. It always does the same thing! To let Python make decisions, we can use an ```if``` statement.

Try running this program in the trinket  below...

```
temperature = 35
if temperature > 30:
    print("It is a hot day!")
else:
    print("It is a cool day!")
```

<div class="skulpt_box" console_only>
</div>

To use an ```if``` statement, you start with an ```if```, ends with a ```:```, and indent the code you want to run conditionally. You can also add in an ```else```, which will run if the condition is false.

**IMPORTANT:** Make sure all your indents are at the same level!

Conditions
===
In the above program, the ```temperature > 30``` is the **condition**. We can use different types of conditions, try these out:

```
temperature < 30   # Temperature less than 30
temperature > 30   # Temperature greater than 30
temperature <= 30  # Temperature less than or equal to 30
temperature >= 30  # Temperature greater than or equal to 30
temperature == 30  # Temperature is exactly 30
temperature != 30  # Temperature not equal to 30
```

**IMPORTANT:** Note that we use ```==``` and not ```=``` when comparing if it is equal.

We can also compare two variables like this...

<div class="skulpt_box" console_only>
tom_age = 12
jerry_age = 11

if tom_age > jerry_age:
    print("Tom is older")
else:
    print("Jerry is older")
</div>

Conditions with Inputs
===
Earlier, we have learned how to read inputs from the user. Let's combine this with our ```if``` statements. Try this program...

<div class="skulpt_box" console_only>
temperature = input("What is the temperature today?")

if temperature > 30:
    print("It is a hot day!")
else:
    print("It is a cool day.")
</div>

Well, that didn't work correctly... Can you figure out why? Try to fix the program!

Conditions using Strings
===
We can also compare strings, but you should typically only use **equal** (```==``` ) and **not equal** (```!=```) with strings.

<div class="skulpt_box" console_only>
ans = input("Do you want ice cream? (yes or no)")

if ans == "yes":
    print("Here's an ice cream for you!")
else:
    print("No ice cream for you!")
</div>
