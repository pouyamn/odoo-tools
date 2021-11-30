#!/usr/bin/env python3

import re
import sys


def main(file):
    with open(file, mode='rt') as py_file:
        fields = re.findall(r"\s*(\w*)\s*=\s*fields\.", py_file.read())

    print(fields)
    print("\n".join(
        ['<field name="%s"/>' % field for field in fields]
    ))


if __name__ == "__main__":
    if len(sys.argv) !=2:
      print(f'Usage: {sys.argv[0]} path/to/python/file.py')
    main(sys.argv[1])
