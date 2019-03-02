[![](https://img.shields.io/pypi/pyversions/xdg-cache.svg?longCache=True)](https://pypi.org/project/xdg-cache/)
[![](https://img.shields.io/pypi/v/xdg-cache.svg?maxAge=3600)](https://pypi.org/project/xdg-cache/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/xdg-cache.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/xdg-cache.py/)

#### Install
```bash
$ [sudo] pip install xdg-cache
```

#### Functions
function|`__doc__`
-|-
`xdg_cache.exists(key)`|return True if cache exists, else False
`xdg_cache.read(key)`|return a file content string, return None if cache not exist
`xdg_cache.rm(key)`|remove cache file
`xdg_cache.write(key, string)`|write string to cache

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>