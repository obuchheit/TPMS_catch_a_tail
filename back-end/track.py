import simplekml
import gpsd


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

