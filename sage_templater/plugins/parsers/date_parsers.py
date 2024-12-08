from datetime import datetime

from dateutil.parser import parse


def parse_date(date_str: str) -> datetime | None:
    try:
        dt = parse_spanish_date(date_str)
        if dt:
            return dt
        return parse(date_str)
    except ValueError:
        # Handle errors, perhaps log them or return a default value
        return None

def parse_spanish_date(date_str: str) -> datetime | None:
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        return None
