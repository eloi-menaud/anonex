# structure
```
.
├── anonex.py        - interface (main)
├── custom_syntax.py - fonctions defining custom outex suntax
├── dictionnary.py   - store variables containg list of name,city...
└── tools.py         - where you could put generique fonction or tools
```


# add custom syntax
1 create your own fonction taking full text with ~xx and return the new version overwrited
2 add a call to your function in `custom_syntax()`
```python
def custom_syntax(text):
    text = new_syntax(text)
    ...

...

def new_syntax(text):
    ...
    return(new_text)
```