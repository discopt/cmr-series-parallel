#!/bin/bash

echo "Binary reductions:"
for FILE in random_perturbed/binary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average number of reductions:" | cut -d: -f2-
done

echo "Ternary reductions:"
for FILE in random_perturbed/ternary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average number of reductions:" | cut -d: -f2-
done
