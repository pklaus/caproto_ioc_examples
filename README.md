[caproto.ioc\_examples]: https://github.com/NSLS-II/caproto/tree/master/caproto/ioc_examples

# caproto\_ioc\_examples

The examples are taken from
<https://nsls-ii.github.io/caproto/iocs.html>.
Note, that they are also to be found in the [caproto.ioc\_examples][] subpackage.
What makes this repo here special is that I'm trying to come up with some useful client examples too.

As of 2018-10-17, version 0.1.2 of caproto is not enough, needs the development version:

    pip install --upgrade https://github.com/NSLS-II/caproto/archive/master.zip

## Startup

Run the examples ending in `_ioc.py` with the `--list-pvs` argument. For example:

    ./simple_ioc.py --list-pvs

And then try out the matching `_client.py` client side:

    ./simple_synchronous_client.py
