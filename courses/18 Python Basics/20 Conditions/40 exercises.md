Exercises
===
<script src="../../skulpt/skulpt.min.js" type="text/javascript"></script> 
<script src="../../skulpt/skulpt-stdlib.js" type="text/javascript"></script> 
<script src="../../ace-1.11.2/ace.js"></script>
<script src="../../ace-1.11.2/ext-language_tools.js"></script>
<script src="../../skulpt_box/skulpt_box.js" type="text/javascript"></script>
<link rel="stylesheet" href="../../css/skulpt_box.css"></link>

###Ex 1. Enough money?
This program asks the user how much money they have and how many apples they want to buy (...each apple costs $2). It will then tell the user if they have enough money.

The program doesn't work correctly. Can you figure out the problem and fix it?

<div class="skulpt_box" console_only>
money = input("How much money do you have?")
apples = input("How many apples do you want to buy?")
cost = apples * 2

if cost > money:
    print("You don't have enough money")
else:
    print("You have enough money")
</div>

###Ex 2. Apples and Oranges 
You have $20. Each apple costs $2 and each orange costs $3.

Write a program that will ask the user if they prefer apples or oranges. If they prefer apples, it should ask them how many apples they want to buy. If they prefer oranges, it should ask them how many oranges they want to buy. It should then tell them if they have enough money.

<div class="skulpt_box" console_only>
</div>

###Ex 3. Rainy Day
Write a program that asks the user the temperature and whether it is raining or not. 

* If the temperature is above 30 and it is raining, the program should print "It is a hot and rainy day".
* If the temperature is above 30 and it is not raining, the program should print "It is a hot and dry day".
* If the temperature is not above 30 and it is raining, the program should print "It is a cold and rainy day".
* If the temperature is not above 30 and it is not raining, the program should print "It is a cold and dry day".

<div class="skulpt_box" console_only>
</div>
