""" Tests for dna.py """

import os
from subprocess import getstatusoutput

PRG = './dna.py'
TEST1 = ('./inputs/input1.txt', '1 2 3 4')
TEST2 = ('./inputs/input2.txt', '20 12 17 21')
TEST3 = ('./inputs/input3.txt', '196 231 237 246')


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg() -> None:
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        retval, out = getstatusoutput(f'{PRG} {dna}')
        assert retval == 0
        assert out == expected

