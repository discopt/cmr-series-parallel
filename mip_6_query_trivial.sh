#!/bin/bash

python mip_query.py | egrep "ternary.*'trivial': True" | cut -d ' ' -f1
