from owslib.wms import WebMapService
url='https://geoportal.cuzk.cz/WMS_ZM10_PUB/WMService.aspx'
wms = WebMapService(url)
print('{}\n{}{}\n{}'.format(wms.identification.title,
                            wms.identification.abstract,
                            wms.provider.name,
                            wms.provider.contact.address))

print(wms.contents)

layer = list(wms.contents.keys())[0]
print('{}\n{}'.format(wms.contents[layer].boundingBox,
                      wms.contents[layer].boundingBoxWGS84))

img = wms.getmap(
    layers=[layer],
    size=[800, 600],
    srs="EPSG:5514",
    bbox=[-950003, -1250003, -399990, -899996],
    format="image/png"
)
with open('data/wms_download.png', 'wb') as out:
    out.write(img.read())
