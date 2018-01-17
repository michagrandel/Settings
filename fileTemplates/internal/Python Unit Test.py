#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @formatter:off
#
#                                             ,,
#                                             db
#     \
#     _\,,          `7MM  `7MM  `7MMpMMMb.  `7MM  ,p6"bo   ,pW"Wq.`7Mb,od8 `7MMpMMMb.
#    "-=\~     _      MM    MM    MM    MM    MM 6M'  OO  6W'   `Wb MM' "'   MM    MM
#       \\~___( ~     MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#      _|/---\\_      MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#     \        \      MM    MM    MM    MM    MM YM.    , YA.   ,A9 MM       MM    MM
#                     `Mbod"YML..JMML  JMML..JMML.YMbmd'   `Ybmd9'.JMML.   .JMML  JMML.
#
#                     written with <3 by Micha Grandel, talk@michagrandel.com
#                     
#                     Project:         https://github.com/michagrandel/${PROJECT_NAME}
#                     Report a bug:    https://github.com/michagrandel/${PROJECT_NAME}/issues
#                     Contribute:      https://github.com/michagrandel/${PROJECT_NAME}/wiki/Contribute
#                     
#                     Facebook:        https://me.me/micha.animator
#                     Instagram:       @michagrandel
#                     -----------------------------------------------------------------
#                     
#parse("license.apache.py")
#                     -----------------------------------------------------------------
#                     @formatter:on

"""
:mod:`${NAME}` -- Unit test

.. module:: ${NAME}
   :platform: Unix, Windows
   :synopsis: unit test
.. moduleauthor:: Micha Grandel <talk@michagrandel.de>
"""

from __future__ import unicode_literals, print_function
from io import open
import six
import unittest


class MyTestCase(unittest.TestCase):
    """ Test Case """
    
    def test_something(self):
        """ test something """
        self.assertEqual(True, False)


def main():
    """ run all tests """
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()