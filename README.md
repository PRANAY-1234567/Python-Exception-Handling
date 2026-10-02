# Python Exception Handling

This repository contains Python examples for understanding **Exception Handling**, including `try`, `except`, `else`, and `finally` blocks. It also demonstrates **nested exception handling** and how to create and handle **user-defined exceptions**.

## 📌 Topics Covered

* `try` block
* `except` block
* `else` block
* `finally` block
* Combination of `try`, `except`, `else`, and `finally`
* Nested exception handling
* Creating user-defined exceptions
* Using `raise`
* Handling custom exceptions

---

## 1. Using the `else` Block

The `else` block executes only when the `try` block executes successfully without any error.

### Example

```python
a = {1: 2, 4: 5, 8: 9}

try:
    print(a[1])
except:
    print("Error Handling")
else:
    print("It's Working")
```

### Output

```text
2
It's Working
```

If an exception occurs inside the `try` block, the `else` block will not execute.

---

## 2. Using the `finally` Block

The `finally` block executes **regardless of whether an exception occurs or not**.

### Example

```python
a = {1: 2, 4: 5, 8: 9}

try:
    print(a[1])
except:
    print("Error Handling")
finally:
    print("All Working")
```

### Output

```text
2
All Working
```

If the `try` block contains an error, the `except` block executes and the `finally` block still executes.

---

## 3. Using `try`, `except`, `else`, and `finally`

Python allows all four blocks to be used together.

### Example

```python
a = {1: 2, 4: 5, 8: 9}

try:
    print(a[1])
except:
    print("Error Handling")
else:
    print("It's Working")
finally:
    print("All Working")
```

### Execution Flow

If there is **no error**:

```text
try → else → finally
```

If there is an **error**:

```text
try → except → finally
```

The `else` block is skipped when an exception occurs.

---

## 4. Nested Exception Handling

Exception handling can also be placed inside another `try` block.

### Example

```python
a = 10
b = 5

try:
    print(a / b)

    try:
        print(a / 2)
    except NameError:
        print("Name error Handling")
    else:
        print("second one")
    finally:
        print("finally block is working")

except:
    print("error Handling")

else:
    print("stage one done")

finally:
    print("its done")
```

### Execution Flow

The program contains an outer `try` block and an inner `try` block.

```text
Outer try
   ↓
Inner try
   ↓
Inner except / else
   ↓
Inner finally
   ↓
Outer except / else
   ↓
Outer finally
```

Nested exception handling is useful when different parts of a program require separate error-handling logic.

---

## 5. Creating a User-Defined Exception

Python allows us to create our own exception classes.

A custom exception can be created by inheriting from `BaseException` or, more commonly, from `Exception`.

### Example

```python
class MetroError(Exception):
    pass
```

We can then raise the custom exception using the `raise` keyword.

```python
def demo(x):
    if x < 0:
        print("It's Working")
    else:
        raise MetroError

demo(20)
```

Since `20` is not less than `0`, the program raises `MetroError`.

---

## 6. Handling a User-Defined Exception

A custom exception can be handled using `try` and `except`.

### Example

```python
class MetroError(Exception):
    pass

def demo(x):
    if x < 0:
        print("It's Working")
    else:
        raise MetroError

try:
    demo(20)
except MetroError:
    print("MetroError Handled")
```

### Output

```text
MetroError Handled
```

### How It Works

1. `MetroError` is created as a custom exception.
2. `demo(20)` is called.
3. Since `20 < 0` is false, `MetroError` is raised.
4. The `except MetroError` block catches the exception.
5. `"MetroError Handled"` is printed.

---

## 7. User-Defined `LengthError`

Another example is creating an exception for string length.

```python
class LengthError(Exception):
    pass

def demo(a):
    if len(a) <= 5:
        print("Below length")
    else:
        raise LengthError

demo("HIHELLO")
```

Since `"HIHELLO"` has more than 5 characters, the custom `LengthError` is raised.

It can be handled using:

```python
try:
    demo("HIHELLO")
except LengthError:
    print("Length Error Handled")
```

---

## 🔑 Important Concepts

| Keyword     | Purpose                                        |
| ----------- | ---------------------------------------------- |
| `try`       | Contains code that may cause an exception      |
| `except`    | Handles the exception                          |
| `else`      | Executes when the `try` block has no exception |
| `finally`   | Executes whether an exception occurs or not    |
| `raise`     | Manually raises an exception                   |
| `Exception` | Base class commonly used for custom exceptions |

---

## 🧠 Key Takeaways

* Use `try` for code that may generate an exception.
* Use `except` to handle exceptions.
* Use `else` when you want code to run only after successful execution.
* Use `finally` for code that must execute regardless of errors.
* Multiple levels of exception handling can be created using nested `try` blocks.
* Custom exceptions can be created using classes.
* The `raise` keyword is used to manually trigger an exception.
* For user-defined exceptions, inheriting from `Exception` is generally preferred over directly inheriting from `BaseException`.

---

## 🛠️ Technologies Used

* Python 3
* Exception Handling
* User-Defined Exceptions

## 📂 Suggested File Name

```text
exception_handling.py
```

## 👨‍💻 Author

**Pranay Jadhao**

