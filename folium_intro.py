import folium
map=folium.Map(location=[28.971996, 77.654629],zoom_start=6,tiles="Mapbox Bright")	
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[28.971996, 77.654629],popup="Hi I am Marker", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")