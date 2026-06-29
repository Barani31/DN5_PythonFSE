import pytest

@pytest.mark.parametrize(

"a,b,result",

[(2,3,5),

(10,20,30),

(5,5,10)]

)

def test_add(a,b,result):

    assert a+b==result