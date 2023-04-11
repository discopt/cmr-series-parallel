# cmr-series-parallel
Repository for experiments with series-parallel matrix recognition

# Recognizing Series-Parallel Matrices in Linear Time

The software and data in this repository are a snapshot of the software and data used in the paper Recognizing Series-Parallel Matrices in Linear Time by M. walter.
Users are advised to use [CMR](https://github.com/discopt/cmr), which might contain improvements and fixes compared to this repository.

The code in this repository presents an implementation of a certfying recognition algorithm for series-parallel matrices.
It can determine in linear time (in the number of nonzeros of the matrix) a sequence of series-parallel reductions that either leads to a 1-by-1 matrix or a so-called wheel submatrix.
The latter constitutes a certificate that the matrix is not series-parallel.
The details are described in the paper (to be published).

## Usage

### Installation of CMR

The `cmr` subdirectory contains the subset of the [CMR](https://discopt.github.io/cmr/) library that is necessary to compile and run the experiments.
The following steps build the executables from the snapshot but work similarly for the complete library:

$ cd cmr/
$ mkdir build
$ cd build
$ cmake .. -DGUROBI_DIR=<GUROBI-INSTALLATION-DIR> -DCMAKE_BUILD_TYPE=Release
$ make

### Matrices from mixd-integer optimization

$ cd miplib
$ ./download.sh
$ ./extract.sh
$ for FILE in *.mps.gz; do ../cmr/build/cmr-extract-gurobi ${FILE} -o sparse > 


## Instances

Instances contained in folder `data` are part of the so-called "Uchoa dataset".
We refer to the following paper for further information on their generation and characteristics:

```bib
@article{uchoa_2017,
    title={New benchmark instances for the capacitated vehicle routing problem},
    author={Uchoa, Eduardo and Pecin, Diego and Pessoa, Artur and Poggi, Marcus and Vidal, Thibaut and Subramanian, Anand},
    year=2017,
    journal={European Journal of Operational Research},
    volume=257,
    number=3,
    pages={845--858},
    doi={10.1016/j.ejor.2016.08.012}
}
```

## Results

Folder `results` contains the figures used in the paper.

## Acknowledgements

We are extremely grateful to Stefan Ropke for sharing with us his code for ALNS applied to the CVRP.

## License

This software is released under the MIT license, which we report in file `LICENSE`.

