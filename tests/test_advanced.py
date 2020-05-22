# -*- coding: utf-8 -*-

import unittest

from .context import raptorbot


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(raptorbot.hmm())


if __name__ == '__main__':
    unittest.main()
