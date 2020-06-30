#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xdg_cache

KEY = "folder/name"
string = "string value"

xdg_cache.write(KEY,string)
assert xdg_cache.read(KEY) == string
xdg_cache.rm(KEY)
assert xdg_cache.exists(KEY) == False
