import pytest
from unittest import TestCase

from cardilib.analysis.peaks_calculation import calculate_peaks


class TestPeaksCalculation(TestCase):
    def test_raise_error_when_no_max_peak_found(self):
        vector = [0, 0, 0, 0]
        min_dist_between_max_peaks = 2
        self.assertRaises(ValueError, lambda: calculate_peaks(vector, min_dist_between_max_peaks))

    def test_raise_error_when_no_max_peak_between_min_dist(self):
        vector = [0, 1, 0, 1, 0, 1, 0, 0]
        min_dist_between_max_peaks = 5
        self.assertRaises(ValueError, lambda: calculate_peaks(vector, min_dist_between_max_peaks))

    def test_raise_error_when_no_max_peak_found_due_to_possible_peaks_bellow_threshold(self):
        # The threshold is calculated as 1.0 / max(vector)
        # We use the threshold to avoid false positives

        vector = [0, 1, 0, 0, 0, 1, 0, 0]
        min_dist_between_max_peaks = 2
        self.assertRaises(ValueError, lambda: calculate_peaks(vector, min_dist_between_max_peaks))

    def test_raise_error_if_the_only_founded_peak_is_in_the_first_position_of_the_vector(self):
        vector = [2, 0, 0, 0, 0, 0, 0, 0]
        min_dist_between_max_peaks = 2
        self.assertRaises(ValueError, lambda: calculate_peaks(vector, min_dist_between_max_peaks))

    def test_raise_error_if_the_only_founded_peak_is_in_the_last_position_of_the_vector(self):
        vector = [0, 0, 0, 0, 0, 0, 2]
        min_dist_between_max_peaks = 2
        self.assertRaises(ValueError, lambda: calculate_peaks(vector, min_dist_between_max_peaks))
  
    def test_with_one_peaks_there_are_two_minimum_peaks(self):
        vector = [-1, 2, 3, 10, 9, 11, 6, 1, 3]
        min_dist_between_max_peaks = 2
        (max_peaks, min_peaks) = calculate_peaks(vector, min_dist_between_max_peaks)

        self.assertEqual(len(max_peaks), 1)
        self.assertEqual(max_peaks[0], 5)
        self.assertEqual(len(min_peaks), 2)
        self.assertEqual(min_peaks[0], 0)
        self.assertEqual(min_peaks[1], 7)

    def test_finds_max_and_minumum_peaks(self):
        vector = [-1, 2, 3, 10, 9, 8, 7, 15, 3]
        min_dist_between_max_peaks = 2
        (max_peaks, min_peaks) = calculate_peaks(vector, min_dist_between_max_peaks)

        self.assertEqual(len(max_peaks), 2)
        self.assertEqual(max_peaks[0], 3)
        self.assertEqual(max_peaks[1], 7)
        self.assertEqual(len(min_peaks), 3)
        self.assertEqual(min_peaks[0], 0)
        self.assertEqual(min_peaks[1], 6)
        self.assertEqual(min_peaks[2], 8)
