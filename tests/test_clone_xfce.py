#!/usr/bin/env python

"""
Name: test_clone_xfce.py
Purpose: test clone_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
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
        pass
        # begins with self.

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_clone_xfce(self):
        """testing clone_xfce() function"""
        # self.assertIsNotNone(
        #     clone_xfce(component=bindings, comp_list=bindings)
        # )
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of clone_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_main(self):
        """testing main() function in clone_xfce.py"""
        # self.assertIsNotNone(main(bindings))
        pass


if __name__ == "__main__":
    unittest.main()
