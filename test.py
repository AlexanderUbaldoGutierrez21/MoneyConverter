import conversor
import pytest

def test_conversor(self):
    conversor.input = lambda: '1'
    output = conversor.conversor("colombianos", 3875, 1000)
    assert output == 0.26
