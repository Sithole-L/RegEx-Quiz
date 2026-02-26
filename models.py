import csv
import re
from datetime import datetime

def validate_username(name: str) -> bool:
    """
    Validates user input.
    Returns True if name is alphanumeric and 3-15 chars.
    """
    if not name:
        return False
    return name.isalnum() and 3 <= len(name) <= 15