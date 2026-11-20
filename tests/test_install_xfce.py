"""
Name: test_install_xfce.py
Purpose: test install_xfce.py script

source: https://gitlab.com/kevinbowen/xfrepos
version: 0.8.7
updated: 20260828
@author: kevin.bowen@gmail.com
"""

import unittest

from cappdata import component_list, query_yes_no  # ruff: ignore[unused-import]
from install_xfce import install_xfce  # ruff: ignore[unused-import]

args = "bindings"


class TestInstallXfce(unittest.TestCase):
    """Test the install_xfce() function of install_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")

    def test_install_xfce(self):
        """testing install_xfce() function"""


class TestMain(unittest.TestCase):
    """Test the main() function of install_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")

    def test_main(self):
        """testing main() function in install_xfce.py"""


if __name__ == "__main__":
    unittest.main()
