import rasterio

with rasterio.open('data/B04-2018-05-06.tiff') as vis:
    vis_data = vis.read().astype(float)[0]

with rasterio.open('data/B08-2018-05-06.tiff') as nir:
    nir_data = nir.read().astype(float)[0]
    meta = nir.meta

ndvi = (nir_data - vis_data) / (nir_data + vis_data)

print (ndvi.min(), ndvi.max())

meta["dtype"] = "float32"

with rasterio.open('outputs/ndvi.tif', 'w', **meta) as dst:
   dst.write_band(1, ndvi.astype(rasterio.float32))
