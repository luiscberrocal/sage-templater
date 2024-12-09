from sage_templater.plugins.parsers.check_excel_parsers import get_start_and_end_row_numbers
from sage_templater.plugins.parsers.excel_parser import get_wb_and_sheets


class TestGetStartAndEndRowNumbers:

    def test_get_start_and_end_row_numbers(self, check_template):
        wb, sheet_names =  get_wb_and_sheets(check_template)
        start, end = get_start_and_end_row_numbers(wb, sheet_names[0])
        assert start == 8
        assert end == 16
