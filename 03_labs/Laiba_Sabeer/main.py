"""
main.py
Demonstrates how to use custom modules and built-in packages in Python.
"""

# custom modules
from datetime import datetime
import datetime_util
from string_util import StringHandler


def main():
    date_utils= datetime_util.DateTimeHandler

    date1 = datetime(2025, 10, 21)
    date2 = datetime(2025, 12, 25)
    print(f"Date Difference: {date_utils.dates_diff(date1,date2)}")

    print(f"Yesterday: {date_utils.yesterday_date(date1)}")

    text = "Data Engineering"
    str_util = StringHandler()
    print(f"Uppercase: {str_util.to_upper(text)}")

if __name__ == "__main__":
    main()
