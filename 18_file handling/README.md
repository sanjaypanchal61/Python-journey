# Day 18 – File Handling

---

## 📖 Definition

File handling is used to perform operations like reading, writing, appending, and managing files in Python.

---

## File Modes

| Mode  | Description            |
| ----- | ---------------------- |
| `"r"` | Read file (default)    |
| `"w"` | Write (overwrite file) |
| `"a"` | Append (add data)      |
| `"x"` | Create new file        |
| `"b"` | Binary mode            |
| `"t"` | Text mode (default)    |

---

## Methods

* file.readline()     # read one line
* file.readlines()    # read all lines as list

---

## Difference between "w" and "a"

* `"w"` → overwrite file
* `"a"` → append data

---

## ⭐ Important Points

* Always use `with` statement
* `"w"` mode deletes old data
* `"a"` adds data without deleting

---

## ⚠️ Common Mistakes

* ❌ Forgetting to close file
* ❌ Using `"w"` accidentally (data loss)

---

## 💡 Real-World Use Cases

* Log files handling
* Notes saving app
* Data storage
* Report generation
* CSV / JSON data processing