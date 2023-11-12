# Import necessary modules
import os, json
from caltechdata_api import caltechdata_edit

# Get access token for CaltechDATA as environment variable with source token.bash
token = os.environ["RDMTOK"]

# Open and load metadata from a Datacite JSON file
metaf = open("cd_metadata.json", "r")
metadata = json.load(metaf)

# Set additional parameters
production = True # Indicates that changes will be made in the production environment
parent = "w6hhb-mc015" # Parent dataset or collection ID

# Call the caltechdata_edit function to edit metadata and publish datasets
response = caltechdata_edit(
    parent,
    metadata,
    token,
    ["cell_atlas_offline.zip", "cell_atlas_offline_lite.zip"],
    production,
    publish=True,
)
print(response)
