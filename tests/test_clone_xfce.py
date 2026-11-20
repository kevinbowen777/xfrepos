"""
Name: test_clone_xfce.py
Purpose: test clone_xfce.py script

source: https://gitlab.com/kevinbowen/xfrepos
version: 0.8.7
updated: 20260828
@author: kevin.bowen@gmail.com
"""

import unittest

from cappdata import component_list  # ruff: ignore[unused-import]
from clone_xfce import clone_xfce  # ruff: ignore[unused-import]

args = "bindings"


class TestCloneXfce(unittest.TestCase):
    """Test the clone_xfce() function of clone_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        # begins with self.

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")

    def test_clone_xfce(self):
        """testing clone_xfce() function"""
        # self.assertIsNotNone(
        #     clone_xfce(component=bindings, comp_list=bindings)
        # )


class TestMain(unittest.TestCase):
    """Test the main() function of clone_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")

    def test_main(self):
        """testing main() function in clone_xfce.py"""
        # self.assertIsNotNone(main(bindings))


if __name__ == "__main__":
    unittest.main()
