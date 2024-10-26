import simplekml
import gpsd
import time


class GPSKMLGenerator:
    def __init__(self, kml_file_name):
        self.kml = simplekml.Kml()
        self.kml_file_name = kml_file_name
        self.coordinates = []  # List to store the coordinates for the line

    def add_point(self, latitude, longitude):
        """Store the coordinates for the line."""
        self.coordinates.append((longitude, latitude))  # Store the coordinates

def save_kml(kml, kml_file_name, coordinates):
    """Add a line to the KML file and save it."""
    # Add a line connecting the stored coordinates to the KML file
    if coordinates:
        line = kml.newlinestring(name="Path", coords=coordinates)
        line.altitudemode = simplekml.AltitudeMode.clamptoground
        line.style.linestyle.width = 5  # Set line width
        line.style.linestyle.color = simplekml.Color.red  # Set line color (red in this case)

    # Save the KML file
    kml.save(kml_file_name)

class GPSDataCollector:
    def __init__(self):
        gpsd.connect()  # Connect to gpsd

    def get_location(self):
        """Fetch the current GPS location."""
        packet = gpsd.get_current()
        if packet.mode >= 2:  # Check if we have a fix (2D or 3D)
            return packet.lat, packet.lon
        return None

# def continuously_run(gps_collector, kml_generator):
#     """Continuously collect GPS data."""
#     while running2:
#         location = gps_collector.get_location()
#         if location:
#             latitude, longitude = location
#             kml_generator.add_point(latitude, longitude)  # Only store coordinates
#             print(f"Added point: {latitude}, {longitude}")

#         time.sleep(1)  # Add a sleep to avoid overwhelming the GPS daemon
#     save_kml(kml_generator.kml, kml_generator.kml_file_name, kml_generator.coordinates)
#     print("KML file saved.")

# Main execution
# if __name__ == "__main__":
#     # Initialize GPS data collector and KML generator
#     gps_collector = GPSDataCollector()
#     kml_generator = GPSKMLGenerator("my_gps_data.kml")

#     try:
#         continuously_run(gps_collector, kml_generator)
#     except KeyboardInterrupt:
       # print("Stopping GPS data collection.")
    
    # Save the KML file with the line when done
    # save_kml(kml_generator.kml, kml_generator.kml_file_name, kml_generator.coordinates)
    # print("KML file saved.")
