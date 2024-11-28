from pathlib import Path
from typing import List

import openpyxl

from sage_templater.plugin_manager import hookimpl
from sage_templater.schemas import SmallBoxRecordSchema


def get_wb_and_sheets(file_path: Path) -> (openpyxl.Workbook, List[str]):
    """Get workbook and sheets from an Excel file."""
    wb = openpyxl.load_workbook(file_path, data_only=True)
    return wb, wb.sheetnames


def get_start_and_end_row_numbers(wb: openpyxl.Workbook, sheet_name: str) -> tuple[int, int]:
    """Get start and end row numbers from a sheet with the small box format."""
    sheet = wb[sheet_name]
    start_row = -1
    end_row = sheet.max_row
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value in ["Código", "CÓDIGO"]:
                start_row = cell.row
                break
    return start_row, end_row


def get_raw_rows(wb: openpyxl.Workbook, sheet_name: str, start_row: int, end_row: int) -> List[List[str]]:
    """Get raw rows from a sheet with the small box format."""
    sheet = wb[sheet_name]
    raw_rows = []
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row):
        raw_row = []
        for cell in row:
            raw_row.append(str(cell.value))
        raw_rows.append(raw_row)
    return raw_rows


@hookimpl
def parse_file(file_path: str) -> List[SmallBoxRecordSchema]:
    if not file_path.endswith(".xlsx"):
        return []
