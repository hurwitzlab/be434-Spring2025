#!/usr/bin/env python3
"""
Author : Caroline <carolinescranton@arizona.edu>
Date   : 2025-02-10
Purpose: Jump the 5
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the 5',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text')

   
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    text = args.text
    for char in text:
        print(jumper.get(char, char), end='')

    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
