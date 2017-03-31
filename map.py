import folium
import pandas
map= folium.Map(location=[48.1118011,-121.1110001],zoom_start= 4, tiles="Stamen Terrain")
df=pandas.read_csv("Sample_Data_Volcano_USA.txt")
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
for lat,lon,name,elev in zip(df["LAT"],df["LON"],df["NAME"],df['ELEV']):
            folium.Marker([lat,lon,], popup=name, icon = folium.Icon(color =color(elev),icon_color="yellow")).add_to(map)

#folium.CircleMarker([22.5867,88.4171],radius=150, popup='SALTLAKE CITY',fill_color='#3186cc').add_to(map)
map.save("map.html")
