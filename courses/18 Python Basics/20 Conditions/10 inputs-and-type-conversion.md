Inputs
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

In our earlier lessons, we have learned about outputs using ```print()```. In this lesson, we are going to learn to use ```input()``` to read an input.

Try running this program in the trinket  below...

```
age = input("What is your age?")
print("Your age is " + age)
```

<div class="skulpt_box" console_only>
</div>

Let's look at how ```input``` works...

```
age = input("What is your age?")
```

This line will first display **"What is your age?"** in the terminal on the right, then wait for the user to type in an answer. Press enter after typing in your age, and input will assign the answer to the variable ```age```.

```
print("Your age is " + age)
```

The second line adds the string ```"Your age is "``` to the variable ```age```, then prints the result.

***IMPORTANT :*** *The ```input``` function will always return a string, even if you type in a number.*

---

Type Conversion
===
We have seen that ```"123"``` is a string, while ```123``` is a number, but how can we convert it from one type to another?

<div class="skulpt_box" console_only>
a = "3"
b = 4
print(int(a) + b)
</div>

In the above program, we set ```a``` to a string ```"3"```, and ```b``` to a number ```4```. Normally, we won't be able to add them together, because they are different types. But we can use ```int()``` to convert a string into an integer number. This will then allow us to add ```a``` and ```b``` together!

To convert a type into another, we can use...

```
str(1)       # This converts the number 1 into a string
int("2")     # This converts the string "2" into an integer
float("3.1") # This converts the string "3.1" into a float
```

All of these works with variables as well!

```
a = 1
str(a)     # This converts the number 1 into a string

b = "2"
int(b)     # This converts the string "2" into an integer

c = "3.1"
float(c)   # This converts the string "3.1" into a float
```

The program below contains an error, because we are trying to add a number to a string. Can you fix it?

<div class="skulpt_box" console_only>
my_age = 12
print("My age is " + my_age)
</div>

Here's a slightly more difficult problem...

<div class="skulpt_box" console_only>
boys = 20
girls = "19"
total_students = boys + girls
print("There are " + total_students + " students in my class")
</div>

---

Exercises (Inputs and Type Conversion)
===
### Ex 1. Apple prices

Remember than ```input()``` always return a string, even if you type in a number? That can be a problem if you need to do some calculation with the input.

Here's a program that calculate the total price you have to pay. Each apple is priced at $2. The program will ask the user how many apples they want to buy, then calculate the price the user have to pay. Can you correct the error in the program?

<div class="skulpt_box" console_only>
apples = input("How many apples do you want to buy?")
total_price = apples * 2
print("You will need to pay $ " + total_price)
</div>

### Ex 2. Maximum Heart Rate

When exercising, we can measure our heart rate to determine if we are exercising too hard or too little. To do so, we will first need to calculate our maximum heart rate using the following formula.

```
Max_Heart_Rate = 220 - age
```

If our heart rate is within 50% to 70% of our maximum, then we are exercising at moderate intensity. If it's within 70% to 85% of our maximum, then we are exercising at high intensity. You can read more about heart rates and exercise here: https://www.healthhub.sg/live-healthy/1231/keep-track-of-your-exercise-intensity.

Using the empty trinket below, write a program that will ask the user for their age, calculate their maximum heart rate, then output it to the terminal.

<div class="skulpt_box" console_only>
</div>
