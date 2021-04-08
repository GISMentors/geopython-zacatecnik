from owslib.wps import WebProcessingService

wps = WebProcessingService('https://rain1.fsv.cvut.cz/services/wps')
wps.getcapabilities()
print(wps.identification.type)

for process in wps.processes:
    print(process.identifier, process.title)

processId = 'd-rain-csv'

from owslib.wps import ComplexDataInput
inputs = [
    ("input", ComplexDataInput('http://rain.fsv.cvut.cz/geodata/test.gml')),
    ("keycolumn", "HLGP_ID"),
    ("return_period", "N2,N5,N10"),
    ("rainlength", "120")
]

execution = wps.execute(processId, inputs)
outputFile = '/tmp/output.csv'
execution.getOutput(outputFile)

with open(outputFile) as fd:
    print(fd.readlines())
