# Weekly Skill Log

## Week 1

### Concepts covered
- Big O: O(1), O(n), O(log n), O(n²), O(2ⁿ) — concrete examples for each
- Iterative vs. recursive Fibonacci as a direct O(n) vs O(2ⁿ) comparison
- Array reversal in place: two-pointer swap, O(n) time, O(1) space
- Cyclic right rotation by k using `(i - k) % N`
- String immutability and why `s += char` in a loop is O(n²)
- Two-pass frequency map for first non-repeating character
- Palindrome check via index comparison
- OOP: `__init__`, `self`, instance state, methods that mutate it
- `for/else`: the `else` only runs if the loop completes without `break` — used for "search, and handle not-found" logic

### Built
- **`todo.py`** — CLI to-do list: add, view, edit, remove, JSON persistence (load on start, save on exit), plain-text export
- **`museum.py`** — `Exhibition` class (`room_no`, `theme_name`, `is_open`), open/close with duplicate-entry guard, sorted insert by room number
- **Algorithm scratch scripts** — fibonacci (iterative + recursive), `no_repeat`, `is_palindrome`, `reverse_array`, `shift`

### Code

```python
# fibonacci_iterative.py
a, b = 0, 1
n = 100
for i in range(n + 1):
    print(f"fibonacci({i}) = {a}")
    a, b = b, a + b
```

```python
# fibonacci_recursive.py — O(2^n), deliberately shown to be slow
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 35
for i in range(n + 1):
    print(f"fibonacci({i}) = {fibonacci(i)}")
```

```python
# no_repeat.py
def no_repeat(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
```

```python
# is_palindrome.py
word = input("Enter a word you would like to check if it is a palindrome: ")

def is_palindrome(word):
    N = len(word)
    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            return False
    return True

print(is_palindrome(word))
```

```python
# reverse_array.py
def reverse_array(A):
    N = len(A)
    for i in range(N // 2):
        A[i], A[N - i - 1] = A[N - i - 1], A[i]
    return A
```

```python
# shift.py — cyclic rotation
def shift(A, k):
    N = len(A)
    results = []
    for i in range(N):
        target = (i - k) % N
        results.append(A[target])
    return results
```

`todo.py` and `museum.py` kept as-is in the project folder — not reproduced here, they're long. See files.

### Bugs found on review
- **`shift(A)` originally took only `A`, reading `k` from an outer/global variable.** Fixed above to take `k` as a real parameter — the old version would silently use the wrong rotation amount the moment `k` isn't defined exactly where you expect.
- **`museum.py`'s `main()` was defined inside the `if __name__ == "__main__":` block**, not at module level — works standalone, not importable or testable elsewhere. Needs restructuring before tests get added.
- Minor: `== True` / `== False` comparisons and pointless `int(1)`, `int(2)` casts in print statements throughout — not bugs, just noise worth dropping.

### Breakthroughs
- Understood *why* `s += char` is O(n²), not just that it is
- Caught the `for/else` pattern for search-with-fallback
- Custom objects need explicit dict conversion to serialize to JSON — arrays don't have this problem, objects do

### Weak spots
- No automated tests — verifying everything by hand in the terminal
- The `shift` bug above was real. A second one I initially flagged (`is_palindrome`) turned out to be a stale draft from before switching off the online compiler onto local VS Code with Copilot disabled — the real file already had the correct `N // 2` version. Lesson: when pulling code into a log, confirm it's the current file on disk, not an old tab or paste.

### Week 2 goals
- Refactor `todo.py` tasks from raw strings into a `Task` class (`description`, `task_id`, `is_completed`)
- Add `to_dict()` / `from_dict()` to `Exhibition` for clean JSON save/load
- Move `museum.py`'s `main()` to module level so it's testable
- Implement `__str__` / `__repr__` on both classes