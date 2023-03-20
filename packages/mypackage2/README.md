# A Simple package

[Read](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)

## Extra in this package compared to mypackage1.

- Includes dependency on chuck norris.
- Added entry_points to setup.cfg

## Install and test:

- Activate a virtual environment.
- Navigate to this folder.
- Install editable: `pip install -e .`
- Test with python interpreter

```Python
>>> import mypackage2.cmd as cmd
>>> cmd.chuck())
Many people wonder why Star Wars begins with "A long time ago, in a galaxy far, far away"... 
```

## Testing entry-point

```bash
(venv) C:\Users\p_olo\Documents\python>pol-app1
App1 main
*** Chuck Norris Facts ***
Chuck Norris can make you disappear with just a blink of an eye, literally.
***
None
```
