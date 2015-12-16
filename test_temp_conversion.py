#This test script contains tests for temperature conversion.
from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_kelvin1():
    assert round(fahr_to_kelvin(10), 3) == 260.928
	
def test_kelvin2():
    assert round(fahr_to_kelvin(-200), 3) == 144.261	

def test_kelvin3():
    assert round(fahr_to_kelvin(-459.67), 2) == 0.0	
	
@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin("SomeTemperature")

@raises(TypeError)
def test_null_temp():
    assert fahr_to_kelvin()
	