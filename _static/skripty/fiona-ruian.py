import datetime
import fiona
from shapely.geometry import shape

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
url='http://vdp.cuzk.cz/vymenny_format/soucasna/{}_OB_{}_UKSH.xml.zip'.format(datum, obec)

count_dif = 0

with fiona.open('/vsizip/vsicurl/' + url, layer='Parcely') as ds:
    schema = {
            "geometry": "Polygon",
            "properties": {
                "cislo":  "str:25",
                "vymera": "float",
                "rozdil": "float"
                }
            }
    with fiona.open("parcely.shp", 'w', driver="ESRI Shapefile", crs="epsg:5514", schema=schema) as dso:
        for f in ds:
            cislo = f["properties"]["KmenoveCislo"]
            if f["properties"]["PododdeleniCisla"]:
                cislo  = "{}/{}".format(cislo, f["properties"]["PododdeleniCisla"])

            vym = float(f["properties"]["VymeraParcely"])
            vym2 = shape(f["geometry"]).area
            dif = abs(vym - vym2)

            if dif < tol:
                continue

            dso.write({
                "type": "Feature",
                "properties": {
                    "cislo": cislo,
                    "vymera": f["properties"]["VymeraParcely"],
                    "rozdil": vym - vym2
                }
            })

            count_dif += 1

        print("-"*80)
        print("Počet parcel: {}".format(len(dso)))
        print("Počet parcel nad tolerancí: {}".format(count_dif))

