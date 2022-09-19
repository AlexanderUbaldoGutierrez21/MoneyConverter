from conversor import conversor as methodTest
import pytest

def test_conversor(self):
    module.input = lambda: '1'
    output = methodTest("colombianos", 3875, 1000)
    assert output == 0.26
