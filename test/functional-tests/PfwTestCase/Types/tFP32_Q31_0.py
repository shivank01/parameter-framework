# -*-coding:utf-8 -*

# Copyright (c) 2011-2015, Intel Corporation
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Fixed-Point parameter type testcases - FP32_Q31.0

List of tested functions :
--------------------------
    - [setParameter]  function
    - [getParameter] function

Initial Settings :
------------------
    FP32_Q31.0 :
        - size = 32 bits
        - 31 integer bits, 0 fractionnal bits
        - range : [-2147483648, 2147483647]

Test cases :
------------
    - FP32_Q31.0 parameter min value = -2147483648
    - FP32_Q31.0 parameter min value out of bounds = -4147483649
    - FP32_Q31.0 parameter max value = 2147483647
    - FP32_Q31.0 parameter max value out of bounds = 12147483648
    - FP32_Q31.0 parameter in nominal case = 2222
"""
import commands
from Util.PfwUnitTestLib import PfwTestCase
from Util import ACTLogging
log=ACTLogging.Logger()

# Test of type FP32_Q31.0 - range [-2147483648,2147483647]
class TestCases(PfwTestCase):
    def setUp(self):
        self.param_name = "/Test/Test/TEST_DIR/FP32_Q31.0"
        self.pfw.sendCmd("setTuningMode", "on")

    def tearDown(self):
        self.pfw.sendCmd("setTuningMode", "off")

    def test_Nominal_Case(self):
        """
        Testing FP32_Q31.0 in nominal case = 2222
        -----------------------------------------
            Test case description :
            ~~~~~~~~~~~~~~~~~~~~~~~
                - set FP32_Q31.0 parameter in nominal case = 2222
            Tested commands :
            ~~~~~~~~~~~~~~~~~
                - [setParameter] function
            Used commands :
            ~~~~~~~~~~~~~~~
                - [getParameter] function
            Expected result :
            ~~~~~~~~~~~~~~~~~
                - FP32_Q31.0 parameter set to 2222
                - Blackboard and filesystem values checked
        """
        log.D(self.test_Nominal_Case.__doc__)
        log.I("FP32_Q31.0 parameter in nominal case = 2222")
        value = "2222"
        hex_value = "0x8ae"
        #Set parameter value
        out, err = self.pfw.sendCmd("setParameter", self.param_name, value)
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert out == "Done", log.F("when setting parameter %s : %s"
                                    % (self.param_name, out))
        #Check parameter value on blackboard
        out, err = self.pfw.sendCmd("getParameter", self.param_name, "")
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert float(out) == float(value), log.F("BLACKBOARD : Incorrect value for %s, expected: %s, found: %s"
                                                 % (self.param_name, value, out))
        #Check parameter value on filesystem
        assert commands.getoutput('cat $PFW_RESULT/FP32_Q31.0') == hex_value, log.F("FILESYSTEM : parameter update error")
        log.I("test OK")

    def test_TypeMin(self):
        """
        Testing FP32_Q31.0 minimal value = -2147483648
        ----------------------------------------------
            Test case description :
            ~~~~~~~~~~~~~~~~~~~~~~~
                - set FP32_Q31.0 parameter min value = -2147483648
            Tested commands :
            ~~~~~~~~~~~~~~~~~
                - [setParameter] function
            Used commands :
            ~~~~~~~~~~~~~~~
                - [getParameter] function
            Expected result :
            ~~~~~~~~~~~~~~~~~
                - FP32_Q31.0 parameter set to -2147483648
                - Blackboard and filesystem values checked
        """
        log.D(self.test_TypeMin.__doc__)
        log.I("FP32_Q31.0 parameter min value = -2147483648")
        value = "-2147483648"
        hex_value = "0x80000000"
        #Set parameter value
        out, err = self.pfw.sendCmd("setParameter", self.param_name, value)
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert out == "Done", log.F("when setting parameter %s : %s"
                                    % (self.param_name, out))
        #Check parameter value on blackboard
        out, err = self.pfw.sendCmd("getParameter", self.param_name, "")
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert float(out) == float(value), log.F("BLACKBOARD : Incorrect value for %s, expected: %s, found: %s"
                                                 % (self.param_name, value, out))
        #Check parameter value on filesystem
        assert commands.getoutput('cat $PFW_RESULT/FP32_Q31.0') == hex_value, log.F("FILESYSTEM : parameter update error")
        log.I("test OK")

    def test_TypeMin_Overflow(self):
        """
        Testing FP32_Q31.0 parameter value out of negative range
        --------------------------------------------------------
            Test case description :
            ~~~~~~~~~~~~~~~~~~~~~~~
                - set FP32_Q31.0 to -4147483649
            Tested commands :
            ~~~~~~~~~~~~~~~~~
                - [setParameter] function
            Used commands :
            ~~~~~~~~~~~~~~~
                - [getParameter] function
            Expected result :
            ~~~~~~~~~~~~~~~~~
                - error detected
                - FP32_Q31.0 parameter not updated
                - Blackboard and filesystem values checked
        """
        log.D(self.test_TypeMin_Overflow.__doc__)
        log.I("FP32_Q31.0 parameter min value out of bounds = -4147483649")
        value = "-4147483649"
        param_check = commands.getoutput('cat $PFW_RESULT/FP32_Q31.0')
        #Set parameter value
        out, err = self.pfw.sendCmd("setParameter", self.param_name, value)
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert out != "Done", log.F("PFW : Error not detected when setting parameter %s out of bounds"
                                    % (self.param_name))
        #Check parameter value on filesystem
        assert commands.getoutput('cat $PFW_RESULT/FP32_Q31.0') == param_check, log.F("FILESYSTEM : Forbiden parameter change")
        log.I("test OK")

    def test_TypeMax(self):
        """
        Testing FP32_Q31.0 parameter maximum value
        ------------------------------------------
            Test case description :
            ~~~~~~~~~~~~~~~~~~~~~~~
                - set FP32_Q31.0 to 2147483647
            Tested commands :
            ~~~~~~~~~~~~~~~~~
                - [setParameter] function
            Used commands :
            ~~~~~~~~~~~~~~~
                - [getParameter] function
            Expected result :
            ~~~~~~~~~~~~~~~~~
                - FP32_Q31.0 parameter set to 2147483647
                - Blackboard and filesystem values checked
        """
        log.D(self.test_TypeMax.__doc__)
        log.I("FP32_Q31.0 parameter max value = 2147483647")
        value = "2147483647"
        hex_value = "0x7fffffff"
        #Set parameter value
        out, err = self.pfw.sendCmd("setParameter", self.param_name, value)
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert out == "Done", log.F("when setting parameter %s : %s"
                                  % (self.param_name, out))
        #Check parameter value on blackboard
        out, err = self.pfw.sendCmd("getParameter", self.param_name, "")
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert float(out) == float(value), log.F("BLACKBOARD : Incorrect value for %s, expected: %s, found: %s"
                                                 % (self.param_name, value, out))
        #Check parameter value on filesystem
        assert commands.getoutput('cat $PFW_RESULT/FP32_Q31.0') == hex_value, log.F("FILESYSTEM : parameter update error")
        log.I("test OK")

    def test_TypeMax_Overflow(self):
        """
        Testing FP32_Q31.0 parameter value out of positive range
        --------------------------------------------------------
            Test case description :
            ~~~~~~~~~~~~~~~~~~~~~~~
                - set FP32_Q31.0 to 12147483648
            Tested commands :
            ~~~~~~~~~~~~~~~~~
                - [setParameter] function
            Used commands :
            ~~~~~~~~~~~~~~~
                - [getParameter] function
            Expected result :
            ~~~~~~~~~~~~~~~~~
                - error detected
                - FP32_Q31.0 parameter not updated
                - Blackboard and filesystem values checked
        """
        log.D(self.test_TypeMax_Overflow.__doc__)
        log.I("FP32_Q31.0 parameter max value out of bounds = 12147483648")
        value = "12147483648"
        param_check = commands.getoutput('cat $PFW_RESULT/FP32_Q31.0')
        #Set parameter value
        out, err = self.pfw.sendCmd("setParameter", self.param_name, value)
        assert err == None, log.E("when setting parameter %s : %s"
                                  % (self.param_name, err))
        assert out != "Done", log.F("PFW : Error not detected when setting parameter %s out of bounds"
                                    % (self.param_name))
        #Check parameter value on filesystem
        assert commands.getoutput('cat $PFW_RESULT/FP32_Q31.0') == param_check, log.F("FILESYSTEM : Forbiden parameter change")
        log.I("test OK")
