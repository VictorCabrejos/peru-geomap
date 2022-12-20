from flask import Flask, render_template
import geopandas as gpd

# app = Flask(__name__)



# # Load your geopandas map
# url_geojson = "peru_departamental_simple.geojson"
# region_geojson = gpd.read_file(url_geojson)

# fig, ax = region_geojson.plot(figsize=(15,15))
# plt.ylabel('Latitude')
# plt.xlabel('Longitude')
# plt.show()

# fig.savefig('map.png')


# # Convert the map to an HTML element
# html = ax.to_html()

# @app.route('/')
# def index():
#     return html


# if __name__ == '__main__':
#     app.run()

#**********************************


# app = Flask(__name__)

# @app.route('/')
# def map():
#     # load the map data
#     map_data = gpd.read_file('peru_departamental_simple.geojson')

#     # render the template and pass in the map data
#     return render_template('map.html', map_data=map_data)

# if __name__ == '__main__':
#     app.run()

import streamlit as st
import geopandas as gpd

url_geojson = "peru_departamental_simple.geojson"
region_geojson = gpd.read_file(url_geojson)
ax = region_geojson.plot(figsize=(15,15))

st.title("Peru Map")
st.pyplot(ax.get_figure())
