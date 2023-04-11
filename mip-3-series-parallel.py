import os
import sys
from data_mip import *

CMR_BUILD = './build/'
CMR_SERIES_PARALLEL = CMR_BUILD + '/cmr-series-parallel'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'

for kary in ['binary', 'ternary']:
    for instance in getInstances():
        data = getData(instance, kary)
        if not data['trivial']:
            print(f'Checking {kary} version of {instance} for SP')
            os.system(f'gzip -cd mip-matrices/{instance}.{kary}.sparse.gz | {CMR_SERIES_PARALLEL} -i sparse - -R temp-{instance}.submat')
            os.system(f'gzip -cd mip-matrices/{instance}.{kary}.sparse.gz | {CMR_MATRIX} - -d -i sparse -S temp-{instance}.submat - | gzip > mip-matrices/{instance}.{kary}.reduced.sparse.gz')
            os.unlink(f'temp-{instance}.submat')
        else:
            print(f'Skipping {kary} version of {instance}')
