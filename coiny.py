#!/usr/bin/env python3
'''coiny - scrapes Market Data from deribit.com

Usage:
    coiny.py --version

'''

import docopt


__version__ = '0.0.1'

def main(args):
    print(f'coiny v{__version__}')
    print(f'args = {args}')


if __name__ == '__main__':
    args = docopt.docopt(__doc__, version=__version__)
    main(args)