json = """
[
    "1.2-with-color.las",
    {
        "type": "filters.sort",
        "dimension": "X"
    }
]
"""

import pdal
pipeline = pdal.Pipeline(json)
count = pipeline.execute()
arrays = pipeline.arrays
metadata = pipeline.metadata
log = pipeline.log
