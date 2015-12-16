from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_basic_value():
    assert fahr_to_kelvin(20)==266.4833333333333

def test_zero_kelvin():
    assert round(fahr_to_kelvin(-459.67),2)==0.00

@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin("Sometemperature")

@raises(TypeError)
def test_null_temp():
    assert fahr_to_kelvin
