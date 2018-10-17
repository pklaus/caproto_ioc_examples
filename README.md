# caproto\_ioc\_examples

As of 2018-10-17, version 0.1.2 of caproto is not enough, needs the development version:

    pip install --upgrade https://github.com/NSLS-II/caproto/archive/master.zip

## Startup

Run the examples ending in `_ioc.py` with the `--list-pvs` argument. For example:

    ./simple_ioc.py --list-pvs

And then try out the matching `_client.py` client side:

    ./simple_synchronous_client.py
