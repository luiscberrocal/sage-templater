from pathlib import Path
from typing import List

import openpyxl
from sage_templater.plugin_manager import hookimpl
from sage_templater.schemas import SmallBoxRecordSchema

def get_wb_and_sheets(file_path: Path) -> (openpyxl.Workbook, List[str]):
    wb = openpyxl.load_workbook(file_path)
    return wb, wb.sheetnames

@hookimpl
def parse_file(file_path: str) -> List[SmallBoxRecordSchema]:
    if not file_path.endswith(".xlsx"):
        return []

