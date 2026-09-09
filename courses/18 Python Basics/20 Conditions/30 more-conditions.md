Else If
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

So far, we have used ```if``` and ```else```, but what if we want to compare many different conditions? Try running this program in the empty trinket below.

```
chillies = input("How many chillies do you want?")
chillies = int(chillies)

if chillies > 8:
    print("Crazy spicy!!!")
elif chillies > 6:
    print("Ultra spicy")
elif chillies > 4:
    print("Very spicy")
elif chillies > 2:
    print("Moderately spicy")
elif chillies > 0:
    print("Slightly spicy")
else:
    print("Not Spicy at all")
```

<div class="skulpt_box" console_only>
</div>

The ```elif``` command means **else if**. It lets us compare multiple conditions, and run the code for the first condition that is true.

Combining Conditions
===
Sometimes, we want to combine multiple conditions together. To do so, we can use ```and``` and ```or```. Try this example program that uses ```and```.

```
students = 25
drinks = input("How many milos do we have?")
drinks = int(drinks)
food = input("How many burgers do we have?")
food = int(food)

if drinks >= students and food >= students:
    print("We have enough food and drinks")
elif drinks >= students:
    print("We have enough drinks")
elif food >= students:
    print("We have enough food")
else:
    print("We don't have enough food or drinks!")
```

<div class="skulpt_box" console_only>
</div>

The ```and``` condition is true, only if both conditions are true. The ```or``` condition is true, if either of the conditions are true.

<div class="skulpt_box" console_only>
a = 1
b = 2

if a == 1 and b == 2:
    print("The first AND is true")

if a == 1 and b == 1:
    print("This is false")
    
if a == 1 or b == 1:
    print("The first OR is true")
    
if a == 2 or b == 2:
    print("The second OR is also true")
</div>
