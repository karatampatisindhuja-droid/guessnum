This program is a **Number Guessing Game** written in Python. The computer randomly selects a number between **1 and 200**, and the player tries to guess it. The game provides hints until the correct number is guessed.

---

# Objective of the Program

* Generate a random number.
* Ask the user to guess the number.
* Give feedback:

  * "Too low" if the guess is smaller.
  * "Too high" if the guess is larger.
* Continue until the correct number is guessed.

---

# Code Explanation

## 1. Importing the Random Module

```python
import random
```

* The `random` module provides functions for generating random values.
* Here it is used to generate a random number.

---

## 2. Generating a Secret Number

```python
secret_number = random.randint(1, 200)
```

### `randint()`

Syntax:

```python
random.randint(start, end)
```

* Generates a random integer between `start` and `end`.
* Both limits are included.

Example:

```python
random.randint(1, 200)
```

Possible outputs:

```text
15
87
150
200
```

The generated number is stored in:

```python
secret_number
```

This is the number the user must guess.

---

## 3. Displaying Welcome Messages

```python
print("🎯 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 200.")
```

These statements display instructions to the player.

Output:

```text
🎯 Welcome to the Number Guessing Game!
I have chosen a number between 1 and 200.
```

---

## 4. Infinite Loop

```python
while True:
```

* Creates an infinite loop.
* The game continues asking for guesses until the correct number is entered.
* The loop stops only when `break` is executed.

---

## 5. Taking User Input

```python
guess = int(input("Enter your guess: "))
```

### `input()`

* Accepts input from the user.
* Input is received as a string.

Example:

```text
Enter your guess: 50
```

### `int()`

* Converts the input string into an integer.

Example:

```python
int("50")
```

becomes:

```python
50
```

The value is stored in:

```python
guess
```

---

## 6. Checking if the Guess is Too Low

```python
if guess < secret_number:
    print("Too low! Try again.")
```

* Compares the user's guess with the secret number.
* If the guess is smaller:

Output:

```text
Too low! Try again.
```

Example:

```python
secret_number = 120
guess = 80
```

Since:

```python
80 < 120
```

the program prints:

```text
Too low! Try again.
```

---

## 7. Checking if the Guess is Too High

```python
elif guess > secret_number:
    print("Too high! Try again.")
```

* Runs when the guess is greater than the secret number.

Example:

```python
secret_number = 120
guess = 150
```

Since:

```python
150 > 120
```

Output:

```text
Too high! Try again.
```

---

## 8. Correct Guess

```python
else:
    print("🎉 Congratulations! You guessed the correct number!")
    break
```

The `else` block executes when:

```python
guess == secret_number
```

Example:

```python
secret_number = 120
guess = 120
```

Output:

```text
🎉 Congratulations! You guessed the correct number!
```

### `break`

```python
break
```

* Terminates the `while` loop.
* Ends the game.

---

# Program Flow

### Step 1

Computer generates a random number.

Example:

```python
secret_number = 137
```

---

### Step 2

Player enters a guess.

```text
Enter your guess: 100
```

---

### Step 3

Program compares the guess.

Since:

```python
100 < 137
```

Output:

```text
Too low! Try again.
```

---

### Step 4

Player guesses again.

```text
Enter your guess: 160
```

Since:

```python
160 > 137
```

Output:

```text
Too high! Try again.
```

---

### Step 5

Player enters:

```text
Enter your guess: 137
```

Output:

```text
🎉 Congratulations! You guessed the correct number!
```

The game ends.

---

# Example Execution

```text
🎯 Welcome to the Number Guessing Game!
I have chosen a number between 1 and 200.

Enter your guess: 50
Too low! Try again.

Enter your guess: 150
Too high! Try again.

Enter your guess: 100
Too low! Try again.

Enter your guess: 120
🎉 Congratulations! You guessed the correct number!
```

---

# Concepts Used in This Program

1. **Modules**

   * `import random`

2. **Random Number Generation**

   * `random.randint()`

3. **Variables**

   * `secret_number`
   * `guess`

4. **Input and Output**

   * `input()`
   * `print()`

5. **Loops**

   * `while True`

6. **Conditional Statements**

   * `if`
   * `elif`
   * `else`

7. **Comparison Operators**

   * `<`
   * `>`
   * `==`

8. **Loop Control Statement**

   * `break`

---

# Time Complexity

* Each guess requires one comparison operation.
* If the user takes **n guesses**, the loop runs **n times**.

**Time Complexity:** `O(n)`
**Space Complexity:** `O(1)` (constant memory usage)

This is a simple interactive game that demonstrates **random number generation, loops, conditions, and user input handling** in Python.
