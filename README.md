# Recognizing Series-Parallel Matrices in Linear Time

This archive is distributed in association with the [INFORMS Journal on Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper [Recognizing Series-Parallel Matrices in Linear Time](https://doi.org/TODO) by M. Walter.
The snapshot is based on 
[this SHA](https://github.com/discopt/cmr/commit/935c627918fc6793a16ef2e44308547e248b8381)
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
$ mkdir build
$ cd build
$ cmake ../src/cmr/ -DGUROBI_DIR=<GUROBI-INSTALLATION-DIR> -DCMAKE_BUILD_TYPE=Release
$ make
```

### Matrices from mixed-integer optimization

1. The following command downloads the MIPLIB 2017 benchmark instance set into the directory `mip-instances`.
   ```
   % python mip-1-download-miplib.py
   ```

2. We now extract a large ternary submatrix of each coefficient matrix:
   ```
% python mip-2-extract-matrices.py mip-instances/* >& mip-2-extract-matrices.log
   ```

## License

This software is released under the MIT license, which we report in file `LICENSE`.

