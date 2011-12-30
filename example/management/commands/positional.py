import numbers

"""
Retrieving positional args, based of numbers.py
numbers.py
    def handle(self, *args, **options):
        print args, options
        
    => () {'integers': [1, 2, 3, 4], 'accumulate': <built-in function max>}
"""

class Command(numbers.Command):
    def handle(self, integers, **options):
        """
        [1, 2, 3, 4] {'accumulate': <built-in function max>}
        """
        print integers, options
        return super(Command, self).handle(integers, **options)
