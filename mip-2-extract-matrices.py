import sys
import os

try:
  os.mkdir('mip-matrices')
except:
  pass

CMR_BUILD = './build/'
CMR_EXTRACT_GUROBI = CMR_BUILD + '/cmr-extract-gurobi'
CMR_K_ARY = CMR_BUILD + '/cmr-k-ary'
CMR_MATRIX = CMR_BUILD + '/cmr-matrix'

for mip in sys.argv[1:]:
  if mip[-7:] == '.mps.gz':
    base = mip[:-7]
  else:
    base = mip
  base = os.path.basename(base)
  os.system( f'{CMR_EXTRACT_GUROBI} {mip} -o sparse > {base}.sparse' )
  os.system( f'head -n 1 {base}.sparse > mip-matrices/{base}.original.header' )
  os.system( f'{CMR_K_ARY} {base}.sparse -R {base}.submat -i sparse -t' )
  os.system( f'{CMR_MATRIX} {base}.sparse -S {base}.submat -i sparse -d - | gzip > mip-matrices/{base}.ternary.sparse.gz' )
  os.system( f'{CMR_K_ARY} {base}.sparse -R {base}.submat -i sparse -b' )
  os.system( f'{CMR_MATRIX} {base}.sparse -S {base}.submat -i sparse -d - | gzip > mip-matrices/{base}.binary.sparse.gz' )
  os.unlink( f'{base}.sparse')
  os.unlink( f'{base}.submat')

