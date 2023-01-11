import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from trace_dkey import trace 


@pytest.fixture
def test_trace_fixture():
    dict1 = {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}
    fixture1 = trace(dict1, 'f')
    dict2 = {'a': {'b': {'c': {'d': {'e': {('h','i'): ('h', 'i')}, 'g': 1}}}}}
    fixture2 = trace(dict2, ('h','i'))
    dict3 = {'a': {'b':{'c':{('d','e'):1}}}}
    fixture3 = trace(dict3, 'r')
    dict4 = {'a': {'b': {'c': {('d','e'): 1}}, 'c': 1}}
    fixture4 = trace(dict4, 'c')
    dict5={'a':'b','c':{'d':[{'e':'f'}]}}
    fixture5 = trace(dict5,'e')
    dict6={'a':'b','c':{'d':['e','f']}}
    fixture6 = trace(dict6,'e')
    return fixture1, fixture2, fixture3, fixture4, fixture5, fixture6


def test_when_key_is_string(test_trace_fixture):
    assert test_trace_fixture[0] == [['a', 'b', 'c', 'd', 'e', 'f']]

def test_when_key_is_tuple(test_trace_fixture):
    assert test_trace_fixture[1] == [['a', 'b', 'c', 'd', 'e', ('h', 'i')]]

def test_when_key_is_not_present(test_trace_fixture):
    assert test_trace_fixture[2] == []

def test_when_multiple_keys_found(test_trace_fixture):
    assert test_trace_fixture[3] == [['a', 'b', 'c'], ['a', 'c']]

def test_when_keys_found_in_list(test_trace_fixture):
    assert test_trace_fixture[4] == [['c', 'd','e']]

def test_when_keys_not_found_in_list(test_trace_fixture):
    assert test_trace_fixture[5] == []