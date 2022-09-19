import conversor
import pytest

def test_capital_case():
    assert conversor.conversor("colombianos", 3875, 1000) == 0.26
