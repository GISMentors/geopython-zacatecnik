from owslib.wms import WebMapService as WMS
from owslib.csw import CatalogueServiceWeb as CSW

def test_wms():
    url = "https://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx"
    wms = WMS(url)

    assert wms

    response = wms.getmap(
            size=[800, 800],
            srs="epsg:4326",
            bbox=[15, 50, 15.5, 50.5],
            format="image/jpeg",
            layers=["GR_ORTFOTORGB"]
            )

    assert response
    assert int(response.info()["Content-Length"])

# def test_csw():
#     url = "http://micka.cenia.cz/metadata/csw/index.php"
#     csw = CSW(url)

#     assert csw

#     csw.getrecords2()

#     assert csw.results["matches"] > 0
