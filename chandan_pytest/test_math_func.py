import math_func as m

def test_add():
    assert m.add(5,4)==9
    assert m.add(2,3)==5
    assert m.add(4,2)==6
    assert m.add(1,3)==4
    assert m.add(20,4)==24
    
    
def test_mul():
    assert m.mul(2,3)==6
    assert m.mul(6,4,)==24
    assert m.mul(3,4)==12
    assert m.mul(5,5)==25
    assert m.mul(6,8)==48