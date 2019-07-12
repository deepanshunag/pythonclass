import pytest
"""def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
"""
"""
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
"""
"""
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
"""

"""
def test_need(tmp_dir):
    print(tmp_dir)
    assert 0
"""
"""
def func(x):
    return x + 1
@pytest.mark.slow
def test_answer():
    assert func(3) == 4
"""
@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass