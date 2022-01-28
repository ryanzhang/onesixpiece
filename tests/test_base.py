from unittest import skipIf
from xmlrpc.client import boolean
import random
from onesixpiece import BaseClass, base_function

import pytest
given = pytest.mark.parametrize
skipif = pytest.mark.skipif
skip = pytest.mark.skip
xfail = pytest.mark.xfail

@given("fn", [BaseClass(), base_function])
def test_parameterized(fn):
    assert "hello from" in fn()


def test_base_function():
    assert base_function() == "hello from base function"


def test_base_class():
    assert BaseClass().base_method() == "hello from BaseClass"

@skip
def test_func_fast():
    assert 0 == random.randrange(0,2,1) 
    # assert 1==1
    print ("fast")


# @skipif(not pytest.config.getoption("--runslow"))
@skipIf(True , reason="没想好")
def test_func_slow_1():    
    print ('skip slow')

# if 0 == random.randrange(0,2,1):
#     pytest.skip("这个文件无论放哪里，见到，就可以跳过整个文件了！", allow_module_level=True)

#cross failed
@xfail()
def test_func_slow_2():
    assert 1==2
    print ('xfail slow')
