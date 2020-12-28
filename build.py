import py_compile
import os

from zipfile import PyZipFile, ZIP_STORED
from pathlib import Path

def main():
    for file_ in Path('src').rglob('*.py'):
        py_compile.compile(file_)

if __name__ == '__main__':
    main()
