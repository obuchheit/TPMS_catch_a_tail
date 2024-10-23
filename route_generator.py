import time
from gps3 import GPS3
import simplekml

class RouteMaker:
    def __init__(self):
        self.gps_socket = GPS3()
        self.data_stream = self.gps_socket.get_current_data()
        self.kml = simplekml.Kml()
        self.track_name = "GPS-Track" #Add unique naming somehow
        self.points = []

    def start_tracking(self):
        """Start tracking GPS data and populating KML points."""
        self.gps_socket.stream()
        print("Tracking GPS data...")

        try:
            while True:
                self.data_stream = self.gps_socket.get_current_data()
                if self.data_stream['lat'] != 0.0 and self.data_stream['lon'] != 0.0:
                    self.add_point(self.data_stream['lat'], self.data_stream['lon'])
                time.sleep(5)  # Adjust the frequency as necessary
        except KeyboardInterrupt:
            print("Tracking stopped.")
            self.create_kml()

    def add_point(self, lat, lon):
        """Add a GPS point to the KML file."""
        print(f"Adding point: Latitude={lat}, Longitude={lon}")
        self.points.append((lat, lon))
        self.kml.newpoint(name="GPS Point", coords=[(lon, lat)])  # Note: KML uses (lon, lat)

    def create_kml(self):
        """Create the KML file with the collected GPS points."""
        if not self.points:
            print("No GPS points collected.")
            return

        # Create a line string for the track
        line = self.kml.newlinestring(name=self.track_name, coords=[(lon, lat) for lat, lon in self.points])
        line.altitudemode = simplekml.AltitudeMode.clamptoground

        # Save the KML file
        kml_filename = f"{self.track_name.replace(' ', '_')}.kml"
        self.kml.save(kml_filename)
        print(f"KML file created: {kml_filename}")



