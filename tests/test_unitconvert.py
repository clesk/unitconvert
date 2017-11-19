#test program for unitconvert module
#first import unitconvert modules and pytest
from unitconvert import unitconvert.temperature
from unitconvert import unitconvert.distance
import pytest

#define the test function
def test_unitconvert():
	
	#test a few temp conversions rounded to tolerance
	assert round(temperature.celsius_to_fahrenheit(0),1)==32.0
	assert round(temperature.celsius_to_fahrenheit(90),1)==194.0
	assert round(temperature.fahrenheit_to_celsius(0),1)==-17.8
	assert round(temperature.fahrenheit_to_celsius(90),1)==32.2

	#test a few dist conversions rounded to tolerance
	assert round(distance.miles_to_kilometers(100),1)==160.9
	assert round(distance.kilometers_to_miles(100),1)==62.1

	#test n args rejected
	with pytest.raises(TypeError):
		distance.miles_to_kilometers(1, 2)
		temperature.celsius_to_fahrenheit(1, 2)

	#make sure it won't take a string
	with pytest.raises(TypeError):
		temperature.fahrenheit_to_celsius('x')
		distance.kilometers_to_miles('x')