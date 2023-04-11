import os
import sys
from data_mip import *

CMR_BUILD = '../master.git/build-release'
CMR_CAMION = CMR_BUILD + '/cmr-camion'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'

def run(instance, kary):
    data = getData(instance, kary)
    if not data['trivial']:
        print(f'Checking {kary} version of {instance} for Camion')
        os.system(f'gzip -cd mip-matrices/{instance}.{kary}.sparse.gz | {CMR_CAMION} -i sparse - -s 2> mip-matrices/{instance}.{kary}.camion')
    else:
        print(f'Skipping {kary} version of {instance}')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for kary in ['binary', 'ternary']:
            for instance in getInstances():
                run(instance, kary)
    else:
        for kary in ['binary', 'ternary']:
            for instance in sys.argv[1:]:
                run(instance, kary)

