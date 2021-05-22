import folium
import pandas

data = pandas.read_excel('/home/rahul/python3/in.xlsx')
lat = list(data['lat'])
lon = list(data['lng'])
city = list(data['city'])

map =folium.Map(location = [25.96,78.98], zoom_start =6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='india')
for lt ,ln,ct in zip(lat,lon,city):
    fg.add_child(folium.Marker(location = [lt , ln], popup ="%s" % ct,icon =folium.Icon(color = 'blue')))

map.add_child(fg)
map.save('Indian_map.html')