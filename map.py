import folium
import pandas
import datetime
data=input("Please enter the csv file name with the correct extension\n")
df=pandas.read_csv(data)
titles=["OpenStreetMap", "Mapbox Bright", "Mapbox Control Room", "Stamen Terrain", "CartoDB dark_matter"]
i=int(input("Enter the serial Number for tiles to use for the map:\n 1.OpenStreetMap\n 2.Mapbox Bright\n 3. Mapbox Control Room\n 4.Stamen Terrain\n 5.CartoDB dark_matter\n"))
LAT=input("Please enter the column head name for latitude")
LAT=input("Please enter the column head name for longitude")
map= folium.Map(location=[df[LAT].mean(),df[LON].mean()],zoom_start= 4, tiles=titles[i-1])

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

for lat,lon,name,elev in zip(df[LAT],df[LON],df["NAME"],df['ELEV']):
            folium.Marker([lat,lon,], popup=name, icon = folium.Icon(color =color(elev),icon_color="yellow")).add_to(map)


map.save(("Map("+datetime.datetime.now().strftime(" %Y-%m-%d-%H-%M-%S")+").html"))
