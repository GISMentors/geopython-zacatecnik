import rasterio

with rasterio.open("outputs/ndvi.tif") as src:
    data = src.read(1)

    # reklasifikace začíná
    data[data > 0.6] = 1
    data[(data <= 0.6) & (data > 0.2)] = 2
    data[(data <= 0.2) & (data > -0.1)] = 3
    data[(data <= -0.1)] = 4

    # zápis do souboru
    meta = src.meta
    meta.update(dtype=rasterio.int16, count=1, compress='lzw')
    with rasterio.open('outputs/ndvi-classes.tif', 'w', **meta) as dst:
        dst.write_band(1, data.astype(rasterio.int16))
