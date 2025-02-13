#!/usr/bin/env python3
"""
Author : Caroline <carolinescranton@arizona.edu>
Date   : 2025-01-23
Purpose: Say a word
"""

import argparse


# --------------------------------------------------
def get_args():
    """Say a word"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word',
                        help='word for what you see',
                        metavar='word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Say a word"""
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!') 

# --------------------------------------------------


if __name__ == '__main__':
    main()
