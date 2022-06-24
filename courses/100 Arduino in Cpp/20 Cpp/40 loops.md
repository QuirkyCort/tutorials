# Loops

Loops allows us to repeat a section of code multiple times.
There are two main types of loops; the **for** loop and the **while** loop.

## for Loops

This is an example of the **for** loop...

```cpp hl_lines="6 7 8"
void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int a=0; a<10; a++) {
    Serial.println(a);
  }
  delay(1000);
}
```

Each **for** loop contains 3 expressions...

**int a=0** : This defines a variable **a** and set it to the value **0** at the start of the **for** loop.

**a&lt;10** : This checks if the variable **a** is less than **10**.
If it is true, the code in the curly brackets will run.
If it is false, the **for** loop will end.

**a++** : This increments the variable **a** by one each time after running the code in the curly brackets.

## while Loops

This is an example of the **while** loop...

```cpp hl_lines="7 8 9 10 11"
void setup() {
  Serial.begin(9600);
}

void loop() {
  int a = 1;
  while (a < 5) {
    Serial.println(a);
    delay(200);
    a++;
  }

  delay(2000);
}
```

**while (a &lt; 5)** : This **while** loop will keep repeating the code inside the curly brackets as long as **a** is less than **5**.

## break and continue

There are two special commands that can only be used inside a **for** or **while** loop; **break** and **continue**

### break

The **break** commands orders the loop to end immediately.
Here's an example...

```cpp hl_lines="8 9 10"
void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int a=0; a<10; a++) {
    Serial.println(a);
    if (a == 5) {
      break;
    }
  }
  delay(1000);
}
```

In the above code, the **for** loops ends as soon as **a** is equal to **5**.

### continue

The **continue** commands orders the loop to immediately continue with the next iteration, skipping the code below it.
Here's an example...

```cpp hl_lines="7 8 9"
void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int a=0; a<10; a++) {
    if (a == 5) {
      continue;
    }
    Serial.println(a);
  }
  delay(1000);
}
```

In the above code, the **for** loops skips the **Serial.println** if **a** is equal to **5**.

## Exercise

The factorial of a number is the multiplication of all positive integers less than or equal to that number.
For example, the factorial of 3 is 6 (1 x 2 x 3) and the factorial of 5 is 120 (1 x 2 x 3 x 4 x 5).

Using a **for** loop, modify the program below to print out the factorial of **7**.

```cpp hl_lines="8"
void setup() {
  Serial.begin(9600);
}

void loop() {
  int result = 0;

  // Put your for loop here

  Serial.println(result);

  delay(1000);
}
```
