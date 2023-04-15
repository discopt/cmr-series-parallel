import sys
import re

reMatrix = re.compile('Read ([0-9]*)x([0-9]*) matrix with ([0-9]*) nonzeros in .* seconds.')
reOutcome = re.compile('Matrix (.*) series-parallel. ([0-9]*) reductions can be applied.')
reReduce = re.compile(' *reduction calls: ([0-9]*) in ([0-9.]*) seconds')
reWheel = re.compile(' *wheel searches: ([0-9]*) in ([0-9.]*) seconds')
reTernary = re.compile(' *ternary certificates: ([0-9]*) in ([0-9.]*) seconds')
reTotal = re.compile(' *total: ([0-9]*) in ([0-9.]*) seconds')
reSubmatrix = re.compile('Writing minimal non-series-parallel submatrix of order ([0-9]*) to stdout.')

numParsed = 0
sums = {}
orderSubmatrix = float('inf')
parsed = False
def collect():
    global orderSubmatrix
    global numParsed
    global numNonzeros
    global numReductions
    global timeReduce
    global timeWheel
    global timeTernary
    global timeTotal
    sums['numNonzeros'] = sums.get('numNonzeros', 0) + numNonzeros
    sums['numReductions'] = sums.get('numReductions', 0) + numReductions
    sums['timeReduce'] = sums.get('timeReduce', 0) + timeReduce
    sums['timeWheel'] = sums.get('timeWheel', 0) + timeWheel
    sums['timeTernary'] = sums.get('timeTernary', 0) + timeTernary
    sums['timePerNonzero'] = sums.get('timePerNonzero', 0) + timeTotal / numNonzeros if numNonzeros > 0 else float('inf')
    sums['timeTotal'] = sums.get('timeTotal', 0) + timeTotal
    sums['orderSubmatrix'] = sums.get('orderSubmatrix', 0) + orderSubmatrix
    orderSubmatrix = float('inf')
    numParsed += 1


for line in open(sys.argv[1], 'r').read().split('\n'):
  if not line:
    continue
  if line.startswith('Writing reduced submatrix to '):
    parsed = True
    continue
  if line == 'Series-parallel recognition:' or line == 'Writing minimal non-series-parallel submatrix to stdout.':
    continue
  result = reMatrix.match(line)
  if result:
    if parsed:
        collect()
        parsed = False
    numRows = int(result.group(1))
    numColumns = int(result.group(2))
    numNonzeros = int(result.group(3))
    continue
  result = reOutcome.match(line)
  if result:
    isSP = result.group(1) == 'IS'
    numReductions = int(result.group(2))
    continue
  result = reReduce.match(line)
  if result:
    timeReduce = float(result.group(2))
    continue
  result = reWheel.match(line)
  if result:
    timeWheel = float(result.group(2))
    continue
  result = reTernary.match(line)
  if result:
    timeTernary = float(result.group(2))
    continue
  result = reTotal.match(line)
  if result:
    timeTotal = float(result.group(2))
    continue
  result = reSubmatrix.match(line)
  if result:
    orderSubmatrix = int(result.group(1))
    continue
  sys.stderr.write(f'Unparsed line <{line}>.\n')
  sys.stderr.flush()

if parsed:
    collect()

if numParsed > 0:
  print(f"Average number of nonzeros: {sums['numNonzeros'] / numParsed}")
  print(f"Average number of reductions: {sums['numReductions'] / numParsed}")
  print(f"Average reduce time: {sums['timeReduce'] / numParsed:.3f}")
  print(f"Average wheel time: {sums['timeWheel'] / numParsed:.3f}")
  print(f"Average ternary time: {sums['timeTernary'] / numParsed:.3f}")
  print(f"Average total time: {sums['timeTotal'] / numParsed:.3f}")
  print(f"Average time per nonzero: {sums['timePerNonzero'] / numParsed * 1000000000:.3f}")
  print(f"Average order of submatrices: {sums['orderSubmatrix'] / numParsed:.3f}")

