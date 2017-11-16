"""
Python module for converting temperature units F to C or C to F

"""

def celsius_to_fahrenheit(temp):
	"""Converts temperature units C to F

	PARAMETERS
	----------
	temp : float
		Scalar temp in Celsius


	RETURNS
	-------
	float
		Scalar temp in Fahrenheit
	"""
	return 9/5*temp + 32

def fahrenheit_to_celsius(temp):
	"""Converts temperature units F to C

	PARAMETERS
	----------
	temp : float
		Scalar temp in Fahrenheit


	RETURNS
	-------
	float
		Scalar temp in Celsius
	"""
	return (5/9)*(temp - 32)




