python-lightify
===============

Python module for OSRAM_ Lightify_
Based on work from Mikael Magnusson. (Github: mikma_)

Packaged up for pypi_ by Andreas Neumeier

It communicates with a Lightify gateway connected to the same LAN via
TCP port 4000 using a binary protocol.

This is a work in progress.

Usage
-----

.. code:: shell

    pip install lightify

Example
-------

Turn on all lights connected to the gateway.

.. code:: python

    from lightify import Lightify
    
    lightify = Lightify("Lightify-Hostname")
    lightify.update_all_light_status()
    lights = lightify.lights()
    for light in lights.keys():
      lights[light].set_onoff(True)


.. _OSRAM: http://www.osram.com
.. _Lightify: http://led.osram.de/lightify
.. _pypi: https://pypi.python.org/pypi/lightify/
.. _mikma: https://github.com/mikma/python-lightify
