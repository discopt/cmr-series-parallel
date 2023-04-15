#!/bin/bash

python mip_query.py | egrep "ternary.*'tu': (True|False).*None" | cut -d ' ' -f1
