#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-03-24
Purpose: Print greeting
"""

import argparse
from enum import Flag


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g', '--greeting', default= 'Howdy', metavar= 'str', help='The greeting')

    parser.add_argument('-n','--name', default= 'Stranger', metavar= 'str', help='Whom to greet')
                    
    parser.add_argument('-e','--excited', help='Print ! if this flag is present', action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = args.excited

    if excited:
        print(f'{greeting}, {name}!')
    else:
        print(f'{greeting}, {name}.')
    



# --------------------------------------------------
if __name__ == '__main__':
    main()