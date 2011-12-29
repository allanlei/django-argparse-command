**Incomplete Readme**

# Usage #

## Converting from Django Commands to ArgParse Commands ##

* Change **from django.core.management.base import BaseCommand** to **from argcmd.management.base import BaseCommand**
* Change **from optparse import make_option** to **from argcmd import make_option**
* Change option_list to arg_list
* Some options might need a little tweaking due to incompatibilities
