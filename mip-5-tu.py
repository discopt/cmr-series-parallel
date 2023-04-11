import os
import sys
from data_mip import *

CMR_BUILD = '../master.git/build-release'
CMR_REGULAR = CMR_BUILD + '/cmr-regular'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'

def run(instance, kary, force):
    data = getData(instance, kary)
    if data and not data['trivial'] and data['camion']:
        if data['tu'] is None or force:
            print(f'Checking {kary} version of {instance} for regularity')
            os.system(f'gzip -cd mip-matrices/{instance}.{kary}.sparse.gz | {CMR_MATRIX} -i sparse - - -c | {CMR_REGULAR} -i sparse - -s --no-direct-graphic 2> mip-matrices/{instance}.{kary}.sp.tu')
            os.system(f'gzip -cd mip-matrices/{instance}.{kary}.sparse.gz | {CMR_MATRIX} -i sparse - - -c | {CMR_REGULAR} -i sparse - -s --no-direct-graphic --no-series-parallel 2> mip-matrices/{instance}.{kary}.no-sp.tu')
        else:
            print(f'Skipping {kary} version of {instance} because it was already computed.')
    else:
        print(f'Skipping {kary} version of {instance} because it is trivial or not camion-signed.')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for kary in ['ternary']:#, 'ternary']:
            for instance in getInstances():
                run(instance, kary, False)
    else:
        for kary in ['ternary']: #, 'binary']:
            for instance in sys.argv[1:]:
                run(instance, kary, True)

