"""
string_util.py
A simple utility module for string operations.
"""

class StringHandler:
    """
    A utility class for common string handling operations.
    """
    @staticmethod
    def to_upper(text: str) -> str:
        """Convert string to uppercase."""
        return text.upper() if text else text

