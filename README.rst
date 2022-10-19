trace-dkey
==========

Python library to trace path of a particular key inside a nested dict

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
   >>> trace(l,'f')
   Found 'f' at  a--> b--> c--> d--> e-->f

   Now you can query it as l['a']['b']['c']['d']['e']['f']

   >>> l['a']['b']['c']['d']['e']['f']
   1

Contributing
============

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
