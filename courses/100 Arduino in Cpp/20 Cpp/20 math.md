# Math and Type Conversion

Try the following...

```cpp hl_lines="1 2 11 12 13"
int a = 100;
int b = 1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(a + b);
  b = b + 1;
  delay(1000);
}
```

We can perform some simple math operations on variables using...

* **+** : Plus
* **-** : Minus
* **\*** : Multiply
* **/** : Divide

## Type Conversion

You cannot add a **String** and a number (eg. int, float); adding a word and a number simply doesn't make sense.
But you can add a String and a String together like this...

```cpp
String a = "Hello ";
String b = "World";
Serial.println(a + b);
```

This will cause the Arduino to print "Hello World" on the serial monitor.

### Number to String

To convert a number (eg. int, float) into a String, you can do...

```cpp
String a = "The result is:";
int b = 42;
a = a + String(b);
Serial.println(a);
```

### String to Number

If you need to convert a String into a number, you can do so like this...

```cpp
String a = "100";
Serial.println(a.toInt() + 1);
```

This will convert the String variable **a** into an integer.
You can also use **.toFloat()** to convert it into a float.

## Exercise 1

This program will not work...

```cpp hl_lines="10"
String a = "The result is: ";
int b = 100;
int c = 1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(a + b + c); // Fix this line
  c = c + 1;
  delay(1000);
}
```

...fix it (...change only the highlighted line) so that it displays...

```
The result is: 101
The result is: 102
The result is: 103
.
.
.
```

## Exercise 2

This is the same as the previous program, but the variable **b** is now a String.

```cpp hl_lines="10"
String a = "The result is: ";
String b = "100";
int c = 1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(a + b + c); // Fix this line
  c = c + 1;
  delay(1000);
}
```

...fix it (...change only the highlighted line) so that it displays the same output as before...

```
The result is: 101
The result is: 102
The result is: 103
.
.
.
```