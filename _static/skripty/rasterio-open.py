import rasterio

green = rasterio.open('data/B03-2018-05-06.tiff')

# print metadata
print("Bounds:", green.bounds)
