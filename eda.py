import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geoplot as gplt
import geoplot.crs as gcrs
import geopandas as gpd
import scipy.stats as stats
import descartes
from shapely.geometry import Point, Polygon

gun_df = pd.read_csv('./data/stage3.csv')

clean_lat_long = gun_df[['n_killed', 'n_injured', 'longitude', 'latitude']].dropna()

geometry = [Point(xy) for xy in zip(clean_lat_long['longitude'], clean_lat_long['latitude'])]
crs = {'init': 'epsg:4326'}
geo_df = gpd.GeoDataFrame(clean_lat_long, crs = crs, geometry=geometry)

contiguous_usa = gpd.read_file(gplt.datasets.get_path('contiguous_usa'))
ax = gplt.polyplot(contiguous_usa, projection=gcrs.AlbersEqualArea())
gplt.kdeplot(geo_df[geo_df['n_killed']>0], cmap='Reds', shade=True, thresh=0, clip=contiguous_usa, ax=ax)

plt.show()