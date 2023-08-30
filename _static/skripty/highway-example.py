import fiona
import json
from shapely.geometry import mapping, shape
from fiona.transform import transform_geom
from shapely.ops import cascaded_union
from shapely import speedups

speedups.enable()

with fiona.open("data/chko.shp", "r") as pas:
    with fiona.open("data/highways.geojson", "r") as hws:

        buffered_highways = []

        wgs84 = "EPSG:4326"
        jtsk = pas.crs

        d8 = list(filter(lambda hw: hw["properties"]["ref"] == "D8", hws))

        for hw in d8:
            geom_transformed = transform_geom(wgs84, jtsk, hw["geometry"])

            g = shape(geom_transformed)
            buffered_highways.append(g.buffer(100))

        intersections = []

        for hw in buffered_highways:

            for pa in pas:

                pa_geom = shape(pa["geometry"])
                if hw.intersects(pa_geom):
                    out_geom = hw.intersection(pa_geom)
                    intersections.append(out_geom)

        one_geometry = cascaded_union(intersections)

with open("d8_x_chko.geojson", "w") as out:
    data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "highway": "D8",
                    "area": one_geometry.area
                },
                "geometry": transform_geom(jtsk, wgs84, mapping(one_geometry))
            }
        ]
    }
    json.dump(data, out)
