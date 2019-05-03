import pytest

class TestClass:
    def test_one(self):
        print('one')
        x = "this"
        assert 'h' in x

    def test_two(self):
        print('two')
        x = "hello"
        assert hasattr(x, 'abc')
