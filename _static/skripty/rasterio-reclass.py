import rasterio

with rasterio.open("outputs/ndvi.tif") as src:
    data = src.read(1)

    # reklasifikace začíná
    data[data > 0.3] = 1
    data[(data <= 0.3) & (data > -0.35)] = 2
    data[(data <= -0.35)] = 3

    # zápis do souboru
    meta = src.meta
    meta.update(dtype=rasterio.uint16, count=1, compress='lzw')
    with rasterio.open('outputs/ndvi-classes.tif', 'w', **meta) as dst:
        dst.write_band(1, data.astype(rasterio.uint16))
