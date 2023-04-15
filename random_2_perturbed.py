import subprocess
import sys
import os

DIR='random_perturbed'

try:
  os.mkdir(DIR)
except:
  pass

CMR_BUILD = './build'
CMR_GENERATE_SERIES_PARALLEL = CMR_BUILD + '/cmr-generate-series-parallel'
CMR_PERTURB = CMR_BUILD + '/cmr-perturb-random'
CMR_SERIES_PARALLEL = CMR_BUILD + '/cmr-series-parallel'

N = 10000
#N = 2000 # for debugging
repetitions = 1000
#repetitions = 10 # for debugging

for kary in ['binary', 'ternary']:
    for delta in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
        alpha = 0.0
        beta = 0.5
        gamma = 1.0 - alpha- beta
        PROBABILITY = 1
        BASE = max(1, int(alpha*N))
        UNIT = min(N - BASE, int(beta*N))
        COPY = N - BASE - UNIT
        assert COPY >= 0
        PERTURBED = int(delta*N)
        makeTernary = '-t' if kary == 'ternary' else ''
        testBinary = '-b' if kary == 'binary' else ''
        perturbKary = '-t' if kary == 'ternary' else '-b'
        PREFIX=f'{DIR}/{kary}-{N}-{alpha:.2f}-{beta:.2f}-{gamma:.2f}-{delta:.2f}-{PROBABILITY}'
        open(f'{PREFIX}.sp', 'w').close()
        for i in range(repetitions):
            subprocess.call(f'{CMR_GENERATE_SERIES_PARALLEL} {BASE} {BASE} -p {PROBABILITY} -u {UNIT} {UNIT} -c {COPY} {COPY} {makeTernary} > {PREFIX}-{i}.sparse', shell=True)
            subprocess.call(f'{CMR_PERTURB} -i sparse {perturbKary} {PERTURBED} {PREFIX}-{i}.sparse {PREFIX}-{i}-pert.sparse', shell=True)
            subprocess.call(f'{CMR_SERIES_PARALLEL} -i sparse {PREFIX}-{i}-pert.sparse {testBinary} -R {PREFIX}-{i}-pert.reduced -N - -s 2>> {PREFIX}.sp', shell=True)
            os.unlink(f'{PREFIX}-{i}-pert.reduced')
            os.unlink(f'{PREFIX}-{i}.sparse')
            os.unlink(f'{PREFIX}-{i}-pert.sparse')

