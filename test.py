from conversor import conversor as methodTest
import pytest

def test_conversor():
    assert methodTest("colombianos", 3875, 1000) == 0.26
