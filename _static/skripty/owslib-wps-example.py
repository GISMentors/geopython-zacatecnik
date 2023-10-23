import csv
from owslib.wps import WebProcessingService, monitorExecution

wps = WebProcessingService('https://rain1.fsv.cvut.cz/services/wps')
wps.getcapabilities()
print(wps.identification.type)

for process in wps.processes:
    print(process.identifier, process.title)

processId = 'd-rain6h-timedist'

from owslib.wps import ComplexDataInput
inputs = [
    ("input", ComplexDataInput('https://rain.fsv.cvut.cz/geodata/test.gml')),
    ("keycolumn", "HLGP_ID"),
    ("return_period", "N2"),
    ("return_period", "N5"),
    ("return_period", "N10"),
    ("type", "E"),
    ("type", "F")  
]

execution = wps.execute(processId, inputs)
monitorExecution(execution)
outputFile = '/tmp/output.csv'
execution.getOutput(outputFile)

with open(outputFile) as fd:
    reader = csv.reader(fd)
    for line in reader:
        print(line)
