# Webmap-Leaflet-with-Folium
Folium helps us  build webmap leaflets of the leaflet.js through the data manipulation strenghts of python. The application enables us to take a geo data set and visualize it, add filter tiles layout, control the layout features and also add geojson files to have 
choropleth maps based on particular data feature.

##  How to use the application

The Project contains **map.py** as the primary script. On running the script, a html file will be generated. 
This html file can be opened on any standard web browser and the webmap leaflet will be displayed. There are options to choose map tiles according to preference within the script.
Here I have used sample data in csv format. Please download the "Sample_Data_Volcano_USA.txt" file along with the script to see the corresponding web map.


## Update 
### Version 1.1
- [x] Added Choropleth map display feature via GeoJson file data
![webmap_ss1](https://cloud.githubusercontent.com/assets/18365101/24584350/80eb7f9a-1788-11e7-8c22-79110b966eef.png)

- [x] Added Layer Control Feature
![webmap_ss2](https://cloud.githubusercontent.com/assets/18365101/24584368/f170c676-1788-11e7-873d-9a40a6cb4a50.png)


## Getting GeoJson data
The GeoJson data can be obtained from a Shapefile. The shapefile comes as a zip bundle of multiple files containing parts of geolocation data. We can use any standard geo data file converter to convert the shapefile to GeoJson. 
