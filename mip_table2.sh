#!/bin/bash

python mip_query.py --tex | egrep "ternary.*'camion': True, 'series-parallel': [01]" | egrep -v "'timeSP': None" | egrep -v "'timeNoSP': None" | cut -d '#' -f2-
