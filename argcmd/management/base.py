from django.core.management.base import BaseCommand as BaseDjangoCommand
from django.core.management.base import handle_default_options

from argparse import ArgumentParser

from argcmd import make_option


class BaseCommand(BaseDjangoCommand):
    arg_list = (
        make_option('-v', '--verbosity', action='store', dest='verbosity', default='1', choices=['0', '1', '2', '3'],
            help='Verbosity level; 0=minimal output, 1=normal output, 2=all output'),
        make_option('--settings',
            help='The Python path to a settings module, e.g. "myproject.settings.main". If this isn\'t provided, the DJANGO_SETTINGS_MODULE environment variable will be used.'),
        make_option('--pythonpath',
            help='A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".'),
        make_option('--traceback', action='store_true',
            help='Print traceback on exception'),
    )
    description = None
    epilog = None
    add_help = True
    prog = None
    usage = None

    def run_from_argv(self, argv):
        """
        Set up any environment changes requested (e.g., Python path
        and Django settings), then run this command.

        """
        parser = self.create_parser(argv[0], argv[1])
        self.arguments = parser.parse_args(argv[2:])
        handle_default_options(self.arguments)
        options = vars(self.arguments)
        self.execute(**options)

    def get_usage(self, subcommand):
        """
        Return a brief description of how to use this command, by
        default from the attribute ``self.help``.

        """
        return self.usage or '%(prog)s {subcommand} [options]'.format(subcommand=subcommand)

    def create_parser(self, prog_name, subcommand):
        """
        Create and return the ``ArgumentParser`` which will be used to
        parse the arguments to this command.

        """        
        parser = ArgumentParser(
            description=self.description,
            epilog=self.epilog,
            add_help=self.add_help,
            prog=self.prog,
            usage=self.get_usage(subcommand),
        )
        parser.add_argument('--version', action='version', version=self.get_version())
        self.add_arguments(parser)
        return parser
    
    def add_arguments(self, parser):
        for args, kwargs in self.arg_list:
            parser.add_argument(*args, **kwargs)
