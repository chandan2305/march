import math_func
import pytest

@pytest.mark.parametrize("num1,num2,result",
                         [
                            (4,5,9)
                            ("hi", "chandan","hi chandan")
                            ("hi", "nikhil","hi nikhil")
                            (8.5,7.4,15.9)
                            
                          ]
                          )


def test_add(num1,num2,result):
    math_func.add(num1,num2)==result