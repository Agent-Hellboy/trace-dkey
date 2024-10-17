# Usage Guide

trace-dkey can be used both as a Python library and as a command-line tool.

## As a Python Library

You can use trace-dkey in your Python code as follows:

```python
from trace_dkey import trace

data = {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}
path = trace(data, 'f')
print(path)   # Output: [['a', 'b', 'c', 'd', 'e', 'f']]
```


## As a Command-Line Tool

You can use trace-dkey as a command-line tool:

```bash
python -m trace_dkey --file=test.json --key=name
```

