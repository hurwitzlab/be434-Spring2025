#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-02-24
Purpose: Count C and G
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input sequence file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.FILE)


# --------------------------------------------------
if __name__ == '__main__':
    main()
