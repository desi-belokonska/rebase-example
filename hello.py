#!/usr/bin/env python3
from datetime import datetime

def say_time():
    print('it is', datetime.now())

def greeting():
    print('hello world')

if __name__ == '__main__':
    greeting()
    say_time()
