import subprocess
import os
import sys
from mip_query import *

CMR_BUILD = './build/'
CMR_SERIES_PARALLEL = CMR_BUILD + '/cmr-series-parallel'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'

instances = sys.argv[1:]
if not instances:
    instances = getInstances()

for kary in ['binary', 'ternary']:
    for instance in instances:
        data = getData(instance, kary)
        if not data['trivial']:
            print(f'Checking {kary} version of {instance} for SP', flush=True)
            subprocess.call(f'gzip -cd mip_matrices/{instance}.{kary}.sparse.gz | {CMR_SERIES_PARALLEL} -i sparse - -R temp-{instance}.submat', shell=True)
            subprocess.call(f'gzip -cd mip_matrices/{instance}.{kary}.sparse.gz | {CMR_MATRIX} - -d -i sparse -S temp-{instance}.submat - | gzip > mip_matrices/{instance}.{kary}.reduced.sparse.gz', shell=True)
            os.unlink(f'temp-{instance}.submat')
        else:
            print(f'Skipping {kary} version of {instance}', flush=True)
