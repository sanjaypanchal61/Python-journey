# Day 19 – Local & Global Variables

---

## 📖 Definition

Scope defines where a variable can be accessed in a program.

---

## 🔹 Local Variable

* A variable declared inside a function is called a local variable.
* Accessible only inside the function

---

## 🔹 Global Variable

* A variable declared outside a function is called a global variable.
* Accessible throughout the program

---

## 🔹 Global Keyword

* Modifies global variable inside function

---

## 🔍 Example of Scope

```python
x = 100

def outer():
    x = 50

    def inner():
        x = 10
        print(x)

    inner()

outer()
```

👉 Output: 10 (Local scope priority)

---

## ⚠️ Common Mistakes

* ❌ Trying to access local variable outside function
* ❌ Modifying global variable without `global` keyword

---

## ⭐ Important Points

* Local variables exist only inside function
* Global variables exist throughout program
* Local has higher priority than global