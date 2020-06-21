from app import app
from flask import render_template
import folium

@app.route('/')
def index():
	return render_template('index.html')
	# start_coords = (41.38879, 2.15899)
	# folium_map = folium.Map(location=start_coords, zoom_start=10)
	# return folium_map._repr_html_()