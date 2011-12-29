from argcmd.management.base import BaseCommand

from argcmd import make_option

"""
15.4.1. Example
From http://docs.python.org/dev/library/argparse.html#argparse.ArgumentParser.parse_args
"""

class Command(BaseCommand):
    arg_list = BaseCommand.arg_list + (
        make_option('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator'),
        make_option('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)'),
    )
    description = 'hehlo'

    def handle(self, *args, **options):
        args = self.arguments
        print(args.accumulate(args.integers))
