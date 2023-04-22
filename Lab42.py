#Allison Aranda
#Email: allison.aranda48@myhunter.cuny.edu
#Date:  April 11,2022


import folium

#Create a map, centered (0,0), and zoomed out a bit:
mapWorld = folium.Map(location=[40.75, -74.125],zoom_start=3)
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapWorld)

#Save the map:
mapWorld.save(outfile='nycMap.html')
