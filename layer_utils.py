#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diaphite Creator

A program to create layers of diamond-graphite mixes, known as diaphite.
Adapted from a Pascal program of unknown provenance.

@author: Matt Bailey
@date: 2020-01-06
"""

from enum import Enum, unique
from typing import Iterable, Union


@unique
class LayerTypes(Enum):
    """
    Represent each of the 4 different valid layer types.
    """

    Diamond = (1,)
    DiamondGraphene = 2
    Graphene = 3
    GrapheneDiamond = 4


def int_seq_to_layertypes(int_seq: Iterable[int]) -> Iterable[LayerTypes]:
    new_seq = []
    for item in int_seq:
        if item == 1:
            new_seq.append(LayerTypes.Diamond)
        elif item == 2:
            new_seq.append(LayerTypes.DiamondGraphene)
        elif item == 3:
            new_seq.append(LayerTypes.Graphene)
        elif item == 4:
            new_seq.append(LayerTypes.GrapheneDiamond)
        else:
            raise ValueError(f"Invalid layer type to transform, got {item}")
    return new_seq


def verify_layer_sequence(sequence: Iterable[Union[LayerTypes, int]]) -> bool:
    """
    Verify that a sequence of layers is valid.

    The rules are:
        - 1s can be followed by 1s or 2s
        - 2s can be followed by 3s
        - 3s can be followed by 3s or 4s
        - 4s can be followed by 1s

    Parameters
    ----------
    sequence
        An sequence of layer types
    Returns
    -------
    is_valid
        Does this sequence follow the rules?
    """
    if all(isinstance(item, int) for item in sequence):
        sequence = int_seq_to_layertypes(sequence)

    for idx in range(len(sequence)):
        next_idx = (idx + 1) % len(sequence)
        if sequence[idx] == LayerTypes.Diamond:
            # Diamond must be followed by diamond
            # or diamond/graphene interace.
            if sequence[next_idx] not in (
                LayerTypes.Diamond,
                LayerTypes.DiamondGraphene,
            ):
                return False
        elif sequence[idx] == LayerTypes.DiamondGraphene:
            # diamond/graphene interface must be followed by
            # graphene
            if sequence[next_idx] not in (LayerTypes.Graphene,):
                return False
        elif sequence[idx] == LayerTypes.Graphene:
            # graphene must be followed by graphene or
            # graphene / diamond interface
            if sequence[next_idx] not in (
                LayerTypes.Graphene,
                LayerTypes.GrapheneDiamond,
            ):
                return False
        elif sequence[idx] == LayerTypes.GrapheneDiamond:
            if sequence[next_idx] not in (LayerTypes.Diamond,):
                return False
        else:
            return False
    return True


def sequence_from_string(string: str) -> Iterable[LayerTypes]:
    """
    Read in a layer sequence from a string.

    The file should contain a single line, with a string of numbers 1-4
    representing layer types. The layers should follow the rules
    set out by verify_layer_sequence.

    Parameters
    ----------
    string
        a string made up of 1,2,3,4
    Returns
    -------
    int_seq
        A list of integers representing layer types, that follow the rules.

    Raises
    ------
    RuntimeError
        If the sequence is bad.
    """

    seq = []
    for item in string.strip():
        if item == "1":
            seq.append(LayerTypes.Diamond)
        elif item == "2":
            seq.append(LayerTypes.DiamondGraphene)
        elif item == "3":
            seq.append(LayerTypes.Graphene)
        elif item == "4":
            seq.append(LayerTypes.GrapheneDiamond)
        else:
            raise ValueError(f"Invalid layer type to transform, got {item}")
    return seq


def read_sequence_from_file(filename: str) -> Iterable[LayerTypes]:
    """
    Read in a layer sequence from a file.

    The file should contain a single line, with a string of numbers 1-4
    representing layer types. The layers should follow the rules
    set out by verify_layer_sequence

    Parameters
    ----------
    filename
        The name of the file to read the sequence from
    Returns
    -------
    seq
        A list of layer types that follow the rules.

    Raises
    ------
    RuntimeError
        If the sequence is bad.
    ValueError
        If the file contains non-integer characters.
    FileNotFoundError
        If the file with the given name can't be found.
    """
    with open(filename, "r") as fi:
        return sequence_from_string(fi.readline().strip())
