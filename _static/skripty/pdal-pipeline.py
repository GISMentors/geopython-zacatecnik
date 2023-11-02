json = """
[
    "/cesta/soubor.las",
    {
        "type": "filters.sort",
        "dimension": "Z"
    }
]
"""

import pdal
pipeline = pdal.Pipeline(json)
count = pipeline.execute()
arrays = pipeline.arrays
print(arrays)
