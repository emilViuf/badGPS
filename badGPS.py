import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt

# Start & stop
orig_address = "Hannemanns Allé 25, 2300 København"
dist_address = "Osvald Helmuths Vej 4, 2000 Frederiksberg"

#(latitude, longitude) coordinates
orig_point = ox.geocode(orig_address)
dist_point = ox.geocode(dist_address)

# Forøg hvis route fejler
buffer = 0.1  

# bounding box 
north = max(orig_point[0], dist_point[0]) + buffer
south = min(orig_point[0], dist_point[0]) - buffer
east = max(orig_point[1], dist_point[1]) + buffer
west = min(orig_point[1], dist_point[1]) - buffer
G = ox.graph_from_bbox(north, south, east, west, network_type='drive', simplify=True)

# Finder tætteste nodes på adresser
orig = ox.distance.nearest_nodes(G, orig_point[1], orig_point[0])
dist = ox.distance.nearest_nodes(G, dist_point[1], dist_point[0])

#Shortest path
route = nx.shortest_path(G, orig, dist)

# Plot graph & route
fig, ax = ox.plot_graph_route(G, route, route_linewidth=4, node_size=0, bgcolor='black', save=True, filepath='route_graph.png')

plt.show()
