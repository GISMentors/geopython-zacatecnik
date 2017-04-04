from owslib.wms import WebMapService
zm10_url='http://geoportal.cuzk.cz/WMS_ZM10_PUB/WMService.aspx?service=WMS&request=getCapabilities'
zm10_wms = WebMapService(zm10_url)
print (u'{}\n{}{}\n{}'.format(zm10_wms.identification.title,
                              zm10_wms.identification.abstract,
                              zm10_wms.provider.name,
                              zm10_wms.provider.contact.address))

print (zm10_wms.contents)

print ('{}\n{}'.format(zm10_wms.contents['GR_ZM10'].boundingBox,
                       zm10_wms.contents['GR_ZM10'].boundingBoxWGS84))

img = zm10_wms.getmap(
    layers=['GR_ZM10'],
    size=[800, 600],
    srs="EPSG:5514",
    bbox=[-950003.175021186, -1250003.1750036045, -399990.474995786, -899996.8249909044],
    format="image/png"
)
with open('zm10.png', 'w') as out:
    out.write(img.read())
