# coding=utf-8
from owslib.wfs import WebFeatureService
# nefunguje na pripojeni https, pouzijeme http
url = 'http://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer'
aopk = WebFeatureService(url)

capabilities = aopk.getcapabilities()
print (capabilities.geturl())

print (u'{}\n{}\n{}\n{}\n{}'.format(aopk.provider.name,
                                    aopk.identification.title,
                                    aopk.identification.keywords[0],
                                    aopk.identification.fees,
                                    aopk.identification.abstract))

for rec in aopk.contents:
    print (rec)

url='http://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer'
chranena_uzemi_wfs = WebFeatureService(url)
for rec in chranena_uzemi_wfs.contents:
    print (rec)

identifier = u'ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'
print (chranena_uzemi_wfs.contents[identifier])
    
print ('{}\n{}'.format(chranena_uzemi_wfs.contents[identifier].boundingBoxWGS84,
                       chranena_uzemi_wfs.contents[identifier].crsOptions))

# getfeature nepodporuje UTF-8
identifier = 'ChranUzemi:Zonace_velkoplo\xc5\xa1n\xc3\xa9ho_zvl\xc3\xa1\xc5\xa1t\xc4\x9b_chr\xc3\xa1n\xc4\x9bn\xc3\xa9ho_\xc3\xbazem\xc3\xad'
features = chranena_uzemi_wfs.getfeature([identifier])
print (features)

print (features.read())

cuzk = WebFeatureService('http://geoportal.cuzk.cz/wfs_au/wfservice.aspx',
                         version="2.0.0")
for c in cuzk.contents:
    print (c)

kraj = cuzk.getfeature(['gmgml:KRAJ'])
print (kraj.read())
