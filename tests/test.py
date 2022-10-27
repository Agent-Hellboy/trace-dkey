from trace_dkey import trace

def test_trace():
    l={'a':{'b':{'c':{'d':{'e':{'f':1}}}}}}
    assert l['a']['b']['c']['d']['e']['f']==1
