import warnings
from pathlib import Path
from time import time
from typing import List

import click

from sage_templater.plugins.parsers.check_excel_parsers import is_check_template
from sage_templater.plugins.parsers.petit_cash_excel_parsers import is_small_box_template

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')


def get_excel_files(folder: Path, pattern: str = "**/*.xlsx") -> List[Path]:
    """Get excel files from a folder."""
    return list(folder.glob(pattern))


def main(pattern: str = "menuda"):
    folder = Path.home() / "Downloads" / "sage" #/ "data_ls"
    excel_files = get_excel_files(folder)
    for i, excel_file in enumerate(excel_files):
        try:
            if pattern is not None and pattern in excel_file.name.lower():
                start = time()
                is_petit_cash = is_small_box_template(excel_file)
                is_check = is_check_template(excel_file)
                elapsed = time() - start
                if is_petit_cash:
                    file_type = "PETIT_CASH"
                    click.secho(f"{i + 1} {excel_file.relative_to(folder)} {file_type} time: {elapsed:.2f}", fg="green")
                elif is_check:
                    file_type = "CHECK"
                    click.secho(f"{i + 1} {excel_file.relative_to(folder)} {file_type} time: {elapsed:.2f}", fg="blue")
                else:
                    file_type = "UNKNOWN"
                    click.secho(f"{i + 1} {excel_file.relative_to(folder)} {is_petit_cash} time: {elapsed:.2f}", fg="yellow")

        except Exception as e:
            click.secho(f"{i + 1} {excel_file.relative_to(folder)} {e}", fg="red")


if __name__ == '__main__':
    main()
