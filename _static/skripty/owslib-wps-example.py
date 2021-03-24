from owslib.wps import WebProcessingService

wps = WebProcessingService('https://rain1.fsv.cvut.cz/services/wps')

wps.getcapabilities()
print(wps.identification.type)

for process in wps.processes:
    print (process.identifier, process.title)

inputs = [ ('input', '@xlink:href=http://rain.fsv.cvut.cz/geodata/test.gml'),
           ('return_period', 'N2,N5,N10'),
           ('rainlength', '120')
]
execution = wps.execute('d-rain-shp', inputs, output = "output")    
from owslib.wps import monitorExecution
monitorExecution(execution)
