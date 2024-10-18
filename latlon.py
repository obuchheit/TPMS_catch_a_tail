import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radius of Earth in kilometers (use 3956 for miles)
    r = 6371.0
    return c * r


lat1, lon1 = 52.2296756, 21.0122287  
lat2, lon2 = 41.8919300, 12.5113300  

distance = haversine(lat1, lon1, lat2, lon2)
print(f"Distance: {distance:.2f} km")