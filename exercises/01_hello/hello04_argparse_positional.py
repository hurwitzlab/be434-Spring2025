#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
arg=parser.parse_args()
name=arg.name
print('Hello, ' + name + '!')
