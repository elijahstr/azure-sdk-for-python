import os
import types
import pytest

# Get list of updated files (comma-separated)
UPDATED_FILES = os.getenv("UPDATED_SAMPLE_FILES", "").split(",")

def pytest_collect_file(parent, path):
    if path.ext == ".py":
        # Match only filenames listed in UPDATED_SAMPLE_FILES
        filename = str(path).split("/")[-1]  # just the filename
        for updated_file in UPDATED_FILES:
            if updated_file.strip() == filename:
                return parent.Module.from_parent(parent=parent, fspath=path)

def pytest_pycollect_makeitem(collector, name, obj):
    if isinstance(obj, types.FunctionType):
        return pytest.Function.from_parent(collector, name=name)
