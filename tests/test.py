from trace_dkey import trace

def test_trace_1():
    l = {'a':{'b':{'c':{'d':{'e':{'f':1}}}}}}
    assert l['a']['b']['c']['d']['e']['f']==1

def test_trace_2():
    l = {'a':{'b':{'c':{'d':{'e':{'f':('h','i')},'g':1}}}}}
    assert l['a']['b']['c']['d']['e']['f']==('h','i')
