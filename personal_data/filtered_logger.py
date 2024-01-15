#!/usr/bin/env python3
"""
Module for log filtering
"""

import re


def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in the log message.

    Arguments:
    - fields: List of strings representing fields to obfuscate.
    - redaction: String representing the obfuscation value.
    - message: String representing the log line.
    - separator: String representing the character separating fields in the log line.

    Returns:
    - String: Log message with specified fields obfuscated.
    """
    return re.sub(fr'(?<={separator}|^)({"|".join(fields)})=[^{separator}]+', f'\\1={redaction}', message)
