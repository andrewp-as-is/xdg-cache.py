#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import shutil

XDG_CACHE_HOME = os.getenv("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))

def path(key):
    """return fullpath - `$XDG_CACHE_HOME/<key>`"""
    return os.path.join(XDG_CACHE_HOME,key)


@public.add
def exists(key):
    """return True if cache exists, else False"""
    fullpath = path(key)
    return os.path.exists(fullpath)


@public.add
def write(key,string):
    """write string to cache"""
    fullpath = path(key)
    dirname = os.path.dirname(fullpath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    open(fullpath,"w").write(string)


@public.add
def read(key):
    """return a file content string, return None if cache not exist"""
    fullpath = path(key)
    if os.path.exists(fullpath):
        return open(fullpath).read()


@public.add
def rm(key):
    """remove cache file"""
    fullpath = path(key)
    if os.path.exists(fullpath):
        if os.path.isfile(fullpath) or os.path.islink(fullpath):
            os.unlink(fullpath)
        if os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
