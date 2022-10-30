trace-dkey
==========

Python library to trace path of a particular key inside a nested dict

.. image:: https://img.shields.io/pypi/v/trace-dkey
   :target: https://pypi.python.org/pypi/trace-dkey/

.. image:: https://github.com/Agent-Hellboy/trace-dkey/actions/workflows/python-app.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/trace-dkey/
    
.. image:: https://img.shields.io/pypi/pyversions/trace-dkey.svg
   :target: https://pypi.python.org/pypi/trace-dkey/

.. image:: https://img.shields.io/pypi/l/trace-dkey.svg
   :target: https://pypi.python.org/pypi/trace-dkey/

.. image:: https://pepy.tech/badge/trace-dkey
   :target: https://pepy.tech/project/trace-dkey

.. image:: https://img.shields.io/pypi/format/trace-dkey.svg
   :target: https://pypi.python.org/pypi/trace-dkey/

.. image:: https://coveralls.io/repos/github/Agent-Hellboy/trace-dkey/badge.svg?branch=main
   :target: https://coveralls.io/github/Agent-Hellboy/trace-dkey?branch=main

Installation
============

For stable version 
   - pip install trace-dkey

For developement 
   - git clone https://github.com/Agent-Hellboy/trace-dkey
   - cd trace-dkey 
   - python -m venv .venv 
   - source .venv/bin/activate

Example
=======

.. code:: py

   >>> from trace_dkey import trace
   >>> l={'a':{'b':{'c':{'d':{'e':{'f':1}}}}}}
   >>> print(trace(l,'f'))
   [['a', 'b', 'c', 'd', 'e', 'f']]

   Now you can query it as l['a']['b']['c']['d']['e']['f']

   >>> l['a']['b']['c']['d']['e']['f']
   1

General Info
============

| The value returned by the `trace` function is an array of paths, where each path is an array of dictionary keys.
| Because of that, the library can be used in a practical way by taking advantage of this format.
| In the example below we use the returned path to iterate over the dictionary keys and print the key value:

.. code:: py

   from trace_dkey import trace
   l={'a':{'b':{'c':{'d':{'e':{'f':1}}}}}}

   paths = trace(l,'f')

   for path in paths:
      dic = l
      for key in path:
         dic = dic[key]
      print(dic)

Contributing
============

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
