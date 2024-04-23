import matplotlib.pyplot
import pandas as pd
from shapely.geometry import Point
import PyQt5
import matplotlib
import matplotlib.animation as animation
import geopandas as gpd

def init():
    countries.plot( ax=ax, color='lightgrey', linewidth=0.5, edgecolor='white', figsize=(1000,600)) # Empty Canvas

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.axis('off')

    return ax

def update(frame):
    print("This is frame: " + str(frame))
    print(sites.loc[[frame],'geometry'])
    
    sites.loc[[frame],'geometry'].plot(markersize=8, color='blue', alpha=0.25, ax=ax)
    
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.axis('off')

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
df=pd.read_csv("2004_locations.csv",header=0)
df=df.dropna()
df = df.reset_index()
points = df.apply(lambda row: Point(row.Long, row.Lat), axis=1)
sites = gpd.GeoDataFrame(df, geometry=points)

fig, ax = matplotlib.pyplot.subplots()
ani = animation.FuncAnimation(fig=fig, func=update, frames=range(0,sites.shape[0]), init_func=init, interval=150, repeat=True, blit=False)

ani.save(filename="2004_communication.gif", writer="pillow")