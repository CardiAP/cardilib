import pytest
from unittest import TestCase

import numpy as np

from cardilib.analysis.statistical_functions import calculate_amplitudes, MAX_PEAKS_ARE_REQUIRED, MIN_PEAKS_ARE_REQUIRED, \
    BAD_MAX_AND_MIN_LENGTHS, calculate_time_to_peaks, calculate_times_to_half_peaks, EMPTY_INTENSITIES, \
    MAX_POSITIONS_OUT_OF_BOUND, MIN_POSITIONS_OUT_OF_BOUND, calculate_taus, _calculate_tau


class StatisticalFunctionsTest(TestCase):

    def test_max_peaks_are_needed_for_amplitude_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_amplitudes([], [])
        self.assertEqual(str(context.exception), MAX_PEAKS_ARE_REQUIRED)

    def test_min_peaks_are_needed_for_amplitude_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_amplitudes([1], [])
        self.assertEqual(str(context.exception), MIN_PEAKS_ARE_REQUIRED)

    def test_mins_need_to_be_2_more_than_maxs(self):
        with self.assertRaises(AssertionError) as context:
            calculate_amplitudes([1], [1])
        self.assertEqual(str(context.exception), BAD_MAX_AND_MIN_LENGTHS)

    def test_do_the_amplitudes_calculation(self):
        amplitudes = calculate_amplitudes([4, 6], [1, 2, 3])
        self.assertEqual(len(amplitudes), 2)
        self.assertEqual(amplitudes[0], (4 - 1) / 1)
        self.assertEqual(amplitudes[1], (6 - 2) / 2)

    def test_max_peaks_are_needed_for_time_to_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_time_to_peaks([], [])
        self.assertEqual(str(context.exception), MAX_PEAKS_ARE_REQUIRED)

    def test_min_peaks_are_needed_for_time_to_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_time_to_peaks([1], [])
        self.assertEqual(str(context.exception), MIN_PEAKS_ARE_REQUIRED)

    def test_mins_need_to_be_2_more_than_maxs_for_time_to_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_time_to_peaks([1], [1])
        self.assertEqual(str(context.exception), BAD_MAX_AND_MIN_LENGTHS)

    def test_do_the_time_to_peak_calculation(self):
        calibration = 2
        times_to_peaks = calculate_time_to_peaks([4, 6], [1, 2, 3], calibration)
        self.assertEqual(len(times_to_peaks), 2)
        self.assertEqual(times_to_peaks[0], (4 - 1) * calibration)
        self.assertEqual(times_to_peaks[1], (6 - 2) * calibration)

    def test_max_peaks_are_needed_for_time_to_half_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_times_to_half_peaks([], [], [])
        self.assertEqual(str(context.exception), MAX_PEAKS_ARE_REQUIRED)

    def test_min_peaks_are_needed_for_time_to_half_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_times_to_half_peaks([], [1], [])
        self.assertEqual(str(context.exception), MIN_PEAKS_ARE_REQUIRED)

    def test_mins_need_to_be_2_more_than_maxs_for_time_to_half_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_times_to_half_peaks([], [1], [1])
        self.assertEqual(str(context.exception), BAD_MAX_AND_MIN_LENGTHS)

    def test_intensities_are_needed_for_time_to_half_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_times_to_half_peaks([], [1], [1, 1])
        self.assertEqual(str(context.exception), EMPTY_INTENSITIES)

    def test_max_positions_need_to_be_indexes_of_intensities_for_time_to_half_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_times_to_half_peaks([1], [1], [1, 1])
        self.assertEqual(str(context.exception), MAX_POSITIONS_OUT_OF_BOUND)

    def test_min_positions_need_to_be_indexes_of_intensities_for_time_to_half_peak_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_times_to_half_peaks([1], [0], [1, 1])
        self.assertEqual(str(context.exception), MIN_POSITIONS_OUT_OF_BOUND)

    def test_do_the_time_to_half_peak_calculation(self):
        calibration = 2
        intensities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        max_peaks = [9, 19]
        min_peaks = [0, 10, 20]

        times_to_half_peaks = calculate_times_to_half_peaks(intensities, max_peaks, min_peaks, calibration)
        self.assertEqual(len(times_to_half_peaks), 2)
        self.assertEqual(times_to_half_peaks[0], 5 * calibration)
        self.assertEqual(times_to_half_peaks[1], 5 * calibration)

    def test_max_peaks_are_needed_for_tau_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_taus([], [], [])
        self.assertEqual(str(context.exception), MAX_PEAKS_ARE_REQUIRED)

    def test_min_peaks_are_needed_for_tau_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_taus([], [1], [])
        self.assertEqual(str(context.exception), MIN_PEAKS_ARE_REQUIRED)

    def test_mins_need_to_be_2_more_than_maxs_for_tau_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_taus([], [1], [1])
        self.assertEqual(str(context.exception), BAD_MAX_AND_MIN_LENGTHS)

    def test_intensities_are_needed_for_tau_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_taus([], [1], [1, 1])
        self.assertEqual(str(context.exception), EMPTY_INTENSITIES)

    def test_max_positions_need_to_be_indexes_of_intensities_for_tau_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_taus([1], [1], [1, 1])
        self.assertEqual(str(context.exception), MAX_POSITIONS_OUT_OF_BOUND)

    def test_min_positions_need_to_be_indexes_of_intensities_for_tau_calculation(self):
        with self.assertRaises(AssertionError) as context:
            calculate_taus([1], [0], [1, 1])
        self.assertEqual(str(context.exception), MIN_POSITIONS_OUT_OF_BOUND)

    def test_do_the_tau_calculation(self):
        calibration = 2
        intensities = [1, 2, 3, 4, 10, 8, 6, 4, 2, 0, 6, 7, 8, 9, 10, 6, 3, 3, 2, 1]
        max_peaks = [4, 14]
        min_peaks = [0, 9, 19]
        times_for_first_peak = np.array([4, 5, 6, 7, 8]) * calibration
        times_for_second_peak = np.array([14, 15, 16, 17, 18]) * calibration
        intensities_for_first_peak = intensities[4:9]
        intensities_for_second_peak = intensities[14:19]

        taus = calculate_taus(intensities, max_peaks, min_peaks, calibration)
        self.assertEqual(len(taus), 2)
        self.assertEqual(taus[0], _calculate_tau(times_for_first_peak, intensities_for_first_peak))
        self.assertEqual(taus[1], _calculate_tau(times_for_second_peak, intensities_for_second_peak))
