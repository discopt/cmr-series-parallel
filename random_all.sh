#!/bin/bash

date
echo "series-parallel"
python random_1_series_parallel.py
date
echo "perturbed series-parallel"
python random_2_perturbed.py
date
echo "varying base size"
python random_3_vary_base.py
date
echo "big base"
python random_4_big_base.py
date
