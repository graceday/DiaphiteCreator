#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:17:19 2021

@author: matthew-bailey
"""

from layer_utils import verify_layer_sequence
import pytest


class TestSequenceVerifier:
    def test_all_same_type(self):
        """
        Test two simple valid sequences.
        """
        seq = [1, 1, 1, 1, 1, 1]
        assert verify_layer_sequence(seq)

        seq = [3, 3, 3, 3, 3, 3]
        assert verify_layer_sequence(seq)

    def test_one_negative(self):
        with pytest.raises(ValueError):
            seq = [1, 1, 1, 1, 5, 1]
            assert not verify_layer_sequence(seq)

    def test_one_nonnumeric(self):
        seq = [1, 1, 1, "a", 1, 1]
        assert not verify_layer_sequence(seq)

    def test_valid_pattern(self):
        seq = [1, 2, 3, 4]
        assert verify_layer_sequence(seq)

    def test_invalid_pattern(self):
        seq = [1, 3, 2, 4]
        assert not verify_layer_sequence(seq)

    def test_real_sequence(self):
        """
        This sequence came with the code of unknown provenance
        """
        seq = [1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 1]
        assert verify_layer_sequence(seq)
