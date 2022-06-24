# Functions

Functions are like recipes, they store your instructions and allow us to reuse them again and again.
Here's an example of how functions are created and used in C++...

```cpp hl_lines="1 2 3 4 11"
float add_and_half(int a, int b) {
  float c = (a + b) / 2.0;
  return c;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  float result = add_and_half(2, 3);
  Serial.println(result);
  delay(1000);
}
```

**int add_and_double(int a, int b)** : This defines **add_and_double** as a function that returns a **float** value.
It takes two parameters; **a** and **b**, both of which are **int** types.
The code inside the curly brackets are the content of this function; they will run whenever we call the function.

**float result = add_and_half(2, 3)** : In this line, we call the function **add_and_half**.
We supply it with **2** for the first parameter and **3** for the second.
The value that the **add_and_half** function returns will be stored in the **result** variable.

**float c = (a + b) / 2.0** : Here we add **a** and **b** together, then divide it by **2.0**.
Note that we are using **2.0** and not **2**. If we had used **2**, the Arduino will perform an integer calculation (...you can try it and see what happens).

**return c** : This ends the **add_and_half** function, and causes it to return the value of the variable **c**.

## Return Types and void

You can create functions that returns any types of values (eg. int, float, String).
If your function does not need to return any value, you should define it as type **void** like this...

```cpp hl_lines="1 2 3 4 11"
void prints_a_and_b(int a, int b) {
  Serial.println(a);
  Serial.println(b);
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  prints_a_and_b(2, 3);
  delay(1000);
}
```

## No Parameters

If your function does not require any parameters, you should use an empty **()** like this...

```cpp hl_lines="1 2 3 10"
void prints_nothing() {
  Serial.println("nothing");
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  prints_nothing();
  delay(1000);
}
```

## Exercise 1

Write a function that takes a single **int** as parameter, and returns the cube (power of 3) of that number.

## Exercise 2

Make an alternate version of the previous function (...use a different name), and modify it so that instead of returning the cube of the provided number, it will simply print it out.

<div class="tip">
Functions are not strictly necessary in a program, but they help reduce code repetition and improve the neatness of your code; this becomes important as your code gets longer and more complicated.
</div>