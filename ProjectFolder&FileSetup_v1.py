import os
import shutil

#######Receive user input######
State = "Colorado"
CityState = "EatonCO"
ProjectNumber = "50509"
SDrive_Location = r"S:\IMS Data\Colorado\Eaton (Northern Engr'g)\50509 Northern Eng - Eaton, CO (2022)"
SurveyYear = "2022"
Io_Type = "Titan"       # Titan or Non Titan
#######Receive user input######

#Template filepaths#
MileageUpdate_Template = r"O:\_IMS Data\_Pavemetrics\Jovian Processes\MileageUpdate_Template\empty.xlsx"
Geopackage_Template = r"O:\_IMS Data\_Pavemetrics\Empty Geopackage Template\empty.gpkg"
Ganymede_Template = r"O:\_IMS Data\_Pavemetrics\Jovian Processes\Ganymede\ClientSTYYYY_Ganymede_v4.mdb"
Europa_Script = r"O:\_IMS Data\_Pavemetrics\Jovian Processes\Europa_Orbiter_v3.py"
Titan_Template = r"O:\_IMS Data\_Pavemetrics\Jovian Processes\Io\ClientST_Io_v06_Titan.mdb"
NonTitan_Template = r"O:\_IMS Data\_Pavemetrics\Jovian Processes\Io\ClientST_Io_v06_NonTitan.mdb"
Titan_Script = r"O:\_IMS Data\_Pavemetrics\Jovian Processes\Titan\Titan_Testing\Titan_v2e"
#Template filepaths#

#########Configure O Drive################
ClientProject = CityState + SurveyYear
print("Beginning directory and file configuration in Hot Storage")

try:
    ProjectFolder = rf'O:\{State}\{CityState}_{ProjectNumber}'
    os.mkdir(ProjectFolder)
except FileExistsError:
    pass

# Make primary subdirs
Projectdir_subdirs =  ['GIS', 'Raw', 'Processed']
for i in Projectdir_subdirs:
    os.makedirs(os.path.join(ProjectFolder, i), exist_ok=True)

#Configure GIS folder
path_to_GIS = rf"{ProjectFolder}\GIS"
GIS_subdirs = ['ClearingMap', 'Linking', 'Final Inventory']
for i in GIS_subdirs:
    os.makedirs(os.path.join(path_to_GIS, i), exist_ok=True)
try:
    path_to_Routes = rf"{path_to_GIS}\Linking\Routes"
    os.mkdir(path_to_Routes)
except FileExistsError:
    pass
try:
    path_to_Joins = rf"{path_to_GIS}\Linking\Joins"
    os.mkdir(path_to_Joins)
except FileExistsError:
    pass

path_to_ClearingMap = rf"{path_to_GIS}\ClearingMap"
shutil.copy(MileageUpdate_Template, path_to_ClearingMap)
shutil.copy(Geopackage_Template, path_to_ClearingMap)

try:
    os.chdir(path_to_ClearingMap)
    for file in os.listdir(path_to_ClearingMap):
        os.rename(os.path.join(path_to_ClearingMap, file), file.replace('empty', rf'{CityState}_Clearing'))
except FileExistsError:
    pass

#Configure Processed folder#
path_to_Processed = rf"{ProjectFolder}\Processed"
Processed_Subdirs = ['QC', 'PNGs']
for i in Processed_Subdirs:
    os.makedirs(os.path.join(path_to_Processed, i), exist_ok=True)

#Configure Raw Folder
path_to_Raw = rf"{ProjectFolder}\Raw"
Raw_Subdirs = ['NOMAD', 'IMAGES', 'IMG_TXT']
for i in Raw_Subdirs:
    os.makedirs(os.path.join(path_to_Raw, i), exist_ok=True)

print("Hot Storage Project files configured, Now configuring S Drive...")
#########Configure S Drive################
try:
    path_to_ConditionData = rf"{SDrive_Location}\Condition Data"
    os.mkdir(path_to_ConditionData)
except FileExistsError:
    pass

#Configure Condition Data folder
ConditionData_Subdirs = ['Inventory Check', 'Processed']
for i in ConditionData_Subdirs:
    os.makedirs(os.path.join(path_to_ConditionData, i), exist_ok=True)
#Configure Processed folder
try:
    path_to_Working = rf"{path_to_ConditionData}\Processed\Working"
    os.mkdir(path_to_Working)
except FileExistsError:
    pass

path_to_CSVCombos = rf"{path_to_ConditionData}\Processed\CSVs\CSVCombos"
os.makedirs(path_to_CSVCombos, exist_ok=True)

# Configure Working Folder
shutil.copy(Ganymede_Template, path_to_Working)
try:
    os.chdir(path_to_Working)
    for file in os.listdir(path_to_Working):
        os.rename(os.path.join(path_to_Working, file), file.replace('ClientSTYYYY', ClientProject))
except FileExistsError:
    pass

# Configure Europa Folder
try:
    path_to_Europa = rf'{path_to_Working}\Europa'
    os.mkdir(path_to_Europa)
except FileExistsError:
    pass

shutil.copy(Europa_Script, path_to_Europa)

# Configure Io folder

if Io_Type == 'Titan':
    Europa_subdirs = ['Xmlcombo', 'Io', 'Norpix', 'Flagger']
    for i in Europa_subdirs:
        os.makedirs(os.path.join(path_to_Europa, i), exist_ok=True)
    path_to_Io = rf'{path_to_Europa}\Io'
    path_to_Titan = rf'{path_to_Europa}\Titan'
    shutil.copytree(Titan_Script, path_to_Titan)
    shutil.copy(Titan_Template, path_to_Io)
    print("Titan Io files configured")

elif Io_Type == 'Non Titan':
    Europa_subdirs = ['Xmlcombo', 'Io', 'Norpix', 'Flagger', 'Linking']
    for i in Europa_subdirs:
        os.makedirs(os.path.join(path_to_Europa, i), exist_ok=True)
    path_to_Io = rf'{path_to_Europa}\Io'
    shutil.copy(NonTitan_Template, path_to_Io)
    print("Non Titan Io files configured")

print("End of directory and file configuration")