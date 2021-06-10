# Binotel package for Python language

This package provides Python implementation of some Binotel api.

## Installation

Use the `pip` command:

	$ pip install binotel

## Requirements

Binotel package tested against Python 3.8.1

## Example

```python
from binotel import Binotel

# Creating binotel object
b = Binotel('your_key', 'your secret')

# Get all incoming calls since date
calls = b.all_incoming_calls_since(1370034000)
print(calls)

```
