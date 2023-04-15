import sys
import re

reMatrix = re.compile('Read ([0-9]*)x([0-9]*) matrix with ([0-9]*) nonzeros in .* seconds.')
reOutcome = re.compile('Matrix ([a-zA-Z ]*) graphic.')
reTotal = re.compile(' *total: ([0-9]*) in ([0-9.]*) seconds')


numParsed = 0
sums = {}
parsed = False
def collect():
    global numParsed
    global numNonzeros
    global timeTotal
    sums['numNonzeros'] = sums.get('numNonzeros', 0) + numNonzeros
    sums['timePerNonzero'] = sums.get('timePerNonzero', 0) + timeTotal / numNonzeros if numNonzeros > 0 else float('inf')
    sums['timeTotal'] = sums.get('timeTotal', 0) + timeTotal
    numParsed += 1


for line in open(sys.argv[1], 'r').read().split('\n'):
  if not line or line == 'Graphicness recognition:':
    continue
  result = reMatrix.match(line)
  if result:
    if parsed:
        collect()
        parsed = False
    numRows = int(result.group(1))
    numColumns = int(result.group(2))
    numNonzeros = int(result.group(3))
    parsed = True
    continue
  result = reOutcome.match(line)
  if result:
    isSP = result.group(1) == 'IS'
    continue
  result = reTotal.match(line)
  if result:
    timeTotal = float(result.group(2))
    continue
  if line[:len('  transpositions')] == '  transpositions':
    continue
  if line[:len('  column')] == '  column':
    continue
  sys.stderr.write(f'Unparsed line <{line}>.\n')
  sys.stderr.flush()

if parsed:
    collect()

if numParsed > 0:
  print(f"Average number of nonzeros: {sums['numNonzeros'] / numParsed}")
  print(f"Average total time: {sums['timeTotal'] / numParsed:.3f}")
  print(f"Average time per nonzero: {sums['timePerNonzero'] / numParsed * 1000000000:.3f}")

