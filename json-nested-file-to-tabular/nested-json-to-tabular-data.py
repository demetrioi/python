import pandas as pd
import json

filepath = "/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/json-nested-file-to-tabular/cars.json"

with open(filepath, 'r') as f:
    data = json.load(f)  # Dict

# CSV Sample - Structure - "/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/json-nested-file-to-tabular/cars.json"
"""
{
    "values": [
        {
            "id": 1,
            "name": "Toyota",
            "details": {
                "name": "Corolla",
                "horsepower": "140",
                "color": "black"
            }
        },
        {
            "id": 2,
            "name": "Toyota",
            "details": {
                "name": "Camry",
                "horsepower": "170",
                "color": "blue"
            }
        },
        ...
"""

FIELDS = ["id", "name", "details.name", "details.horsepower", "details.color"]

df = pd.json_normalize(data, record_path="values")[FIELDS]

print(df.head())
