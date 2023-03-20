# A Simple package

[Read](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)

## Install and test:

- Activate a virtual environment.
- Navigate to this folder.
- Install editable: `pip install -e .`
- Test with python interpreter

```Python
>>> import mypackage1.sub1.extra as extra
>>> extra.calc_1(1,2)
4
```