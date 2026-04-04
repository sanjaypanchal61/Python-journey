# Day 23 – is vs ==

---

## 📖 Definition

* `is` → compares **object identity (memory location)**
* `==` → compares **values (equality)**

---

## 💻 Basic Example

```python id="eq1"
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # true (same values)
print(a is b)  # false (different objects)
```

---

## ⭐ Important Points

* `==` → checks equality (values)
* `is` → checks identity (memory)
* Immutable objects may behave differently
* Never use `is` for list/string comparison