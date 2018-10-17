#!/usr/bin/env python3
import time
from caproto.threading.client import Context


ctx = Context()

keypress, = ctx.get_pvs('io:keypress')

res = keypress.read()
print("Keypress value when startup up: %s" % res.data[0])

sub = keypress.subscribe()

def f(response):
    print("New keypress received: %s" % response.data[0])

token = sub.add_callback(f)

def sleep(seconds):
    print("sleeping for %s seconds" % seconds)
    time.sleep(seconds)

sleep(120)
