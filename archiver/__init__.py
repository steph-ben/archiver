import shutil
import logging
from pathlib import Path
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class Archiver:
    """
    Archive file in directory
    """
    base_directory = None
    default_subdir: str = "default"

    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)

        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True)

    def archive(self, fp: Path, subdir=default_subdir, unlink=False):
        dest_fp = self.base_directory / subdir / fp.name
        logger.info(f"Archiving {fp} to {dest_fp.absolute()}")

        if not dest_fp.parent.exists():
            dest_fp.parent.mkdir(parents=True)

        shutil.copy(str(fp), str(dest_fp))
        if unlink:
            fp.unlink()
