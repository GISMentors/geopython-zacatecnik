import rasterio
from rasterio.windows import Window
import rasterio.features
import json, os

class TestRaster:
    data_dir = os.path.join('tests', 'data')
    def create_ndvi(self):
        with rasterio.open(os.path.join(self.data_dir, 'B04-2018-05-06.tiff')) as vis:
            vis_data = vis.read().astype(float)[0]

        with rasterio.open(os.path.join(self.data_dir, 'B08-2018-05-06.tiff')) as nir:
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
            "transform": (0.00017964690780272554, 0.0, 14.69, 0.0, -0.00011842547881016553, 48.81),
            "compress": "lzw"
        }

        with rasterio.open(os.path.join(self.data_dir, 'ndvi.tif'), 'w', **kwargs) as dst:
            dst.write_band(1, ndvi.astype(rasterio.float32))

    def create_ndvi_classes(self):
        self.create_ndvi()
        with rasterio.open(os.path.join(self.data_dir, "ndvi.tif")) as src:
            data = src.read(1)

            # reklasifikace začíná
            data[data > 0.6] = 1
            data[(data <= 0.6) & (data > 0.2)] = 2
            data[(data <= 0.2) & (data > -0.1)] = 3
            data[(data <= -0.1)] = 4

            # zápis do souboru
            meta = src.meta
            meta.update(dtype=rasterio.int16, count=1, compress='lzw')
            with rasterio.open(os.path.join(self.data_dir, 'ndvi-classes.tif'), 'w', **meta) as dst:
                dst.write_band(1, data.astype(rasterio.int16))

    def test_rasterio_read(self):
        red = rasterio.open(os.path.join(self.data_dir, 'B04-2018-05-06.tiff'))
        assert red.bounds[0] > 14.69469421 and red.bounds[0] < 14.69469422

        with rasterio.open(os.path.join(self.data_dir, 'B04-2018-05-06.tiff')) as vis:
            vis_data = vis.read().astype(float)[0]

        with rasterio.open(os.path.join(self.data_dir, 'B08-2018-05-06.tiff')) as nir:
            nir_data = nir.read().astype(float)[0]

        ndvi = (nir_data - vis_data) / (nir_data + vis_data)

        assert ndvi.min() < -0.05759017 and ndvi.min() > -0.05759018

    def test_rasterio_write(self):
        self.create_ndvi()

    def test_rasterio_window_read(self):
        with rasterio.open(os.path.join(self.data_dir, 'B04-2018-05-06.tiff')) as red:
            w = red.read(1, window=Window(0, 0, 256, 128))

        assert w.shape[0] == 128

    def test_rasterio_vectorize(self):
        self.create_ndvi_classes()
        with rasterio.open(os.path.join(self.data_dir, "ndvi-classes.tif")) as src:
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
            with open(os.path.join(self.data_dir, "ndvi-classes.geojson"), "w") as out:
                json.dump(features, out)

            with open(os.path.join(self.data_dir,"ndvi-classes.geojson"), "r") as infile:
                data = json.load(infile)
                assert len(data['features']) == 23
