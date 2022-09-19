import conversor
import pytest

def test_conversor():
    assert conversor.conversor("colombianos", 3875, 1000) == 0.26
