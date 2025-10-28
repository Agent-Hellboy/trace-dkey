# Hashable Built-in Data Types

**Hashable objects** have a hash value that never changes during their lifetime
and can be used as dictionary keys or set elements.  
Objects are hashable by default if they are immutable and implement both
`__hash__()` and `__eq__()` consistently.

---

## Hashable Built-in Types

The following standard built-in types are hashable:

- `int`
- `float`
- `complex`
- `bool`
- `str`
- `bytes`
- `tuple` *(only if all its elements are hashable)*
- `frozenset`
- `range`
- `NoneType` (`None`)
- `memoryview` *(if readonly)*
- user-defined classes that implement `__hash__` consistently with `__eq__`

Most hashable types are immutable.  

Mutable built-in types such as `list`, `set`, and `dict` are **not** hashable
because their contents (and thus their hash values) can change.

---

## Notes and Exceptions

- Immutable objects have stable hash values → can be used as dictionary keys.
- Mutable objects can’t be hashed because their state (and equality) can change.
- A `tuple` is hashable **only if all its elements** are hashable.
- `memoryview` is hashable only if it’s **readonly**.
- User-defined classes are hashable by default **unless** `__eq__` is overridden
  without redefining `__hash__`.

---

## Quick Check in Python

You can test hashability easily with this helper function:

```python
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

examples = [int, float, complex, bool, str, bytes,
            tuple, list, dict, set, frozenset, range,
            memoryview, type(None)]

for t in examples:
    # Safely create an instance
    if t is memoryview:
        instance = t(b"example")  # readonly by default
    elif t is type(None):
        instance = None
    else:
        instance = t()

    print(f"{t.__name__:>10}: {is_hashable(instance)}")
