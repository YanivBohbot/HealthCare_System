import re

def validate_email(email):
    """Validate email address format."""
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None


def validate_phone_number(phone):
    """Validate phone number format (simple check for numeric and length)."""
    return phone.isdigit() and len(phone) in [10, 11, 12]


def validate_email(email):
    """Validate email address format."""
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None