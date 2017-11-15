"""Python module for converting distance units km to mi and mi to km

"""


def miles_to_kilometers(dist_mi):
	"""Converts miles distance to kilometers

	PARAMETERS
	----------
	dist_mi : float
		Scalar distance kilometers


	RETURNS
	-------
	distance : float
		Scalar distance in miles
	"""

	return 1.609344 * dist_mi


def kilometers_to_miles(dist_km):
	"""Converts km distance to miles

	PARAMETERS
	----------
	dist_km : float
		Scalar distance in kilometers


	RETURNS
	-------
	dist_mi : float
		Scalar distance in kilometers
	"""

	return dist_km / 1.609344


