from Calculator import *

def test_add1():
    assert add(2,3)==5

def test_add2():
    assert add(-2,3)==1

def test_add3():
    assert add(0,0)==0

def test_sub1():
    assert sub(5,2)==3

def test_sub2():
    assert sub(2,5)==-3

def test_mul1():
    assert mul(2,3)==6

def test_mul2():
    assert mul(0,10)==0

def test_div1():
    assert div(10,2)==5

def test_div2():
    assert div(9,3)==3

def test_div3():
    assert div(5,2)==2.5