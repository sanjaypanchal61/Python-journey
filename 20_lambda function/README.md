# Day 20 – Lambda Function

---

## 📖 Definition

A **lambda function** is a small anonymous function defined using the `lambda` keyword.

---

## Lambda vs Normal Function

```python
# Normal Function
def square(x):
    return x * x

# Lambda Function
square = lambda x: x * x
```

---

## Difference between def and lambda

| Feature    | def           | lambda       |
| ---------- | ------------- | ------------ |
| Name       | Yes           | No           |
| Statements | Multiple      | Single       |
| Use        | Complex logic | Simple logic |

---

## ⚠️ Limitations of Lambda

* Only one expression allowed
* Cannot contain multiple statements
* Not suitable for complex logic

---

## ⚠️ Common Mistakes

* ❌ Using lambda for complex logic
* ❌ Writing unreadable one-liners
* ❌ Overusing lambda instead of normal functions

---

## 💡 Best Practices

* Use lambda only for **small/simple tasks**
* Prefer normal function for complex logic