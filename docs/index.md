# trace-dkey

trace-dkey is a simple tool for tracing keys in nested dictionaries.

## Installation

You can install Trace DKey using pip:


```bash
pip install trace-dkey
```

## Usage

### As a Command-Line Tool
You can use trace-dkey as a command-line tool:

```bash
python -m trace_dkey --file=test.json --key=name
```

### As a Python Library

You can use trace-dkey in your Python code as follows:

```python
from trace_dkey import trace

data = {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}
path = trace(data, 'f')
print(path)   # Output: [['a', 'b', 'c', 'd', 'e', 'f']]
``` 







