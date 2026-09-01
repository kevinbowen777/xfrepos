#!/usr/bin/env python

"""
Name: test_build_xfce.py
Purpose: test build_xfce.py script

source: https://gitlab.com/kevinbowen/xfrepos
version: 0.8.7
updated: 20260828
@author: kevin.bowen@gmail.com
"""

import unittest

from build_xfce import build_xfce  # ruff: ignore[unused-import]
from cappdata import component_list  # ruff: ignore[unused-import]

arg = "bindings"


class TestBuildXfce(unittest.TestCase):
    """Test the build_xfce() function of build_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_build_xfce(self):
        """testing build_xfce() function."""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of build_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_main(self):
        """testing main() function in build_xfce.py"""
        pass


if __name__ == "__main__":
    unittest.main()
