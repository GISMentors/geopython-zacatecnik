import datetime
from osgeo import ogr, osr

# tolerance ve vymere
tol = 100

# kod zajmove obce
obec = 505528

# posledni datum v mesici (k tomuto dni jsou publikovana stavova data)
today = datetime.date.today()
if today.month == 12:
	day = today.replace(day=31)
day = (today.replace(month=today.month, day=1) - datetime.timedelta(days=1))
datum = day.strftime("%Y%m%d")

# URL souboru VDP
url='http://vdp.cuzk.cz/vymenny_format/soucasna/{}_OB_{}_UKSH.xml.gz'.format(datum, obec)

# otevrit vstupni datasource (RUIAN)
ds = ogr.Open('/vsicurl/' + url)
# nacist vrstvu parcel
layer = ds.GetLayerByName('Parcely')

# vytvorit vystupni datasource (Shapefile - parcely)
driver = ogr.GetDriverByName("ESRI Shapefile")
dso = driver.CreateDataSource("parcely.shp")
srs = osr.SpatialReference()
srs.ImportFromEPSG(5514)
olayer = dso.CreateLayer("parcely", srs, ogr.wkbPolygon)

# definovat atributovou tabulku vystupniho Shapefile
field_name = ogr.FieldDefn("cislo", ogr.OFTString)
field_name.SetWidth(255)
olayer.CreateField(field_name)
olayer.CreateField(ogr.FieldDefn("vymera", ogr.OFTReal))
olayer.CreateField(ogr.FieldDefn("rozdil", ogr.OFTReal))

# pocet parcel
count = layer.GetFeatureCount()

# pocet parcel nad toleranci
count_dif = 0

# sekvencne cist parcely
layer.ResetReading()
while True:
	feat = layer.GetNextFeature()
	if feat is None:
		break
		
	# nacist zajmove atributy
	kc = feat.GetField('KmenoveCislo')
	pod = feat.GetField('PododdeleniCisla')
	vym = feat.GetField('VymeraParcely')
	
	# prvek ma vice geometrickych reprezentaci, zajima nas hranice parcel
	geom = feat.GetGeomFieldRef('OriginalniHranice')
	
	# na zakladne geometrie spocitat vymeru
	vym2 = geom.GetArea()
	
	# vypocitat rozdil mezi vymerou z atributove tabulky a geometrie
	dif = abs(vym - vym2)
	
	# oznaceni parcely
	pc = str(kc)
	if pod:
		pc += '/' + str(pod)
	
	# vytisknout report pro kazdou parcelu
	print ('{0}: {1} {2:.1f} {3:.1f}'.format(pc, vym, vym2, dif))
	
	if dif < tol:
		continue
	
	# parcely, u kterych je rozdil vymer vetsi nez 100m2, ulozime
	# do vystupniho shapefile
	ofeature = ogr.Feature(olayer.GetLayerDefn())
	ofeature.SetField("cislo", pc)
	ofeature.SetField("vymera", vym)
	ofeature.SetField("rozdil", dif)
	ofeature.SetGeometry(geom)
	olayer.CreateFeature(ofeature)
	
	count_dif += 1
	
	# dealokovat pamet
	ofeature = None
	
# vytisknout zaverecnou statistiku
print ('-' * 80)
print ('Pocet parcel: {}'.format(count))
print ('Pocet parcel nad toleranci: {}'.format(count_dif))

# zavrit datove zdroje
ds.Destroy()
dso.Destroy()
