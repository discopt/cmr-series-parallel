find_path(GUROBI_INCLUDE_DIRS
    NAMES gurobi_c.h
    HINTS ${GUROBI_DIR} $ENV{GUROBI_DIR}
    PATH_SUFFIXES linux64/include include)

find_library( GUROBI_CXX_LIBRARY
              NAMES gurobi_c++ gurobi_stdc++
              HINTS ${GUROBI_DIR} $ENV{GUROBI_DIR}
              PATH_SUFFIXES linux64/lib lib)

find_library(GUROBI_LIBRARY
    NAMES gurobi gurobi70 gurobi75 gurobi80 gurobi81 gurobi90 gurobi95 gurobi100
    HINTS ${GUROBI_DIR} $ENV{GUROBI_DIR}
    PATH_SUFFIXES linux64/lib lib)

set(GUROBI_LIBRARIES ${GUROBI_LIBRARY} ${GUROBI_CXX_LIBRARY} )

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(GUROBI DEFAULT_MSG GUROBI_INCLUDE_DIRS GUROBI_LIBRARIES)
