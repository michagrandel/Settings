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
#if( $License.toString().toLowerCase().contains("apache") || $License=="")
#parse("license.apache.py")
#elseif($License.toString().toLowerCase().contains("gpl") || $License.toString().toLowerCase().contains("gnu"))
#parse("license.agpl.py")
#end
#                     -----------------------------------------------------------------
#                     @formatter:on

"""
:mod:`${NAME}` -- discover and run all unit tests

.. module:: ${NAME}
   :platform: Unix, Windows
   :synopsis: create a TestLoader to run all unit tests
.. moduleauthor:: Micha Grandel <talk@michagrandel.de>
"""

from __future__ import unicode_literals
import six
import unittest


def discover(path='.'):
    """ discover all unit tests """
    loader = unittest.TestLoader()
    return loader.discover(path)


def run(tests):
    """ run unit tests """
    test_runner = unittest.runner.TextTestRunner(verbosity=2)
    test_runner.run(tests)


if __name__ == '__main__':
    tests = discover()
    run(tests)
