import py_compile
import os

from zipfile import PyZipFile, ZIP_STORED
from pathlib import Path

def main():
    for file_ in Path('src').rglob('*.py'):
        py_compile.compile(
            file_,
            os.path.join("build", file_.with_suffix(".pyc"))
        )

if __name__ == '__main__':
    main()
