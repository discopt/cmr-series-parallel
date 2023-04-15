#!/bin/bash

python mip_query.py | egrep "ternary.*'camion': True, 'series-parallel': 1, 'tu': None" | cut -d ' ' -f1
