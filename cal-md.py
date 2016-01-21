#!/usr/bin/env python

__author__ = "Md. Minhazul Haque"
__copyright__ = "Copyright (C) 2016 Md. Minhazul Haque"
__license__ = "Public Domain"
__version__ = "1.0"

import calendar
import datetime
import sys

m = datetime.date.today().month
y = datetime.date.today().year

if len(sys.argv) == 3:
    m = int(sys.argv[2])
    y = int(sys.argv[1])

print "###", calendar.month_name[m], " ", y

w, m = calendar.monthrange(y, m)
weekdays = 'Mo Tu We Th Fr Sa Su'.split(' ')

print "|",
for wd in (weekdays[w:] + weekdays[:w]):
    print "%3s|" % wd,

print
print "|",

for i in range(7):
    print "---|",
    
print

for day in range(1, m+1):
    if day % 7 == 1:
        print "|",
    
    print "%3d|" % day,
    
    if day % 7 == 0:
        print
