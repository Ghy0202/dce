import argparse
from pathlib import Path


def make_output_dir(path):
    path = Path(path)
    assert not path.exists(), f'{path} already exists'
    try:
        path.mkdir()
    except:
        assert False, f'Could not create {path}'


def cc_opt_pair_arg(s):
    s = s.split(',')
    if len(s) != 2:
        raise argparse.ArgumentTypeError(
            f'{s} should contain exactly one comma')
    return s[0], s[1]


def opt_level_arg(s):
    if s not in ['1', '2', 's', '3']:
        raise argparse.ArgumentTypeError(
            f'O{opt} is not a valid optimization level')
    return 'O' + s
