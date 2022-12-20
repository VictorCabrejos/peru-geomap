
import geopandas as gpd
import streamlit as st


url_geojson = "peru_departamental_simple.geojson"
region_geojson = gpd.read_file(url_geojson)
# ax = region_geojson.plot(figsize=(15,15))


ax = region_geojson.plot(figsize=(20,20),edgecolor=u'white', color='grey', alpha=0.3, linewidth=3)
region_geojson[region_geojson['NOMBDEP'] == 'ANCASH'].plot(ax=ax, color='orange', edgecolor=u'white', label='Presupuesto')
region_geojson[region_geojson['NOMBDEP'] == 'HUANUCO'].plot(ax=ax, color='orange', edgecolor=u'white')
region_geojson[region_geojson['NOMBDEP'] == 'LIMA'].plot(ax=ax, color='orange', edgecolor=u'white')
region_geojson[region_geojson['NOMBDEP'] == 'CUSCO'].plot(ax=ax, color='orange', edgecolor=u'white')
region_geojson[region_geojson['NOMBDEP'] == 'PUNO'].plot(ax=ax, color='orange', edgecolor=u'white')

# remove the axis
ax.axis('off')

# add custom text box
ax.text(-0.1, 0.05, 'Presupuesto Inversión y Devengado (Mill. S/)', transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='orange', alpha=0.5))

# Add text pointing to the region
ax.text(-80.3, -9.5, 'ANCASH', fontsize=14, color='black', fontweight='bold')
ax.text(-80.8, -9.8, '255,65', fontsize=14, color='red', fontweight='bold')
ax.text(-79.5, -9.8, '143,51', fontsize=14, color='blue', fontweight='bold')

ax.text(-74, -9.5, 'HUANUCO', fontsize=14, color='black', fontweight='bold')
ax.text(-79, -12, 'LIMA', fontsize=14, color='black', fontweight='bold')
ax.text(-72, -12, 'CUSCO', fontsize=14, color='black', fontweight='bold')
ax.text(-69, -15, 'PUNO', fontsize=14, color='black', fontweight='bold')

# add arrows pointing to the region
# ax.annotate('', xy=(-79.5, -9.5), xytext=(-79.5, -12), arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('', xy=(-69.5, -9.5), xytext=(-69.5, -12), arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('', xy=(-79.5, -12), xytext=(-79.5, -15), arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('', xy=(-69.5, -12), xytext=(-69.5, -15), arrowprops=dict(facecolor='black', shrink=0.05))

st.title("SECTOR 36: TRANSPORTES Y COMUNICACIONES EJECUCIÓN INVERSIÓN 2022")
st.pyplot(ax.get_figure())
