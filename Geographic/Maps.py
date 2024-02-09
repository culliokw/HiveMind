import pandas as pd
from shapely.geometry import Point
import PyQt5
import matplotlib
import geopandas as gpd
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
df=pd.read_csv("FILE HERE",header=0)
df=df.dropna()
points = df.apply(lambda row: Point(row.Long, row.Lat), axis=1)
sites = gpd.GeoDataFrame(df, geometry=points)
ax = countries.plot(color='lightgrey', linewidth=0.5, edgecolor='white', figsize=(15,5))
sites.plot(markersize=5, color='blue', alpha=.20, ax=ax)
fig, ax = matplotlib.pyplot.subplots()
sites.plot(markersize=10, color='pink', alpha=0.75, ax=ax)
ax.axis('off')
matplotlib.pyplot.savefig("sites.png")