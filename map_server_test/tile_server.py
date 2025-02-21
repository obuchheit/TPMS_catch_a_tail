from flask import Flask, send_file, abort
import sqlite3
import io

app = Flask(__name__)
MBTILES_PATH = "missouri.mbtiles" 
def get_tile(z, x, y):
    """Retrieve a tile from the MBTiles database."""
    y_flipped = (1 << z) - 1 - y  

    conn = sqlite3.connect(MBTILES_PATH)
    cur = conn.cursor()
    cur.execute("SELECT tile_data FROM tiles WHERE zoom_level=? AND tile_column=? AND tile_row=?", (z, x, y_flipped))
    tile = cur.fetchone()
    conn.close()

    if tile:
        return io.BytesIO(tile[0])  # Return image data
    return None

@app.route('/tiles/<int:z>/<int:x>/<int:y>.png')
def serve_tile(z, x, y):
    """Serve the requested tile as a PNG image."""
    tile_data = get_tile(z, x, y)
    if tile_data:
        return send_file(tile_data, mimetype="image/png")
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
