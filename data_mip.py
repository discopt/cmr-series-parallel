import sys
import os
import gzip

DIR='mip-matrices'

def getInstances():
    return [ fileName[:-len('.original.header')] for fileName in os.listdir(DIR) if fileName[-len('.original.header'):] == '.original.header' ]

def getOriginalData(instance):
    firstLine = open(f'{DIR}/{instance}.original.header', 'r').read().split('\n', 1)[0]
    data = list(map(int, firstLine.split()))
    return { 'original rows': data[0], 'original columns': data[1], 'original nonzeros': data[2] }

def getData(instance, kary):
    try:
        firstLine = gzip.open(f'{DIR}/{instance}.{kary}.sparse.gz', 'r').read().decode('utf-8').split('\n', 1)[0]
        data = list(map(int, firstLine.split()))
        isTrivial = (data[0] * data[1] * data[2] == 0)
        isCamion = None
        seriesParallel = -1
        reducedRows = None
        reducedColumns = None
        reducedNonzeros = None
        isTU = None
        timeSP = None
        timeNoSP = None
        if not isTrivial:
            try:
                for line in open(f'{DIR}/{instance}.{kary}.camion', 'r').read().split('\n'):
                    if line == 'Matrix IS Camion-signed.':
                        isCamion = True
                    elif line == 'Matrix IS NOT Camion-signed.':
                        isCamion = False
            except:
                sys.stderr.write(f'WARNING: File {DIR}/{instance}.{kary}.camion is not present.\n')
            try:
                firstLine = gzip.open(f'{DIR}/{instance}.{kary}.reduced.sparse.gz', 'r').read().decode('utf-8').split('\n', 1)[0]
                spData = list(map(int, firstLine.split()))
                if spData[0] == data[0] and spData[1] == data[1]:
                    seriesParallel = 0
                    reducedRows = data[0]
                    reducedColumns = data[1]
                    reducedNonzeros = data[2]
                elif spData[0] == 0 and spData[1] == 0:
                    seriesParallel = 2
                    reducedRows = 0
                    reducedColumns = 0
                    reducedNonzeros = 0
                else:
                    seriesParallel = 1
                    reducedRows = spData[0]
                    reducedColumns = spData[1]
                    reducedNonzeros = spData[2]

            except:
                sys.stderr.write(f'WARNING: File {DIR}/{instance}.{kary}.reduced.sparse.gz is not present.\n')
            if isCamion and seriesParallel != 2:
                try:
                    for line in open(f'{DIR}/{instance}.{kary}.sp.tu', 'r').read().split('\n'):
                        if line == 'Matrix IS regular.':
                            isTU = True
                        elif line == 'Matrix IS NOT regular.':
                            isTU = False
                        elif line[:8] == '  total:':
                            timeSP = float(line.split()[3])
                except:
                    sys.stderr.write(f'WARNING: File {DIR}/{instance}.{kary}.sp.tu is not present.\n')
                try:
                    for line in open(f'{DIR}/{instance}.{kary}.no-sp.tu', 'r').read().split('\n'):
                        if line[:8] == '  total:':
                            timeNoSP = float(line.split()[3])
                except:
                    sys.stderr.write(f'WARNING: File {DIR}/{instance}.{kary}.no-sp.tu is not present.\n')
        return { 'rows': data[0], 'columns': data[1], 'nonzeros': data[2], 'trivial': isTrivial, 'camion': isCamion, 'series-parallel': seriesParallel, 'tu': isTU, 'timeSP': timeSP, 'timeNoSP': timeNoSP, 'SP-reduced rows': reducedRows, 'SP-reduced columns': reducedColumns, 'SP-reduced nonzeros': reducedNonzeros }
    except:
        data = [None, None, None]
        return None

def printTex(instance, kary, data):
    instance = instance.replace('_', '\\_')
    if data['SP-reduced nonzeros'] == 0:
        return f"\\texttt{{{instance}}} & \\num{{{data['rows']}}} & \\num{{{data['columns']}}} & \\num{{{data['nonzeros']}}} & \\SI{{{data['timeNoSP']}}}{{\\s}} & \\SI{{{data['timeSP']}}}{{\\s}} \\\\"
    else:
        return f"\\texttt{{{instance}}} & \\num{{{data['rows']}}} & \\num{{{data['columns']}}} & \\num{{{data['nonzeros']}}} & \\num{{{data['SP-reduced rows']}}} & \\num{{{data['SP-reduced columns']}}} & \\num{{{data['SP-reduced nonzeros']}}} & \\SI{{{data['timeNoSP']}}}{{\\s}} & \\SI{{{data['timeSP']}}}{{\\s}} \\\\"

def dump(instance, tex):
    data = getOriginalData(instance)
    data['binary'] = getData(instance, 'binary')
    data['ternary'] = getData(instance, 'ternary')
    print(f"{instance} is {data['original rows']}x{data['original columns']} with {data['original nonzeros']} nonzeros")
    s = ' #' + printTex(instance, 'binary', data['binary']) if tex else ''
    print(f'{instance} binary:  ' + str(data['binary']) + s)
    s = ' #' + printTex(instance, 'ternary', data['ternary']) if tex else ''
    print(f'{instance} ternary: ' + str(data['ternary']) + s)

if __name__ == '__main__':
    args = sys.argv[1:]
    tex = False
    if args and args[0] == '--tex':
        tex = True
        args = args[1:]
    if args:
        for instance in args:
            dump(instance, tex)
    else:
        for instance in getInstances():
            dump(instance, tex)

