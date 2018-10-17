#!/usr/bin/env python3

import time
from caproto.sync.client import read, write


def sleep(seconds):
    print("sleeping for %s seconds" % seconds)
    time.sleep(seconds)


print("Value of a: %s" % read('simple:A').data[0])
print("Value of b: %s" % read('simple:B').data[0])

sleep(1)

print("Setting value of b to: %s" % 5)
write('simple:B', 5, notify=True)

sleep(1)

print("Value of b now: %s" % read('simple:B').data[0])
