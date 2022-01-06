import sys
from geopy.geocoders import Nominatim
def address(longitude,latitude):
	geocoder = Nominatim(user_agent = "my-applications")
	location = geocoder.reverse((longitude,latitude))
	print(location.address)
def main():
	longitude=sys.argv[1]
	latitude=sys.argv[2]
	address(longitude,latitude)
if __name__=="__main__":
	main()
