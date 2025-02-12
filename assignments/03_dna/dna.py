#!/usr/bin/env python3
"""
Author : Caroline Scranton <carolinescranton@arizona.edu>
Date   : 2025-02-10
Purpose: Read DNA samples
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    DNA=(args.DNA)
    nucleotides = {'A':0, 'C':0, 'G':0, 'T':0}
    Adenine = DNA.count('A')
    Cytosine = DNA.count('C')
    Guanine = DNA.count('G')
    Thymidine = DNA.count('T')
    for DNA in nucleotides.keys():
        if DNA == 'A':
            nucleotides['A'] =+ Adenine
        if DNA == 'C':
            nucleotides['C'] =+ Cytosine
        if DNA == 'G':
            nucleotides['G'] =+ Guanine
        if DNA == 'G':
            nucleotides['T'] =+ Thymidine
    print(*nucleotides.values())

# --------------------------------------------------
if __name__ == '__main__':
    main()
