#!/usr/bin/env python
"""An example of using dumbpig to perform syntax checking on bad.rules"""

import dumbpig
import sys


def dumbpig_rulecheck(rule_path):
    """Perform syntax checking on snort rule file with dumbpig"""
    try:
        dpig = dumbpig.RuleChecker()
        dpig.set_rule_file(rule_path)
        dpig.test_rule_file()
        dpig_output = dpig.process_output()
    except dpig.RuleCheckerError as err:
        raise err
    return dpig_output


def main():
    """Program starts here"""
    try:
        print dumbpig_rulecheck("bad.rules")
    except dumbpig.RuleChecker.RuleCheckerError as err:
        print err

if __name__ == "__main__":
    sys.exit(main())
