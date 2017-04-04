import rasterio
src = rasterio.open('data/lsat7_2002_nir.tiff')
print (src.bounds)

print (src.crs)
    
print (src.tags())

print (src.width, src.height)

print (src.res)

data = src.read()
print (len(data))

(nir, vis) = (data[0], data[1])
ndvi = (nir - vis) / (nir + vis)
print (ndvi.min(), ndvi.max())

kwargs = src.meta
kwargs.update(dtype=rasterio.float64, count=1, compress='lzw')
with rasterio.open('data/ndvi.tif', 'w', **kwargs) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float64))
