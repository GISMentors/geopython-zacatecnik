import urllib.request
import rasterio
from rasterio.windows import Window
import rasterio.features
import json, os

class TestRaster:
    def pytest_sessionstart(self):
        self.get_file('B04-2018-05-06.tiff')
        self.get_file('B08-2018-05-06.tiff')

    def get_file(self, filename):
        url = 'https://github.com/GISMentors/geopython-zacatecnik/raw/master/data/' + filename
        urllib.request.urlretrieve(url, filename)

    def create_ndvi(self):
        with rasterio.open('B04-2018-05-06.tiff') as vis:
            vis_data = vis.read().astype(float)[0]

        with rasterio.open('B08-2018-05-06.tiff') as nir:
            nir_data = nir.read().astype(float)[0]

        ndvi = (nir_data - vis_data) / (nir_data + vis_data)

        kwargs = {
            "count": 1,
            "driver": "GTiff",
            "crs": "+init=epsg:4326",
            "dtype": "float32",
            "width": ndvi.shape[1],
            "height": ndvi.shape[0],
            "nodata": -9999,
            "transform": (0.00017964690780272554, 0.0, 14.513969421386719, 0.0, -0.00011842547881016553, 48.866521538507754),
            "compress": "lzw"
        }

        with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
            dst.write_band(1, ndvi.astype(rasterio.float32))

    def create_ndvi_classes(self):
        self.create_ndvi()
        with rasterio.open("ndvi.tif") as src:
            data = src.read(1)

            # reklasifikace začíná
            data[data > 0.6] = 1
            data[(data <= 0.6) & (data > 0.2)] = 2
            data[(data <= 0.2) & (data > -0.1)] = 3
            data[(data <= -0.1)] = 4

            # zápis do souboru
            meta = src.meta
            meta.update(dtype=rasterio.int16, count=1, compress='lzw')
            with rasterio.open('ndvi-classes.tif', 'w', **meta) as dst:
                dst.write_band(1, data.astype(rasterio.int16))

    def test_rasterio_read(self):
        red = rasterio.open('B04-2018-05-06.tiff')
        assert str(red.bounds) == 'BoundingBox(left=14.513969421386719, bottom=48.66330341686951, right=15.073928833007814, top=48.866521538507754)'

        with rasterio.open('B04-2018-05-06.tiff') as vis:
            vis_data = vis.read().astype(float)[0]

        with rasterio.open('B08-2018-05-06.tiff') as nir:
            nir_data = nir.read().astype(float)[0]

        ndvi = (nir_data - vis_data) / (nir_data + vis_data)

        assert ndvi.min() == -0.4162768343479654

    def test_rasterio_write(self):
        self.create_ndvi()

    def test_rasterio_window_read(self):
        with rasterio.open('B04-2018-05-06.tiff') as red:
            w = red.read(1, window=Window(0, 0, 512, 256))

        assert w.shape[0] == 256

    def test_rasterio_vectorize(self):
        self.create_ndvi_classes()
        with rasterio.open("ndvi-classes.tif") as src:
            data = src.read(1)

            # čištění dat
            cleaned = rasterio.features.sieve(data, 100)

            # převod na vektory - vrací generátor
            shapes = rasterio.features.shapes(cleaned, transform=src.transform)

            names = {
                1: "Trees",
                2: "Grass",
                3: "Dry",
                4: "Water",
            }

            features = {
                "type": "FeatureCollection",
                "features": []
            }

            for (geom, val) in shapes:
                val = int(val)
                if val > 0:
                    feature = {
                        "type": "Feature",
                        "properties": {
                            "class": val,
                            "name": names[val]
                        },
                        "geometry": geom
                    }

                    features["features"].append(feature)

            # zápis do souboru
            with open("ndvi-classes.geojson", "w") as out:
                json.dump(features, out)

            assert os.stat('ndvi-classes.geojson').st_size == 25189696
