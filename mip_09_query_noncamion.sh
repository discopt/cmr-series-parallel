#!/bin/bash

python mip_query.py | egrep "ternary.*'camion': False" | cut -d ' ' -f1
