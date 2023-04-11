import geopandas as gpd
import fiona
import psycopg2
from sqlalchemy import create_engine

# path to data; filetype and recursive iteration may need updating
File_GDB_Path = r"C:/Users/nbasch/Desktop/Temp/Script_Working/Project_Area.gdb"

# postgres table name
pg_table_name = "test"

# Create engine to PostGIS --- "postgresql://[username]:[password]@[Server IP]/[database name]"
try:
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/TRS")
    conn = engine.connect()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connection to PostgreSQL", error)

#Iterate through list of feature classes and upload to PostGIS

i = 0
for feature_class in fiona.listlayers(File_GDB_Path):
    feature_class = feature_class.lower()
    print('The number of feature classes in the file path is ' + str(len(fiona.listlayers(File_GDB_Path))))
    gdf = gpd.read_file(File_GDB_Path, driver='FileGDB', layer=feature_class)
    gdf.to_postgis(feature_class, engine, if_exists='replace', chunksize=10000, index=True)

    # Update counter
    i += 1
    print('Finished uploading feature class number ' + str(i))

# Rename table in postgres
with engine.connect() as con:
    try:
        con.execute(rf"ALTER TABLE project_area RENAME TO {pg_table_name};")
    except (Exception, psycopg2.DatabaseError):
        pass

# close the connection.
if engine:
    conn.close()
    engine.dispose()
    print("PostgreSQL connection is closed")