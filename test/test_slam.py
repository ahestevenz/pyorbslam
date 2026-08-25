import time
import logging
import numpy as np
import imutils
import pickle
import time
import os

import pandas as pd
import pytest
import cv2

import pyorbslam

from .conftest import SETTINGS_DIR, TEST_DIR, EUROC_TEST_DATASET

logger = logging.getLogger("pyorbslam")

# Constants
EUROC_TEST_DATASET = TEST_DIR / 'data' / 'EuRoC' / 'MH01'


def test_mono_slam():
    slam = pyorbslam.MonoSLAM(SETTINGS_DIR / 'EuRoC_ViconRoom2.yaml')
    assert isinstance(slam, pyorbslam.MonoSLAM)
    slam.shutdown()


def test_mono_slam_last_init_diagnostics_default_before_any_frame():
    # Before any frame is processed, MonocularInitialization() hasn't run yet,
    # so all three getters should report the "stage not reached" sentinel.
    slam = pyorbslam.MonoSLAM(SETTINGS_DIR / 'EuRoC_ViconRoom2.yaml')
    assert slam.get_last_init_detections() == -1
    assert slam.get_last_init_raw_matches() == -1
    assert slam.get_last_init_inlier_matches() == -1
    slam.shutdown()