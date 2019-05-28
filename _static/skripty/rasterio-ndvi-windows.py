import rasterio
from rasterio.windows import Window

with rasterio.open('data/B04-2018-05-06.tiff') as red:
    with rasterio.open('data/B08-2018-05-06.tiff') as nir:

        step = 256
        kwargs = red.meta
        kwargs.update(dtype=rasterio.float64, count=1, compress='lzw')

        with rasterio.open('data/ndvi.tif', 'w', **kwargs) as dst:
            slices = [(col_start, row_start, step, step) \
                        for col_start in list(range(0, red.width, 256)) \
                        for row_start in list(range(0, red.height, 256))
            ]

            # nepoužijeme block windows, protože data používají 1x1287 velké bloky
            # for ji, window in src.block_windows(1):
            for slc in slices:
                win = Window(*slc)

                nir_data = nir.read(1, window=win)
                vis_data = red.read(1, window=win)

                ndvi = (nir_data - vis_data) / (nir_data + vis_data)

                write_win = Window(slc[0], slc[1], ndvi.shape[1], ndvi.shape[0])

                dst.write_band(1, ndvi.astype(rasterio.float64), window=write_win)
