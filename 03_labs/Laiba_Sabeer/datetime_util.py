"""
datetime_util.py
A simple utility module for datetime operations.
"""
from datetime import datetime, timedelta

class DateTimeHandler:
    """
    A utility class for common datetime handling operations.
    """
    def yesterday_date(date1: datetime) -> timedelta:
        yesterday = date1 - timedelta(days=1)
        return yesterday

    def dates_diff(date1: datetime, date2:datetime) -> timedelta:
        print("Is date1 before date2?", date1 < date2)
        x = date1-date2
        return x

    
