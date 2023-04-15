#!/bin/bash

echo "Binary reduce:"
for FILE in random_perturbed/binary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average reduce time:" | cut -d: -f2-
done

echo "Binary wheel:"
for FILE in random_perturbed/binary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average wheel time:" | cut -d: -f2-
done

echo "Ternary reduce:"
for FILE in random_perturbed/ternary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average reduce time:" | cut -d: -f2-
done

echo "Ternary wheel:"
for FILE in random_perturbed/ternary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average wheel time:" | cut -d: -f2-
done

echo "Ternary N_2:"
for FILE in random_perturbed/ternary-*; do
  python eval_log_series_parallel.py $FILE | grep "Average ternary time:" | cut -d: -f2-
done
