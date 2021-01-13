#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diaphite Creator Writer Utils

Write a set of diaphite atomic positions to a variety of file types.

@author: Matt Bailey
@date: 2020-01-06
"""

from typing import Optional, TextIO

import numpy as np


def write_xyz(filename: str, positions: np.array, comment: Optional[str] = None):
    """
    Write positions to an xyz file.

    Parameters
    ----------
    filename
        The name of the xyz file
    positions
        an Nx3 array of positions in angstroms.
    Returns
    -------
    None
    """
    with open(filename, "w") as fi:
        fi.write(f"{positions.shape[0]}\n")
        fi.write(str(comment).strip() + "\n")
        for row in positions:
            fi.write(f"{row[0]:.5f} {row[1]:.5f} {row[2]:.5f}\n")


def write_cif_header(file: TextIO, cell_a: float, cell_b: float, cell_c: float) -> None:
    """
    Write the CIF file header out to an open file handle.
    Parameters
    ----------
    file
        An open file handle to write to.
    cell_a
        The length of the a unit cell vector, in Angstroms
    cell_b
        The length of the b unit cell vector, in Angstroms
    cell_c
        The length of the c unit cell vector, in Angstroms
    Returns
    -------
    None
    """

    file.write("data_type2diaphite\n")
    file.write("_symmetry_space_group_name_H-M    P1\n")
    file.write("_symmetry_Int_Tables_number       1\n")
    file.write("_symmetry_cell_setting            triclinic\n")
    file.write("loop_\n")
    file.write("_symmetry_equiv_pos_as_xyz\n")
    file.write("  x,y,z\n")
    file.write(f"_cell_length_a                    {cell_a:.5f}\n")
    file.write(f"_cell_length_b                    {cell_b:.5f}\n")
    file.write(f"_cell_length_c                    {cell_c:.5f}\n")
    file.write("_cell_angle_alpha                 90.0000\n")
    file.write("_cell_angle_beta                  90.0000\n")
    file.write("_cell_angle_gamma                 90.0000\n")
    file.write("loop_\n")
    file.write("_atom_site_label\n")
    file.write("_atom_site_type_symbol\n")
    file.write("_atom_site_fract_x\n")
    file.write("_atom_site_fract_y\n")
    file.write("_atom_site_fract_z\n")
    file.write("_atom_site_occupancy\n")


def write_cif(
    filename: str, positions: np.array, cell_a: float, cell_b: float, cell_c: float
):
    """
    Write a Crystallographic Information File out to the file with given name.

    CIF includes crystallographic data handled by write_cif_header,
    and uses reduced positions (i.e. fractions of cell vectors).

    Parameters
    ----------
    filename
        An open file handle to write to.
    positions
        An Nx3 array of atomic positions.
    cell_a
        The length of the a unit cell vector, in Angstroms
    cell_b
        The length of the b unit cell vector, in Angstroms
    cell_c
        The length of the c unit cell vector, in Angstroms
    Returns
    -------
    None
    """

    reduced_positions = positions / np.array([cell_a, cell_b, cell_c])
    with open(filename, "w") as fi:
        write_cif_header(fi, cell_a, cell_b, cell_c)
        for idx, row in enumerate(reduced_positions, 1):
            fi.write(f"C{idx}  C  {row[0]:5.5f}  {row[1]:5.5f}  {row[2]:5.5f}  1\n")


def write_lammpsdata(
    filename: str, positions: np.array, cell_a: float, cell_b: float, cell_c: float
):
    """
    Write out a LAMMPS data file.

    Parameters
    ----------
    filename
        An open file handle to write to.
    positions
        An Nx3 array of atomic positions.
    cell_a
        The length of the a unit cell vector, in Angstroms
    cell_b
        The length of the b unit cell vector, in Angstroms
    cell_c
        The length of the c unit cell vector, in Angstroms
    Returns
    -------
    None
    """
    with open(filename, "w") as fi:
        fi.write("Diaphite Data\n")
        fi.write("\n")
        fi.write(f"{positions.shape[0]} atoms\n")
        fi.write("\n")
        fi.write("1 atom types\n")
        fi.write(f"{0.0:5.5f} {cell_a} xlo xhi\n")
        fi.write(f"{0.0:5.5f} {cell_b} ylo yhi\n")
        fi.write(f"{0.0:5.5f} {cell_c} zlo zhi\n")
        fi.write("\n")
        fi.write("Atoms\n")
        fi.write("\n")
        for idx, row in enumerate(positions, 1):
            fi.write(f"{idx} 1 {row[0]}  {row[1]}  {row[2]}\n")
