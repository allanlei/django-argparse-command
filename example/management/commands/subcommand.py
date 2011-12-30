from argcmd.management.base import BaseCommand

from argcmd import make_option

"""
15.4.5.1. Sub-commands
From http://docs.python.org/dev/library/argparse.html#argparse.ArgumentParser.add_subparsers

python manage.py subcommand a 12
    Namespace(bar=12, foo=False) => {'baz': 12, 'foo': False}
    
python manage.py subcommand --foo b --baz Z
    Namespace(baz='Z', foo=True) => {'baz': 'Z', 'foo': True}
"""

class Command(BaseCommand):
    arg_list = BaseCommand.arg_list + (
        make_option('--foo', action='store_true', help='foo help'),
    )

    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        
        subparsers = parser.add_subparsers(help='sub-command help')
        
        # create the parser for the "a" command
        parser_a = subparsers.add_parser('a', help='a help')
        parser_a.add_argument('bar', type=int, help='bar help')
        
        # create the parser for the "b" command
        parser_b = subparsers.add_parser('b', help='b help')
        parser_b.add_argument('--baz', choices='XYZ', help='baz help')
        return parser
    
    def handle(self, *args, **options):
        print args, options
