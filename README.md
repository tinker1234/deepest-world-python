# deepest-world-python
This is the base to run python in deepest world
*** This must be run in steam client ***
# in the code section of the game

put this:
```js
await dw.loadScript("https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js");
await dw.loadScript("dw://index.js");
await main("main.py")
```

# config
```
packages: list of packages for pyodide to install
"packages": ["arrr"]
files: list of local files so you can import
"files": ["dw://test.py"]
```
