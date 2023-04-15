#!/bin/bash

python mip_query.py | egrep "ternary.*'camion': True, 'series-parallel': 2" | egrep -v "'timeSP': None" | egrep -v "'timeNoSP': None" | cut -d ' ' -f1
