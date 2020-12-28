# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\importer\custom_import.py
# Compiled at: 2020-02-06 03:30:39
# Size of source mod 2**32: 10107 bytes
import builtins, importlib.abc
from importlib.machinery import PathFinder
import sys
from os import scandir
import sims4.importer.layering, sims4.reload, sims4.tuning.serialization
from paths import DLL_PATH
with sims4.reload.protected(globals()):
    _baseimport = builtins.__import__
    _custom_finder = None
_ignore_modules = [
 'sims4.importer',
 'os', 'io', 're', 'sys', 'imp',
 'importlib', 'pickle', 'collections', '_locale',
 'pkgutil', 'threading', 'math', 'operator', 'xml', 'functools',
 'struct', 'heapq', 'array',
 'weakref', '_weakrefutils',
 'google', 'omega', 'protocolbuffers']

class CustomFinder(importlib.abc.MetaPathFinder):
    _pyd_folders = None

    @staticmethod
    def _build_pyd_locations_cache():
        res = {}
        for dirEntry in scandir(DLL_PATH):
            if not dirEntry.is_dir():
                continue
            res[dirEntry.name] = PathFinder._path_importer_cache(dirEntry.path)

        return res

    @classmethod
    def _search_pyd_locations(cls, fullname):
        if cls._pyd_folders is None:
            cls._pyd_folders = cls._build_pyd_locations_cache()
        else:
            folder = fullname.rpartition('.')[0]
            if not folder:
                return
            finder = cls._pyd_folders.get(folder)
            return finder or None
        return finder.find_spec(fullname)

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        spec = cls._search_pyd_locations(fullname)
        if spec is None:
            spec = PathFinder.find_spec(fullname, path=path, target=target)
        else:
            if spec is None:
                return
            if spec.loader is not None:
                if hasattr(spec.loader, 'exec_module'):
                    spec.loader = CustomLoader(spec.loader)
                else:
                    spec.loader = LegacyCustomLoader(spec.loader)
        return spec


class LegacyCustomLoader(importlib.abc.Loader):

    def __init__(self, real_loader):
        self._real_loader = real_loader

    def load_module(self, load_fullname):
        mod = self._real_loader.load_module(load_fullname)
        self.post_load(mod)
        return mod

    def post_load(self, module):
        if not _should_ignore_module(module.__name__):
            sims4.tuning.serialization.process_tuning(module)

    @property
    def path(self):
        return self._real_loader.path

    def is_package(self, fullname):
        return self._real_loader.is_package(fullname)

    def get_code(self, fullname):
        return self._real_loader.get_code(fullname)

    def get_source(self, fullname):
        return self._real_loader.get_source(fullname)

    def get_filename(self, fullname):
        return self._real_loader.get_filename(fullname)


class CustomLoader(LegacyCustomLoader):

    def create_module(self, spec):
        return self._real_loader.create_module(spec)

    def exec_module(self, module):
        self._real_loader.exec_module(module)
        self.post_load(module)


def _import(name, global_dict=None, local_dict=None, fromlist=None, level=0):
    mod = _baseimport(name, global_dict, local_dict, fromlist, level)
    return mod


def enable():
    global _custom_finder
    if _custom_finder is None:
        _custom_finder = CustomFinder()
        sys.meta_path.remove(PathFinder)
        sys.meta_path.append(_custom_finder)


def disable():
    global _custom_finder
    if _custom_finder is not None:
        sys.meta_path.remove(_custom_finder)
        sys.meta_path.append(PathFinder)
        _custom_finder = None


def _should_ignore_module(module_name):
    return _find_module_in_list(module_name, _ignore_modules)


def _find_module_in_list(module_name, module_list):
    name_list = module_name.split('.')
    name_list_len = len(name_list)
    for module_name in module_list:
        ignore_list = module_name.split('.')
        ignore = True
        for i in range(len(ignore_list)):
            if i < name_list_len and name_list[i] != ignore_list[i]:
                ignore = False
                break

        if ignore:
            return True