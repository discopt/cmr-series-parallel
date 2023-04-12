#!/bin/bash

python mip-1-download-miplib.py
python mip-2-extract-matrices.py mip-instances/* >& mip-2-extract-matrices.log 
python mip-3-series-parallel.py >& mip3-series-parallel.log
python mip-4-camion.py >& mip-4-camion.log
python mip-5-tu.py >& mip-5-tu.log

