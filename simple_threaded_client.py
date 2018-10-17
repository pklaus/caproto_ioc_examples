#!/usr/bin/env python3

import time
from caproto.threading.client import Context


def sleep(seconds):
    print("sleeping for %s seconds" % seconds)
    time.sleep(seconds)


ctx = Context()

a, b = ctx.get_pvs('simple:A', 'simple:B')

print("Value of a: %s" % a.read().data[0])
print("Value of b: %s" % b.read().data[0])

sleep(1)

print("Setting value of b to: %s" % 5)
b.write([5], wait=True)

sleep(1)

print("Value of b now: %s" % b.read().data[0])
