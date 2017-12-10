import rasterio
import rasterio.features
from affine import Affine
import json

with rasterio.open("outputs/ndvi-classes.tif") as src:

    data = src.read(1)

    # čičtění dat
    cleaned = rasterio.features.sieve(data, 100)

    # převod na vektory - vrací generátor
    shapes = rasterio.features.shapes(cleaned, transform=src.transform)

    names = {
            1: "Vegetation",
            2: "Soil",
            3: "Water"
    }


    features = {
        "type": "FeatureCollection",
        "features": []
    }

    for (geom, val) in shapes:
        val = int(val)
        feature = {
            "type": "Feature",
            "properties": {
                "class": val,
                "name": names[val]
            },
            "geometry": geom
        }

        features["features"].append(feature)

    with open("outputs/ndvi-classes.geojson", "w") as out:
        json.dump(features, out)
    # zápis do souboru
