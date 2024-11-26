from typing import List

from sage_templater.plugin_manager import hookimpl
from sage_templater.schemas import SmallBoxRecordSchema


@hookimpl
def parse_file(file_path: str) -> List[SmallBoxRecordSchema]:
    if not file_path.endswith(".xlsx"):
        return []
    
