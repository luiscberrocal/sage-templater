import openpyxl


class TestGetWbAndSheets:

    def test_get_wb_and_sheets(self, small_box_xlsx_c1):
        from sage_templater.plugins.parsers.excel_parser import get_wb_and_sheets
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
