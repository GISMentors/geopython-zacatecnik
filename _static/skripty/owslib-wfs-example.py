from owslib.wfs import WebFeatureService
# pokud nefunguje na pripojeni https, pouzijeme http
url = 'http://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer'
aopk = WebFeatureService(url)

capabilities = aopk.getcapabilities()
print(capabilities.geturl())

print('{}\n{}\n{}\n{}\n{}'.format(aopk.provider.name,
                                  aopk.identification.title,
                                  aopk.identification.keywords[0],
                                  aopk.identification.fees,
                                  aopk.identification.abstract))

for rec in aopk.contents:
    print(rec)

url='http://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer'
chranena_uzemi_wfs = WebFeatureService(url)
for rec in chranena_uzemi_wfs.contents:
    print(rec)

identifier = 'UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'
print(chranena_uzemi_wfs.contents[identifier])
    
print('{}\n{}'.format(chranena_uzemi_wfs.contents[identifier].boundingBox,
                      chranena_uzemi_wfs.contents[identifier].crsOptions))

features = chranena_uzemi_wfs.getfeature([identifier])
print(features)

print(features.read())

cuzk = WebFeatureService('http://geoportal.cuzk.cz/wfs_au/wfservice.aspx',
                         version="2.0.0")
for c in cuzk.contents:
    print(c)

kraj = cuzk.getfeature(['gmgml:KRAJ'])
print(kraj.read())

vuv = WebFeatureService('http://ags.vuv.cz/arcgis/services/inspire/priority_datasets/MapServer/WFSServer',
                        version="2.0.0")
for c in vuv.contents:
    print(c)

floodedAreas = vuv.getfeature(['inspire_priority_datasets:FD_CZ_1000_floodedAreas'])
print(floodedAreas.read())
