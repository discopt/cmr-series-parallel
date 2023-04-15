#!/bin/bash

echo "Downloading MIPLIB instances..."
python mip_1_download_miplib.py

echo "Extracting matrices..."
python mip_2_extract_matrices.py mip_instances/* >& mip_2_extract_matrices.log 
echo "Testing for SP..."
python mip_3_series_parallel.py >& mip_3_series_parallel.log
echo "Testing for Camion..."
python mip_4_camion.py >& mip_4_camion.log
echo "Testing for TU..."
python mip_5_tu.py >& mip_5_tu.log

