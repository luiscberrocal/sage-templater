from pathlib import Path
from typing import List

from sage_templater.plugins.parsers.excel_parser import is_small_box_template

def get_excel_files(folder: Path, pattern: str = "**/*.xlsx") -> List[Path]:
    """Get excel files from a folder."""
    return list(folder.glob(pattern))


def main():
    folder = Path.home() / "Downloads" / "sage" / "data_ls"
    excel_files = get_excel_files(folder)
    for i, excel_file in enumerate(excel_files):
        is_small_box = is_small_box_template(excel_file)
        print(f"{i + 1}: {excel_file.relative_to(folder)} {is_small_box}")


if __name__ == '__main__':
    main()


