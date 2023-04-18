import subprocess
import sys
import os

DIR='random_vary_base'

try:
  os.mkdir(DIR)
except:
  pass

CMR_BUILD = './build'
CMR_GENERATE_SERIES_PARALLEL = CMR_BUILD + '/cmr-generate-series-parallel'
CMR_PERTURB = CMR_BUILD + '/cmr-perturb-random'
CMR_SERIES_PARALLEL = CMR_BUILD + '/cmr-series-parallel'

N = 10000
#N = 1000 # for debugging
repetitions = 100
#repetitions = 2 # for debugging

for kary in ['binary', 'ternary']:
    for alpha in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        PROBABILITY = 0.5
        BASE = max(1, int(alpha*N))
        beta = 0.5*(1-alpha)
        UNIT = int(beta*N)
        gamma = 0.5*(1-alpha)
        COPY = N - BASE - UNIT
        assert COPY >= 0
        delta = 0.0
        makeTernary = '-t' if kary == 'ternary' else ''
        testBinary = '-b' if kary == 'binary' else ''
        PREFIX=f'{DIR}/{kary}-{N}-{alpha:.2f}-{beta:.2f}-{gamma:.2f}-{delta:.2f}-{PROBABILITY}'
        open(f'{PREFIX}.sp', 'w').close()
        for i in range(repetitions):
            subprocess.call(f'{CMR_GENERATE_SERIES_PARALLEL} {BASE} {BASE} -p {PROBABILITY} -u {UNIT} {UNIT} -c {COPY} {COPY} {makeTernary} > {PREFIX}-{i}.sparse', shell=True)
            subprocess.call(f'{CMR_SERIES_PARALLEL} -i sparse {PREFIX}-{i}.sparse {testBinary} -R {PREFIX}-{i}.reduced -N - -s >> {PREFIX}.sp', shell=True)
            os.unlink(f'{PREFIX}-{i}.reduced')
            os.unlink(f'{PREFIX}-{i}.sparse')

