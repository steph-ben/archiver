import celery
import shutil

from pathlib import Path
from datetime import datetime, timedelta


class Archiver:
    """
    Archive file in directory
    """
    base_directory = None
    default_subdir: str = "default"

    def __init__(self, base_directory: Path):
        self.base_directory = Path(base_directory)

        if not self.archive_base_directory.exists():
            self.archive_base_directory.mkdir(parents=True)

    def archive(self, fp: Path, subdir=self.default_subdir):
        dest_fp = self.base_directory / subdir
        logger.info(f"Archiving {fp} to {dest_fp.absolute()}")
        fp.rename(dest_fp)
