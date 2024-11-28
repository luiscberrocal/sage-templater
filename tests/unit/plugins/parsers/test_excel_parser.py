import openpyxl
import pytest

from sage_templater.plugins.parsers.excel_parser import get_wb_and_sheets, get_start_and_end_row_numbers, get_raw_rows, \
    parse_raw_rows


class TestGetWbAndSheets:

    def test_get_wb_and_sheets(self, small_box_xlsx_c1):
        wb, sheets = get_wb_and_sheets(small_box_xlsx_c1)
        assert isinstance(wb, openpyxl.Workbook)
        expected_sheets = [
            "14 DE ENERO ",
            "31 DE ENERO",
            "26 DE FEBRERO",
            "1 DE ABRIL",
            "2 DE MAYO",
            "1 DE JUNIO",
            "29 DE JUNIO",
            "COLOMBIA JUL19",
            "REEMBOLSO",
            "29 DE JULIO",
            "2 DE SEPTIEMBRE",
            "30 DE SEPTIEMBRE",
            "30 DE OCTUBRE",
            "COLOMBIA NOV19",
            "Hoja1",
            "30 DE NOVIEMBRE",
            "30 DE DICIEMBRE",
            "31 DE ENERO 2019",
            "29 DE FEBRERO 2020",
            "MARZO",
            "ABRIL",
            "MAYO",
            "VI\u00c1TICO OSVALDO",
            "VI\u00c1TICO FARIEL",
            "JUNIO ",
            "JULIO",
            "AGOSTO",
            "SEPTIEMBRE",
            "OCTUBRE",
            "NOVIEMBRE",
            "DICIEMBRE",
            "ENERO 2021",
            "FEBRERO 2021",
            "MARZO 2021",
            "ABRIL 2021",
            "MAYO 2021",
            "JUNIO 2021",
            "JULIO 2021",
            "AGOSTO 2021"
        ]

        assert sheets == expected_sheets


class TestGetStartAndEndRowNumbers:

    @pytest.mark.parametrize("sheet_name, expected_start_row, expected_end_row",
                             [
                                 ("14 DE ENERO ", 10, 42),
                                 ("31 DE ENERO", 10, 47),
                                 ("26 DE FEBRERO", 10, 39),
                                 ("1 DE ABRIL", 10, 57),
                                 ("2 DE MAYO", 10, 47),
                                 ("1 DE JUNIO", 10, 60),
                                 ("29 DE JUNIO", 10, 48),
                                 ("COLOMBIA JUL19", 10, 42),
                                 ("REEMBOLSO", 10, 42),
                                 ("29 DE JULIO", 10, 42),
                                 ("2 DE SEPTIEMBRE", 10, 42),
                                 ("30 DE SEPTIEMBRE", 10, 42),
                                 ("30 DE OCTUBRE", 10, 42),
                                 ("COLOMBIA NOV19", 10, 42),
                                 ("Hoja1", 10, 42),
                                 ("30 DE NOVIEMBRE", 10, 42),
                                 ("30 DE DICIEMBRE", 10, 42),
                                 ("31 DE ENERO 2019", 10, 42),
                                 ("29 DE FEBRERO 2020", 10, 42),
                                 ("MARZO", 10, 42),
                                 ("ABRIL", 10, 42),
                                 ("MAYO", 10, 42),
                                 ("VIÁTICO OSVALDO", 10, 42),
                                 ("VIÁTICO FARIEL", 10, 42),
                                 ("JUNIO ", 10, 42),
                                 ("JULIO", 10, 42),
                                 ("AGOSTO", 10, 42),
                                 ("SEPTIEMBRE", 10, 42),
                                 ("OCTUBRE", 10, 42),
                                 ("NOVIEMBRE", 10, 42),
                                 ("DICIEMBRE", 10, 42),
                                 ("ENERO 2021", 10, 42),
                                 ("FEBRERO 2021", 10, 42),
                                 ("MARZO 2021", 10, 42),
                                 ("ABRIL 2021", 10, 42),
                             ])
    def test_get_start_and_end_row_numbers(self, sheet_name, expected_start_row, expected_end_row, small_box_xlsx_c1):
        wb, sheets = get_wb_and_sheets(small_box_xlsx_c1)
        start_row, end_row = get_start_and_end_row_numbers(wb, sheet_name)
        assert start_row == expected_start_row, f"Expected {expected_start_row} but got {start_row} for {sheet_name}"
        assert end_row == expected_end_row, f"Expected {expected_end_row} but got {end_row} for {sheet_name}"


class TestGetRawRows:

    def test_get_raw_rows(self, small_box_xlsx_c1):
        wb, sheets = get_wb_and_sheets(small_box_xlsx_c1)
        start_row, end_row = get_start_and_end_row_numbers(wb, "14 DE ENERO ")
        raw_rows = get_raw_rows(wb, "14 DE ENERO ", start_row, end_row)
        assert len(raw_rows) == end_row - start_row + 1


class TestParseRawRows:

    def test_parse_raw_rows(self, small_box_xlsx_c1):
        wb, sheets = get_wb_and_sheets(small_box_xlsx_c1)
        start_row, end_row = get_start_and_end_row_numbers(wb, "14 DE ENERO ")
        raw_rows = get_raw_rows(wb, "14 DE ENERO ", start_row, end_row)
        records = parse_raw_rows(raw_rows, "small_box_client1.xlsx", "14 DE ENERO ")
        for r in records:
            print(r)
            print("-" * 80)
