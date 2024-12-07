from pathlib import Path
from time import time
from typing import List

from sage_templater.plugins.parsers.excel_parser import is_small_box_template

def get_excel_files(folder: Path, pattern: str = "**/*.xlsx") -> List[Path]:
    """Get excel files from a folder."""
    return list(folder.glob(pattern))


def main():
    folder = Path.home() / "Downloads" / "sage" / "data_ls"
    excel_files = get_excel_files(folder)
    for i, excel_file in enumerate(excel_files):
        try:
            start = time()
            is_small_box = is_small_box_template(excel_file)
            elapsed = time() - start
            if is_small_box or "caja" in excel_file.name.lower():
                print(f"{i + 1} {excel_file.relative_to(folder)} {is_small_box} time: {elapsed:.2f}")

        except Exception as e:
            print(f"{i + 1} {excel_file.relative_to(folder)} {e}")

if __name__ == '__main__':
    main()


