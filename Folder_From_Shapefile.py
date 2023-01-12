import geopandas as gpd 
import os

# Path to output folder location 
output_folder = r"C:\Users\nbasch\Desktop\Make_Folder_from_Shapefile"

# Read in shapefile
homesites = gpd.read_file(r"N:\projects\2022\225188C215378 NTUA 14 Homesites Technical Studies (1.BIO)\Biology\gis\homesite_locations.shp")
homesites = homesites[['Name']]
print(homesites.head())

# Convert column to list and create folders 
folder_list = homesites['Name'].tolist()
for folder in folder_list:
    folder = folder.replace(' ', '_')
    os.makedirs(os.path.join(output_folder, folder), exist_ok=True)