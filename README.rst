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

For development
   - git clone https://github.com/Agent-Hellboy/trace-dkey
   - cd trace-dkey
   - python -m venv .venv
   - source .venv/bin/activate

Documentation
=============

For more details, you can refer to the `documentation <https://agent-hellboy.github.io/trace-dkey/>`_.


General Info
============

- The value returned by the `trace` function is an array of paths, where each path is an array of dictionary keys.
- Because of that, the library can be used in a practical way by taking advantage of this format.
- In the example below we use the returned path to iterate over the dictionary keys and print the key value:

.. code:: py

    from trace_dkey import trace
    l={'a':{'b':{'c':{'d':{'e':{'f':1}}}}}}

    paths = trace(l,'f')

    for path in paths:
       dic = l
       for key in path:
          dic = dic[key]
       print(dic)


- This addresses a wide range of questions asked on StackOverflow about key inside a nested dict
- At least 13 duplicate questions can be found on Stackoverflow
- This can be tracked on https://you.com/search?q=find%20key%20in%20nested%20dictionary%20python

API Examples
============

Added example scripts demonstrating how to use trace-dkey with responses from popular APIs. These examples can be found in the `examples` folder:

1. GitHub API Example (`github_api_example.py`): Demonstrates fetching repository information
2. OpenWeatherMap API Example (`openweathermap_api_example.py`): Retrieves current weather data
3. JSONPlaceholder API Example (`jsonplaceholder_api_example.py`): Shows how to interact with a mock REST API

To run these examples:

1. Install the required dependencies:
   ``pip install -r examples/requirements.txt``

2. For the OpenWeatherMap example, you'll need to sign up for a free API key at https://openweathermap.org/ and set it as an environment variable:
   ``export OPENWEATHERMAP_API_KEY=your_api_key_here``

3. Run the examples:
   ``python examples/github_api_example.py``
   ``python examples/openweathermap_api_example.py``
   ``python examples/jsonplaceholder_api_example.py``

These examples demonstrate how to use trace-dkey to find specific keys in nested JSON responses from real-world APIs.

| Someone made a nice comparison of this lib(trace-dkey) with one of the famous lib(yamlpath) which is doing the similar thing

.. image:: /images/img.png
   :width: 600

Contributing
============

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
