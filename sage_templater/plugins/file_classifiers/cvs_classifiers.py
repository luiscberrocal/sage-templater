from pathlib import Path
from typing import List


def get_csv_files(folder: Path, pattern: str = "**/*.csv") -> List[Path]:
    """Get excel files from a folder."""
    return list(folder.glob(pattern))


def main():
    folder = Path.home() / "Downloads" / "sage" #/ "data_ls"
    excel_files = get_csv_files(folder)
    for i, excel_file in enumerate(excel_files):
        try:
            start = time()
            is_small_box = is_small_box_template(excel_file)
            elapsed = time() - start
            if is_small_box:
                click.secho(f"{i + 1} {excel_file.relative_to(folder)} {is_small_box} time: {elapsed:.2f}", fg="green")
            else:
                click.secho(f"{i + 1} {excel_file.relative_to(folder)} {is_small_box} time: {elapsed:.2f}", fg="yellow")

        except Exception as e:
            click.secho(f"{i + 1} {excel_file.relative_to(folder)} {e}", fg="red")
