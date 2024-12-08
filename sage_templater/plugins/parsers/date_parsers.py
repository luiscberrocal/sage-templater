import re
from datetime import datetime

from dateutil.parser import parse


def parse_date_old(date_str: str) -> datetime | None:
    try:
        regexp = re.compile(r"\d{4}-\d{2}-\d{4}")
        if regexp.match(date_str):
            return datetime.strptime(date_str, "%Y-%m-%d")

        return parse(date_str, dayfirst=True)
    except ValueError:
        # Handle errors, perhaps log them or return a default value
        return None


def parse_spanish_date(date_str: str) -> datetime | None:
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        return None


def parse_date(str_date: str, raise_error:bool=False) -> datetime | None:
   # "(?P<day>[\d]{1,2})/(?P<month>[\d]{1,2})/(?P<year>[\d]{2})"
    datetime_regexp_strs = [
        (r"(?P<year>[0-9]{4})-(?P<month>[\d]{1,2})-(?P<day>[\d]{1,2})", "%Y-%m-%d"),
        (r"(?P<day>[\d]{1,2})/(?P<month>[\d]{1,2})/(?P<year>[0-9]{4})", "%d/%m/%Y"),
        (r"(?P<day>[\d]{1,2})-(?P<month>[\d]{1,2})-(?P<year>[0-9]{4})", "%d-%m-%Y"),
        (r"(?P<day>[\d]{1,2})/(?P<month>[\d]{1,2})/(?P<year>[\d]{2})", "%d/%m/%y"),
        (r"(?P<day>[\d]{1,2})-(?P<month>[\d]{1,2})-(?P<year>[\d]{2})", "%d-%m-%y"),
        (r"(?P<year>[0-9]{4})-(?P<month>1[0-2]|0[1-9])-(?P<day>3[01]|[12][0-9]|0[1-9]) "
         r"(?P<hour>2[0-3]|[01][0-9]):(?P<min>[0-5][0-9]):(?P<sec>[0-5][0-9])",
         "%Y-%m-%d %H:%M:%S"),
    ]
    for datetime_regexp_str, format_str in datetime_regexp_strs:
        regexp = re.compile(datetime_regexp_str)
        match = regexp.match(str_date)
        if match is not None:
            try:
                return datetime.strptime(str_date, format_str)
            except ValueError:
                if raise_error:
                    raise
                return None

    return None
