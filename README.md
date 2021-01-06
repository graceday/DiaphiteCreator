# Diaphite Generator

This is a program to generate Diaphite Type 2 based on the DIFFaX model developed by Christoph Salzmann.
These can be visualised using a program of your choice (e.g. VMD) or used as starting points for simulations.

## REQUIREMENTS
* `python3.5` or above to support type hints
* `argparse`
* `numpy`

## USAGE
The main file is `diaphite_generator.py`. It takes the following arguments:

* `--out_file`, the name of a file to output to. This should autodetect the suffix and output in the appropriate format. Currently supports .xyz, .cif and .data (a LAMMPS data file)
* `--seq_file`, the name of a file containing a layer sequence, detailed below.
* `--seq`, a manually specified 

### LAYER SEQUENCE
Diaphite type 2 is made up of alternating layers of graphene and diamond.
The sequence file contains data about this alternation in the form of a list of integers 1,2,3,4.
The integers represent the following types:
* `1` represents a Diamond layer
* `2` represents a diamond/graphene interface layer
* `3` represents a graphene layer
* `4` represents a graphene/diamond interface layer

There are some rules about this ordering, and remember that periodic boundary conditions means that the last item is followed by the first item.
The rules are that diamond layers (`1`) can only be followed by other diamond layers (`1`) or diamond/graphene interfaces (`2`). Diamond/graphene interfaces can only be followed by graphene (`3`). Graphene layers (`3`) can only be followed by other graphene layers (`3`) or graphene/diamond interfaces (`4`). Finally, graphene/diamond interfaces can only be followed by diamond (`4`).
The program should verify the input if need be.

## REFERENCES
Thanks to Christoph Salzmann for writing the original programme this is based on.

1 P. Németh, K. Mccoll, R. L. Smith, M. Murri, L. A. J. Garvie, M. Alvaro, B. Pécz, A. P. Jones, F. Corà, C. G. Salzmann and P. F. Mcmillan, Nano Lett., 2020, 20, 3611–3619. http://dx.doi.org/10.1021/acs.nanolett.0c00556
2 L. Radosinski, F. Formalik, A. Olejniczak and A. Radosz, Appl. Surf. Sci., 2017, 404, 154–161. http://dx.doi.org/10.1016/j.apsusc.2017.01.085
