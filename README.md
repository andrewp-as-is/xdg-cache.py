<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/xdg-cache.svg?maxAge=3600)](https://pypi.org/project/xdg-cache/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/xdg-cache.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/xdg-cache.py/actions)

### Installation
```bash
$ [sudo] pip install xdg-cache
```

#### Examples
```python
>>> import xdg_cache
>>> xdg_cache.write("key",'value')
>>> xdg_cache.read("key")
'value'
>>> xdg_cache.path("key")
'~/.cache/key'
>>> xdg_cache.exists("key")
True
>>> xdg_cache.rm("key")
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
