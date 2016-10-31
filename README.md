# persistent-resources-tests-parse

Tool for parsing the persistent resource test results https://github.com/osic/persistent-resources-tests

This parsing tool assumes the files given is/was converted from subunit to csv format. For example using `` cat subunitFile|subunit-1to2|subunit2csv`` will do the trick :). Script returns a valid json containing info about test (name, status, service).  

