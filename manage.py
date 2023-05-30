#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import loguru_logging
from Shipping import database_init, objects_init, start, environment_init


def main():
    """Run administrative tasks."""
    environment_init()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    if sys.argv.__len__() == 1:
        loguru_logging.logger_init()
        environment_init()
        database_init()
        objects_init()
        start()
    else:
        main()
