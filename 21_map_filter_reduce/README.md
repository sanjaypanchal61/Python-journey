# Day 21 – map(), filter(), reduce()

---

## 📖 Definitions

* **map()** → applies a function to each element
* **filter()** → selects elements based on condition
* **reduce()** → reduces all elements into a single value

---

## 🆚 Using Loop vs Functional Style

### Using Loop

```python
nums = [1, 2, 3]
result = []

for i in nums:
    result.append(i * 2)
```

### Using map()

```python
result = list(map(lambda x: x * 2, nums))
```

👉 map is shorter & cleaner

---

## Important Points

* map → transform
* filter → condition
* reduce → combine
* All return iterators (convert using list)
* reduce needs `functools` import