python-dumbpig
==============
A Python library for running the Dumbpig Snort Rule Checker.

Requirements
------------
Class::Accessor, Parse::Snort, libwww-perl, and dumbpig.

Install
-------
On CentOS 6/7, installation is as follows:

```
sudo yum install perl-CPAN perl-libwww-perl perl-Class-Accessor
sudo cpan -i "Parse::Snort"
git clone git@github.com:leonward/dumbpig.git
sudo ln -s dumbpig/dumbpig.pl /usr/local/bin/dumbpig.pl
git clone ***REMOVED***
cd python-dumbpig
sudo python setup.py install
```

Usage
-----
```
>>> import dumbpig
>>> dp = dumbpig.RuleChecker()
>>> print dp.get_dumbpig_version()
0.2
>>> dp.set_rule_file("bad.rules")
>>> dp.test_rule_file()
>>> dp_output = dp.process_output()
>>> dp_json = dp.json_output()
```

Output
------
The output of the `process_output()` function is defined as follows:

```
{line_number:
    {
        'fix': ['fix description 1', 'fix description 2', ...],
        'rule': 'Snort rule'
    },
    ...
}
```

License
-------
GNU General Public License (GPL) 3.0