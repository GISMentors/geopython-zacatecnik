import rasterio

with rasterio.open('outputs/ndvi.tif') as ndvi:
    water = ndvi.read()

limit = 0.1

water[water < -1*limit] = -9999
water[water > limit] = -9999
water[(water >= -1.0*limit) & (water <= 0.1)] = 1

kwargs = ndvi.meta
kwargs.update(dtype=rasterio.int32, count=1, compress='lzw', nodata=-9999)
with rasterio.open('outputs/water.tif', 'w', **kwargs) as dst:
    dst.write_band(1, water[0].astype(rasterio.int32))
