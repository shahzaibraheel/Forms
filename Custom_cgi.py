# custom_cgi.py

from urllib.parse import parse_qs
from html import escape
import re

# Mimicking cgi.parse_qs
def parse_query_string(query_string):
    """
    Parse a query string into a dictionary of lists using urllib.parse.parse_qs.
    """
    return parse_qs(query_string)


# Mimicking cgi.escape
def html_escape(text, quote=True):
    """
    Escape a string for HTML using html.escape.
    """
    return escape(text, quote)


# Mimicking cgi.parse_header
def parse_header(header_value):
    """
    Mimic the cgi.parse_header function, which parses a content-type header
    into a MIME type and optional parameters.

    Example:
    'text/html; charset=UTF-8' -> ('text/html', 'charset=UTF-8')
    """
    if not header_value:
        return '', ''

    parts = header_value.split(';', 1)
    if len(parts) == 1:
        return parts[0].strip(), ''

    # Remove extra spaces around the parts
    mime_type = parts[0].strip()
    params = parts[1].strip()

    return mime_type, params
# Adding a valid_boundary implementation
def valid_boundary(boundary):
    """
    Validate a multipart boundary string according to RFC 2046 standards.
    """
    if not boundary:
        return False

    # Decode bytes to string if necessary
    if isinstance(boundary, bytes):
        boundary = boundary.decode('utf-8', 'ignore')

    # Boundary must not contain control characters, spaces, or special characters
    # except for '-' and it should not be empty.
    if re.match(r"^[\w\-]+$", boundary):
        return True
    return False
