# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:20:06 2019

@author: mluci
"""
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'