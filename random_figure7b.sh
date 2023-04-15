#!/bin/bash

echo "Binary time per nonzero:"
for FILE in random_big_base/binary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average time per nonzero:" | cut -d: -f2-
done

echo "Ternary time per nonzero:"
for FILE in random_big_base/ternary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average time per nonzero:" | cut -d: -f2-
done

