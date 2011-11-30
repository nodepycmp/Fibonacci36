#!/usr/bin/env python
import sys

def fib(i, current, next):
  if i == 0:
    return current
  else:
    return fib(i - 1, next, current + next)

print fib(int(sys.argv[1]),0,1)
