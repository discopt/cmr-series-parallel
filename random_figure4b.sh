#!/bin/bash

echo "Binary:"
for FILE in `ls random_series_parallel/binary-*-0.00-*.sp | tac`; do
  python eval_log_series_parallel.py $FILE | grep "Average time per nonzero:" | cut -d: -f2-
done

echo "Ternary:"
for FILE in `ls random_series_parallel/ternary-*-0.00-*.sp | tac`; do
  python eval_log_series_parallel.py $FILE | grep "Average time per nonzero:" | cut -d: -f2-
done

echo "Graphic:"
for FILE in `ls random_series_parallel/binary-*-0.00-*.gra | tac`; do
  python eval_log_graphic.py $FILE | grep "Average time per nonzero:" | cut -d: -f2-
done

