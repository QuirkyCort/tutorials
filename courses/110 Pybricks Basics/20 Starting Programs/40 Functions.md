# Functions

A **Function** is a group of code that runs everytime we **call** the function.

Functions helps us to organize our code, and minimize repetition.
A good program should be made up of many short functions, with very little code outside of functions.

```python
def say_hello():
    print('hello')

say_hello()
say_hello()
say_hello()
```

This bunch of code creates a new function named **say_hello**, and calls (run) it 3 times.
Try it out.

When creating a function, the first line should take the form... `def some_name():`, and subsequent lines should be indented (note the `def` and the colon at the end).

`say_hello()` this calls (run) the **say_hello** function (note that there is no `def` and no colon at the end).
We have 3 lines of `say_hello()`, so the function will run 3 times.

<div class="important">
Defining a function doesn't make it run.
It only runs when you call it.
If you don't call a function, the code inside will never run.
</div>

## Function Parameters

A function can have a parameter.
This allows you to pass in some value when running it.

```python
def say_something(phrase):
    print(phrase)

say_something('hello')
say_something('how are you')
say_something('good bye')
```

`def say_something(phrase):` defines the function **say_something**, with one parameter named `phrase`.
You can then use the variable `phrase` inside the function.

`say_something('hello')` calls (run) the function **say_something**, with the value `'hello'` passed in as the first parameter.
The `'hello'` will be place inside the `phrase` variable when running the function.

## Multiple Parameters and Defaults

You can also have more than one parameter, and parameters can be supplied with default values.

```python
def dinner(place, time='seven pm'):
    print('Meet at', place, 'for dinner at', time)

dinner('McDonalds')
dinner('KFC', 'six pm')
dinner('KFC', time='six pm')
```

`def dinner(place, time='seven pm'):` defines the function **dinner** with two parameters.
The second parameter, `time`, is given a default value.

`dinner('McDonalds')` calls the function **dinner** with the first parameter (place) set as 'McDonalds'.
The second parameter is not provided, so the default will be used.

`dinner('KFC', 'six pm')` calls the function **dinner** with both the parameters set.
This will overide the default value for the second parameter.

`dinner('KFC', time='six pm')` This works the same, but with the second parameter specified by name.

## Return values

A function can also return a value.

```python
def add_up(a, b):
    result = a + b
    return result

c = add_up(1, 2)
print(c)

print(add_up(3, 4))
```

`return result` The `return` statement can only be used inside a function.
It immediately ends the function and return the provided value.
In this case, it returns the result of `a + b`.

`c = add_up(1, 2)` calls the function **add_up** and store the return value in a variable named `c`.

`print(add_up(3, 4))` calls the function **add_up** and immediately print out the return value.

## Global Variables

```python
a = 123

def say_number():
    print(a)

say_number()
```

If you run the above code, you should see `123` in the terminal output.

The `a` variable is defined outside of any functions, so it is called a **global** variable.
Global variables can be accessed anywhere within your program, including inside a function.

## Local Variables

```python
def say_number():
    b = 123
    print(b)

say_number()
print('one more time')
print(b)
```

If you run the above code, you should see a single `123` in the terminal output, the line `one more time`, followed by an error.

The `b` variable is defined inside of the **say_number** function, so it is called a **local** variable.
It is local to the **say_number** function and can only be used inside of that function.

This results in an error when the last `print(b)` try to run.

## global Keyword

```python
a = 123

def say_number():
    a = 456
    print(a)

say_number()
print(a)
```

If you run the above code, you should see `456` in the terminal output, followed by `123`.

When we run the **say_number** function, it changes the value of `a` to `456`, but when we print out the value of `a` in the last line, it reverted back to `123`?

A function can't normally change a global variable, so when the function runs `a = 456`, Python create a new local variable (...also named `a`), and set that local variable to `456`.
The global variable `a` remains unchanged.

```python hl_lines="4"
a = 123

def say_number():
    global a
    a = 456
    print(a)

say_number()
print(a)
```

Here we add the statement `global a` inside the **say_number** function.
This tells Python that we want to change the global variable `a`.

If you run this code, you should see `456` appear twice.

Note that you only need the `global` statement if you are changing a variable, and not if you only need to read its value.