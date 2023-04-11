import geopandas as gpd
from glob import glob
import fiona
from sqlalchemy import create_engine
from tqdm import tqdm
import os


# path to data; filetype and recursive iteration may need updating
Data_Path = r"C:/Users/nbasch/Data_4_Jupyter/*.shp"

# Create engine to PostGIS --- "postgresql://[username]:[password]@[Server IP]/[database name]"
try:
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/TRS")
    conn = engine.connect()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connection to PostgreSQL", error)

#Create list of files
files = glob(Data_Path)
print('The number of files in the file path is ' + str(len(files)))

#Iterate through list of files and upload to PostGIS
i = 0
for file in tqdm(files):
    Table_Names = (os.path.basename(file)).lower().replace('.shp', '')
    gdf = gpd.read_file(file)
    gdf.to_postgis(Table_Names, engine, if_exists='replace', chunksize=10000, index=True)

    #Update counter
    i += 1
    print('Finished uploading file number ' + str(i))

if engine:
    conn.close()
    engine.dispose()
    print("PostgreSQL connection is closed")