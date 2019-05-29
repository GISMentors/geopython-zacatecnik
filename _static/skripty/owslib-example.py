from owslib.csw import CatalogueServiceWeb
cenia = CatalogueServiceWeb('http://geoportal.gov.cz/php/micka/csw/index.php')
print (cenia.service)

cenia.getrecords2()
print (cenia.results)

for rec in cenia.records:
    print (cenia.records[rec].title)

from owslib.fes import PropertyIsLike, BBox, And, PropertyIsEqualTo
wms_query = PropertyIsEqualTo('csw:AnyText', 'WMS')
praha_query = BBox([14.22,49.94,14.71,50.18])
praha_and_wms = And([praha_query, wms_query])
cenia.getrecords2([praha_and_wms], esn='full')
print (cenia.results)

for recid in cenia.records:
    record = cenia.records[recid]
    print (u'{}: {} {} {} {}'.format(record.title, record.bbox.minx, record.bbox.miny,
                                     record.bbox.maxx, record.bbox.maxy))

zm_query = PropertyIsEqualTo('csw:AnyText', '%ZM10%')
cenia.getrecords2([zm_query], esn='full')
zm10 = cenia.records['CZ-CUZK-WMS-ZM10-P']
print (zm10.type)

print (u'{}\n{}'.format(zm10.title, zm10.abstract))

url = zm10.references[0]['url']

wfs_query = PropertyIsLike('csw:AnyText', 'WFS%')
aopk_query = PropertyIsLike('csw:AnyText', 'Agentura%')
service_query = PropertyIsLike('apiso:type', 'service')
aopk_and_wfs = And([aopk_query, wfs_query, service_query])
cenia.getrecords2([aopk_and_wfs], esn='full')
print (cenia.results)

for recid in cenia.records:
    record = cenia.records[recid]
    print (u'{}: {}'.format(recid, record.title))

natura = cenia.records['53e37222-89a0-472b-9781-5bfc0a02080a']
print (u'{}\n{}'.format(natura.abstract, natura.identifiers[1]['identifier']))
