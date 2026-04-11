# Day 29 - Operator Overloading & Method Overriding

---

## 📌 Topics Covered

* Operator Overloading
* Method Overriding

---

## Operator Overloading

### Definition:

Operator overloading allows us to change the behavior of operators for user-defined objects.

---

### Example:

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

---

### Explanation:

* `a + b` internally calls `a.__add__(b)`
* Custom logic can be applied

---

## Method Overriding

### Definition:

When a child class provides a specific implementation of a method that is already defined in its parent class.

---

## Key Differences

| Operator Overloading      | Method Overriding       |
| ------------------------- | ----------------------- |
| Uses dunder methods       | Uses inheritance        |
| Changes operator behavior | Changes method behavior |

---

## Conclusion

* Operator overloading improves flexibility
* Method overriding supports polymorphism