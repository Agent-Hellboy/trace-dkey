from contextlib import redirect_stdout
import io
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from trace_dkey import trace 

def get_stdout_of_trace(l,p):
    f = io.StringIO()
    with redirect_stdout(f):
        trace(l,p)
    return f.getvalue()


@pytest.fixture
def test_trace_fixture():
    dict1 = {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}
    fixture1 = get_stdout_of_trace(dict1,'f')
    dict2 = {'a': {'b': {'c': {'d': {'e': {('h','i'): ('h', 'i')}, 'g': 1}}}}}
    fixture2 = get_stdout_of_trace(dict2,('h','i'))
    dict3 = {'a': {'b':{'c':{('d','e'):1}}}}
    fixture3 = get_stdout_of_trace(dict2,'r')
    return fixture1, fixture2, fixture3


def test_when_key_is_string(test_trace_fixture):
    assert test_trace_fixture[0][:-1] == f"Found 'f' at  a--> b--> c--> d--> e-->f"

def test_when_key_is_tuple(test_trace_fixture):
    assert test_trace_fixture[1][:-1] == f"Found '('h', 'i')' at  a--> b--> c--> d--> e-->('h', 'i')"

def test_when_key_is_not_present(test_trace_fixture):
    assert test_trace_fixture[2][:-1] == ''