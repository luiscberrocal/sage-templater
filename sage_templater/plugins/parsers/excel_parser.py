from pathlib import Path
from typing import List

import openpyxl

from sage_templater.plugin_manager import hookimpl
from sage_templater.schemas import SmallBoxRecordSchema


def get_wb_and_sheets(file_path: Path) -> (openpyxl.Workbook, List[str]):
    wb = openpyxl.load_workbook(file_path)
    return wb, wb.sheetnames


def get_start_and_end_row_numbers(wb: openpyxl.Workbook, sheet_name: str) -> tuple[int, int]:
    sheet = wb[sheet_name]
    start_row = -1
    end_row = sheet.max_row
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value in ["Código", "CÓDIGO"]:
                start_row = cell.row
                break
    return start_row, end_row


@hookimpl
def parse_file(file_path: str) -> List[SmallBoxRecordSchema]:
    if not file_path.endswith(".xlsx"):
        return []
