"""
Test custom Django management commands.
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycop2Error

from django.core.management import call_command
from django.db.utils import OperationalError