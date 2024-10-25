import simplekml
import gpsd
import time

class GPSKMLGenerator:
    def __init__(self, kml_file_name):
        self.kml = simplekml.Kml()
        self.kml_file_name = kml_file_name
        self.coordinates = []  # List to store the coordinates for the line

    def add_point(self, name, latitude, longitude, description=""):
        """Add a point to the KML file and store its coordinates, but make it invisible."""
        point = self.kml.newpoint(name=name, coords=[(longitude, latitude)], description=description)
        
        # Set the icon to be invisible
        point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/transparent.png'
        point.style.iconstyle.scale = 0  # Scale it to 0 to make it effectively invisible
        
        self.coordinates.append((longitude, latitude))  # Store the coordinates

    def add_line(self):
        """Add a line connecting the stored coordinates to the KML file."""
        if self.coordinates:
            line = self.kml.newlinestring(name="Path", coords=self.coordinates)
            line.altitudemode = simplekml.AltitudeMode.clamptoground
            line.style.linestyle.width = 5  # Set line width
            line.style.linestyle.color = simplekml.Color.red  # Set line color (red in this case)

    def save(self):
        """Save the KML file."""
        self.kml.save(self.kml_file_name)

class GPSDataCollector:
    def __init__(self):
        gpsd.connect()  # Connect to gpsd

    def get_location(self):
        """Fetch the current GPS location."""
        packet = gpsd.get_current()
        if packet.mode >= 2:  # Check if we have a fix (2D or 3D)
            return packet.lat, packet.lon
        return None


    
