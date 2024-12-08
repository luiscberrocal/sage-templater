from datetime import datetime

import pytest

from sage_templater.plugins.parsers.date_parsers import parse_date


class TestDateParsers:


    @pytest.mark.parametrize("str_date, expected_date", [
        #("2022-01-02", datetime(2022, 1, 2)),
        # ("2022-01-02 12:00:00", datetime(2022, 1, 2, 12, 0, 0)),
        ("2/1/2022", datetime(2022, 1, 2, 12, 0, 0)),
        ("18/05/2021", datetime(2021, 5, 18)),
    ])
    def test_parse_date(self, str_date, expected_date):
        date = parse_date(str_date)
        assert date == expected_date
