import folium
import pandas
import datetime

print("--------------------------------\n\
WEBMAP-LEAFLET (Version 1.1)\n\
Author: Tirtha Sarker\n\
------------------------------   ")
# Take file input and required parameters
data=input("Enter the csv file name with the correct extension: ")
df=pandas.read_csv(data)
titles=["OpenStreetMap", "Mapbox Bright", "Mapbox Control Room", "Stamen Terrain", "CartoDB dark_matter"]
i=int(input("Enter the serial Number for tiles to use for the map:\n 1.OpenStreetMap\n 2.Mapbox Bright\n 3. Mapbox Control Room\n 4.Stamen Terrain\n 5.CartoDB dark_matter\n"))
LAT=input("Enter the column head name for latitude: ")
LON=input("Enter the column head name for longitude: ")
# Create Map based on the parameters taken
map= folium.Map(location=[df[LAT].mean(),df[LON].mean()],zoom_start= 4, tiles=titles[i-1])

# Defining function for feature based on a property
minimum= int(min(df['ELEV']))
step= int((max(df['ELEV'])-minimum)/3)
maximum=int(max(df["ELEV"]))

def color(elev):
    if elev in range(minimum,step+minimum):
        return "red"
    elif elev in range(step+minimum,2*step+minimum):
        return "green"
    elif elev in range (2*step+minimum,maximum):
        return "blue"

# Adding feature to feature group and adding feature to each data point
feature=folium.FeatureGroup(name="Volcanos")
for lat,lon,name,elev in zip(df[LAT],df[LON],df["NAME"],df['ELEV']):
            feature.add_child(folium.Marker([lat,lon,], popup=name, icon = folium.Icon(color =color(elev),icon_color="yellow")))
map.add_child(feature)

#Adding GeoJSON file to the map
geoj=input("Enter the GeoJSON/JSON file to create chorolpleth: ")
folium.GeoJson(data=open(geoj),
name=input("Enter the name for the feature of this GeoJson: "),
style_function=lambda x: {'fillColor' : "red" if x['properties']['POP2005']<=10000000 else 'green' if 10000000< x['properties']['POP2005'] <20000000 else 'yellow'}).add_to(map)

map.add_child(folium.LayerControl())

map.save(("Map("+datetime.datetime.now().strftime(" %Y-%m-%d-%H-%M-%S")+").html"))
