#!/usr/bin/env python3
import time
from caproto.threading.client import Context


ctx = Context()

x, dt = ctx.get_pvs('random_walk:x', 'random_walk:dt')

res = x.read()
print("Value of x when startup up: %s" % res.data[0])

sub = x.subscribe()

def f(response):
    print("New x received: %s" % response.data[0])

token = sub.add_callback(f)

def sleep(seconds):
    print("sleeping for %s seconds" % seconds)
    time.sleep(seconds)

sleep(10)

print("changing the update interval dt to 10 seconds")
dt.write(10)

sleep(20)


print("changing the update interval dt to 1 seconds")
dt.write(1)

sleep(10)
