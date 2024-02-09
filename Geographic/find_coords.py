import geopy
from geopy.geocoders import Nominatim
import argparse
import pandas as pd
 
def findLongLat(x):
    location = geolocator.geocode(x)
    if location is None:
        print(x)
    print(x)
    return [location.longitude,location.latitude]


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",type=str)
args = parser.parse_args()
df = pd.DataFrame(columns=['Address','Institution','Longitude','Latitude'])
geolocator = Nominatim(user_agent="Google Maps")

reader = pd.read_csv(args.file,header=None)
reader.columns = ['Address','Institution']
df['Institution'] = reader['Institution']
df['Address'] = reader['Address']

coords = [findLongLat(row) for row in df['Institution']]
df['Longitude'] = [x[0] for x in coords]
df['Latitude'] = [x[1] for x in coords]
df.to_csv('final_remaining_locations.csv',header=True,index=False)
    