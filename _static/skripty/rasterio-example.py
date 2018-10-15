import rasterio

with rasterio.open('data/B04-2018-05-06.tiff') as vis:
    vis_data = vis.read().astype(float)[0]

with rasterio.open('data/B08-2018-05-06.tiff') as nir:
    nir_data = nir.read().astype(float)[0]

ndvi = (nir_data - vis_data) / (nir_data + vis_data)

print (ndvi.min(), ndvi.max())

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

with rasterio.open('outputs/ndvi.tif', 'w', **kwargs) as dst:
   dst.write_band(1, ndvi.astype(rasterio.float32))
