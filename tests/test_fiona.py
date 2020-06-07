import os
import fiona
from fiona.crs import from_epsg
        
class TestFiona:
    data_dir = os.path.join('tests', 'data')
    sample_file = 'chko.shp'
    nfeat = 3
    nprop = 14
    
    def test_fiona_open(self):
        with fiona.open(os.path.join(self.data_dir, self.sample_file), 'r', encoding='utf-8') as chko:
            # metadata
            assert chko.driver == 'ESRI Shapefile'
            
            # number of features
            assert len(chko) == self.nfeat
            
            # attributes
            assert len(chko.meta['schema']['properties'].keys()) == self.nprop

    def test_fiona_crs(self):
        assert from_epsg(5514)['init'] == 'epsg:5514'

    def test_fiona_read(self):
        with fiona.open(os.path.join(self.data_dir, self.sample_file), 'r', encoding='utf-8') as chko:

            # seq read
            n = 0 
            for feature in chko:
                n += 1
            assert n == self.nfeat

            # random
            assert chko[0]['properties']['NAZEV'] == 'Bílé Karpaty'
        
