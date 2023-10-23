#!/usr/bin/env python3

from owslib.wps import WebProcessingService
from owslib.wps import ComplexDataInput

# 1. test GetCapabilities query
wps = WebProcessingService('https://rain1.fsv.cvut.cz/services/wps', skip_caps=True)
wps.getcapabilities()
print ("Test 1: GetCapabilities -> list of processes:")
for process in wps.processes:
    print (process.identifier)

processId = 'd-rain-csv'

# 2. test DescribeProcess query
#process = wps.describeprocess(processId)
#print ("Test 2: DescribeProcess -> list of parameters:")
# for input in process.dataInputs:
#     print (input.identifier)
# for output in process.processOutputs:
#     print (output.identifier)

# 3. test Execute query
print ("Test 3: Execute")
inputs = [
    ("input", ComplexDataInput('https://rain.fsv.cvut.cz/geodata/test.gml')),
    ("keycolumn", "HLGP_ID"),
    ("return_period", "N2,N5,N10"),
    ("rainlength", "120")
]
execution = wps.execute(processId, inputs)
outputFile = '/tmp/output.csv'
execution.getOutput(outputFile)
with open(outputFile) as fd:
    print (fd.readlines())
o
