# -*- coding: utf-8 -*-
from typing import Any
from .constants import *


__all__ = sorted([x for x in dir(constants) if not x.startswith("_")])


def __getattr__(name: str) -> Any:
    if name in constants:
        return constants[name]
    raise ImportError(f"No module named {name}")


def __dir__() -> list[str]:
    return __all__