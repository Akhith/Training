import sys
from geopy.geocoders import Nominatim
def address(long,lat):
	geocoder = Nominatim()
	location = geolocator.reverse(long,lat)
	print(location.address)
def main():
	long=sys.argv[1]
	lat=sys.argv[2]
	address(long,lat)
if __name__=="__main__":
	main()

