import os
import sys
import subprocess
from data_mip import *

CMR_BUILD = './build/'
CMR_CAMION = CMR_BUILD + '/cmr-camion'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'
TIME_LIMIT=3600

instances = sys.argv[1:]
if not instances:
    instances = getInstances()

for kary in ['binary', 'ternary']:
    for instance in instances:
        data = getData(instance, kary)
        if not data['trivial']:
            print(f'Checking {kary} version of {instance} for Camion')
            subprocess.call(f'gzip -cd mip-matrices/{instance}.{kary}.sparse.gz | {CMR_CAMION} --time-limit {TIME_LIMIT} -i sparse - -s 2> mip-matrices/{instance}.{kary}.camion', shell=True)
        else:
            print(f'Skipping {kary} version of {instance}')

