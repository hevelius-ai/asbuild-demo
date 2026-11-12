"""A broken test setup: this file ends the whole test run while pytest is still collecting, so no results are
written. AsBuild's demo uses it to show the UNRESOLVED verdict."""

import os

os._exit(3)
