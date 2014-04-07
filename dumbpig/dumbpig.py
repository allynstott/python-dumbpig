#!/usr/bin/env python
"""
python-dumbpig

python-dumbpig is a python library that allows you to easily use the dumbpig
program to analyze Snort rulesets in a pythonic way.

Licence : GPL v3 or any later version


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Ryan Hays'
__author_email__ = 'ryan@oculussec.com'
__version__ = '0.0.1'
__last_modification__ = '2014.04.07'

import os
import subprocess
import re

class RuleChecker(object):
    """
        Allows use of dumbpig from within python
    """

    def __init__(self, dumbpig_search_path=('/usr/bin/dumbpig.pl',
                                            '/usr/local/bin/dumbpig.pl',
                                            '/sw/bin/dumbpig.pl',
                                            '/opt/local/bin/dumbpig.pl') ):
        self._dumbpig_path = ''
        self._dumbpig_version = ''
        self._dumbpig_sensitivity = '4'
        self._dumbpig_rulefile = ''
        self._dumbpig_output = ''
        is_dumbpig_found = False

        # Regex used to find the Dumbpig Version
        reg_ver = re.compile('DumbPig version ([0-9]*\.[0-9]*[^ ])* \-')
        # Search the paths specified for the dumbpig script to ensure that we
        # have it installed
        for dumbpig_path in dumbpig_search_path:
            try:
                proc_out = subprocess.Popen([dumbpig_path], bufsize=-1,
                                            stdout=subprocess.PIPE)
            except OSError:
                pass
            else:
                self._dumbpig_path = dumbpig_path # save path
                break
        else:
            raise RuleCheckerError('Dumbpig program was not found. Path: "%s"' %
                                   ", ".join(dumbpig_search_path))

        dp_out = bytes.decode(proc_out.communicate()[0])
        self._dumbpig_version = reg_ver.findall(dp_out)

        if self._dumbpig_version != '':
            is_dumbpig_found = True

        if not is_dumbpig_found:
            raise RuleCheckerError('Dumbpig was not found. Please install '
                                   'dumbpig first')

    def get_dumbpig_version(self):
        """
            Returns the version of DumbPig installed
        """

        return self._dumbpig_version

    def set_rule_file(self, rule_path):
        """
            Sets the rule file being processed
        """
        # Verify file exists
        if not os.path.isfile(rule_path):
            raise RuleCheckerError('Rule file is not found. Check path and '
                                   'try again.')

        self._dumbpig_rulefile = rule_path

    def set_sensitivity(self, sensitivity):
        """
            Sets the rule check sensitivity
        """
        # You can only have a sensitivity between 1-4
        if (sensitivity < 1) or sensitivity > 4:
            raise RuleCheckerError('Sensitivity can only be between 1 and 4.')

        self._dumbpig_sensitivity = sensitivity

    def test_rule_file(self):
        """
            Runs dumbpig against the rule file and gathers the output
        """

        # SAMPLE COMMAND
        # /usr/local/bin/dumbpig.pl -s 4 -r emerging-voip.rule
        try:
            proc_out = subprocess.Popen([self._dumbpig_path,
                                         '-s', self._dumbpig_sensitivity,
                                         '-r', self._dumbpig_rulefile],
                                        bufsize=-1,
                                        stdout=subprocess.PIPE)
        except OSError:
            raise RuleCheckerError('Error executing Dumbpig. Please try again.')

        dp_output = bytes.decode(proc_out.communicate()[0])
        self._dumbpig_output = dp_output

    def print_output(self):
        """
            Prints the raw output to the screen
        """

        return self._dumbpig_output

class RuleCheckerError(Exception):
    """
    Exception error class for RuleChecker class

    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return 'RuleCheckerError exception {0}'.format(self.value)

if __name__ == '__main__':
    pass