import os
import pytest

import fiona
from shapely.geometry import shape

@pytest.fixture(scope='class')
def fiona_open(request):
    with fiona.open(request.cls.sample_file, 'r', encoding='utf-8') as chko:
        request.cls.geom = shape(chko[0]['geometry'])

    yield
        
@pytest.mark.usefixtures('fiona_open')
class TestShapely:
    sample_file = os.path.join('tests', 'data', 'chko.shp')

    def test_shapely_geom(self):
        assert int(self.geom.area) == 905

    def test_shapely_simplify(self):
        simple = self.geom.simplify(10)

        assert len(simple.exterior.coords) == 5

    def test_shapely_buffer(self):
        assert int(self.geom.buffer(100).area) == 45931
