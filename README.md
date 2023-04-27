# Recognizing Series-Parallel Matrices in Linear Time

[comment]: <> (This archive is distributed in association with the ...)
This archive is supposed to be distributed in association with the [INFORMS Journal on Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper [Recognizing Series-Parallel Matrices in Linear Time](https://doi.org/TODO) by M. Walter.
The snapshot is based on 
[this SHA](https://github.com/discopt/cmr/commit/ed04fa20d938001c6594cf13e918237e2bd7c971)
in the development repository.
Users are advised to use [CMR](https://github.com/discopt/cmr), which might contain improvements and fixes compared to this repository.
More information about the software library itself can be found on its [documentation page](https://discopt.github.io/cmr/). 

The code in this repository presents an implementation of a certfying recognition algorithm for series-parallel matrices.
It can determine in linear time (in the number of nonzeros of the matrix) a sequence of series-parallel reductions that either leads to a 1-by-1 matrix or a so-called wheel submatrix.
The latter constitutes a certificate that the matrix is not series-parallel.
The details are described in the paper (to be published).

## Usage

### Compilation

The `src/cmr` subdirectory contains the subset of the [CMR](https://discopt.github.io/cmr/) library that is necessary to compile and run the experiments.
The following steps build the executables from the snapshot but work similarly for the complete library:

```
mkdir build
cd build
cmake ../src/cmr/ -DGUROBI_DIR=<GUROBI-INSTALLATION-DIR> -DCMAKE_BUILD_TYPE=Release
make
```

### Matrices from mixed-integer optimization

1. The following command downloads the MIPLIB 2017 benchmark instance set into the directory `mip-instances`.
   ```
   python mip-1-download-miplib.py
   ```

1. We now extract a large ternary submatrix of each coefficient matrix:
   ```
   python mip-2-extract-matrices.py mip-instances/* >& mip-2-extract-matrices.log
   ```

1. The following script tests these matrices for being series-parallel and stores an SP-reduced submatrix.
   ```
   python mip_03_series_parallel.py
   ```

1. The next script tests whether these matrices are Camion-signed, which is one step for testing them for total unimodularity.
   ```
   python mip_04_camion.py
   ```

1. Now we test whether these matrices are totally unimodular, once with and once without application of series-parallel reductions.
   ```
   python mip_05_tu.py
   ```

1. The following evaluation scripts query the produced log files for being trivial (-1/0/+1 submatrix is empty), for timeouts and exceeded memory limits, for not being Camion-signed, and for (not) being series-parallel. They output all the relevant information for the respective instance lists from the paper. The data for the tables is produced by the last two scripts.
   ```
   mip_06_query_trivial.shython mip_05_tu.py
   mip_07_query_timeouts.sh
   mip_08_query_memory.sh
   mip_09_query_noncamion.sh
   mip_10_query_series_parallel.sh
   mip_11_query_non_series_parallel.sh
   mip_table1.sh
   mip_table2.sh
   ```

### Randomly generated matrices

1. The following script generates the four families of random matrices discussed in the paper:
   ```
   random_all.sh
   ```
   It does so by executing `random_1_series_parallel.py`, `random_2_perturbed.py`, `random_3_vary_base.py`, `random_4_big_base.py`.
   Each of these will creates a corresponding directory. Since file size of some of the instances exceeds a gigabyte, these files are removed immediately after running the experiments. Only the log files remain.

1. The following scripts evaluate the generated log files and produce the LaTeX code for the corresponding figures:
   ```
   random_figure4a.sh
   random_figure4b.sh
   random_figure5a.sh
   random_figure5b.sh
   random_figure6a.sh
   random_figure6b.sh
   random_figure7a.sh
   random_figure7b.sh
   ```

## License

This software is released under the MIT license, which we report in file `LICENSE`.

