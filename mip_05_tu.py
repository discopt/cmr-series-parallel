import os
import sys
import subprocess
from mip_query import *

CMR_BUILD = './build'
CMR_REGULAR = CMR_BUILD + '/cmr-regular'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'
TIME_LIMIT = 3600

instances = sys.argv[1:]
if not instances:
    instances = getInstances()

for kary in ['binary', 'ternary']:
    for instance in instances:
        data = getData(instance, kary)
        if data and not data['trivial'] and data['camion']:
            if data['tu'] is None:
                print(f'Checking {kary} version of {instance} for regularity')
                subprocess.call(f'gzip -cd mip_matrices/{instance}.{kary}.sparse.gz | {CMR_MATRIX} -i sparse - - -c | {CMR_REGULAR} --time-limit {TIME_LIMIT} -i sparse - -s --no-direct-graphic 2> mip_matrices/{instance}.{kary}.sp.tu', shell=True)
                subprocess.call(f'gzip -cd mip_matrices/{instance}.{kary}.sparse.gz | {CMR_MATRIX} -i sparse - - -c | {CMR_REGULAR} --time-limit {TIME_LIMIT} -i sparse - -s --no-direct-graphic --no-series-parallel 2> mip_matrices/{instance}.{kary}.no-sp.tu', shell=True)
            else:
                print(f'Skipping {kary} version of {instance} because it was already computed.')
        else:
            print(f'Skipping {kary} version of {instance} because it is trivial or not camion-signed.')

