import pytest

@pytest.fixture
def test_trace_fixture():
    l1 = {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}
    l2 = {'a': {'b': {'c': {'d': {'e': {'f': ('h', 'i')}, 'g': 1}}}}}
    l3 = {'a': {'b':{'c':{('d','e'):1}}}}
    fixture1 = l1['a']['b']['c']['d']['e']['f']
    fixture2 = l2['a']['b']['c']['d']['e']['f']
    fixture3 = l3['a']['b']['c'][('d','e')]
    return fixture1, fixture2, fixture3


def test_with_fixture(test_trace_fixture):
    assert test_trace_fixture[0] == 1
    assert test_trace_fixture[1] == ('h','i')
    assert test_trace_fixture[2] == 1

