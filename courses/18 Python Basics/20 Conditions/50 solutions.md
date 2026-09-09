Solutions
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

### Ex 1. Enough money?

<div class="skulpt_box" console_only>
money = input("How much money do you have?")
money = int(money)
apples = input("How many apples do you want to buy?")
apples = int(apples)
cost = apples * 2

if cost > money:
    print("You don't have enough money")
else:
    print("You have enough money")
</div>

### Ex 2. Apples and Oranges

<div class="skulpt_box" console_only>
money = 20
choice = input("Do you prefer apples or oranges?")

if choice == "apples":
    price = 2
    fruits = input("How many apples do you want to buy?")
else:
    price = 3
    fruits = input("How many oranges do you want to buy?")

cost = price * int(fruits)

if cost  > money:
    print("You don't have enough money")
else:
    print("You have enough money")
</div>

### Ex 3. Rainy Day

<div class="skulpt_box" console_only>
temperature = input("What is the temperature?")
temperature = int(temperature)
raining = input("Is it raining? (yes / no)")

if temperature > 30 and raining == 'yes':
    print("It is a hot and rainy day")
elif temperature > 30 and raining == 'no':
    print("It is a hot and dry day")
elif temperature <= 30 and raining == 'yes':
    print("It is a cold and rainy day")
elif temperature <= 30 and raining == 'no':
    print("It is a cold and dry day")
else:
    print("Invalid answers")
</div>
