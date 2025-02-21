import customtkinter as ctk
from tkintermapview import TkinterMapView

# Main Application
class OfflineMapApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Offline Map Viewer")

        # Create a TkinterMapView widget
        self.map_widget = TkinterMapView(self, width=800, height=600)
        self.map_widget.pack(fill="both", expand=True)

        # Set tile server
        self.map_widget.set_tile_server("http://127.0.0.1:5000/tiles/{z}/{x}/{y}.png")

        # Set initial view
        self.map_widget.set_zoom(10)
        self.map_widget.set_position(38.4435,-91.0030)  # Example coordinates 

if __name__ == "__main__":
    app = OfflineMapApp()
    app.mainloop()