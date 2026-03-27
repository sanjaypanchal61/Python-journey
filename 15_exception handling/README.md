# Day 15 – Exception Handling

---

## 📖 Definition

An **exception** is an error that occurs during the execution of a program.

**Exception handling** is the process of handling runtime errors to prevent program crash.

---

## 🎯 Types of Exceptions (Common)

* `ZeroDivisionError` → divide by zero
* `ValueError` → invalid input
* `TypeError` → wrong data type
* `IndexError` → list index out of range
* `KeyError` → dictionary key not found

---

## ⭐ Important Points

* Improves user experience
* Use specific exceptions instead of general `except`
* Avoid hiding errors silently

---

## ⚠️ Common Mistakes

* ❌ Using only `except` (bad practice)
* ❌ Ignoring errors without message
* ❌ Not using specific exception types