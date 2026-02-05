"""IO Utilities."""

import codecs
import locale
from typing import Any

from pydantic import BaseModel


def eliminate_empty(obj: Any, preserve=False) -> Any:
    """Eliminate empty lists and dicts from an object."""
    if isinstance(obj, list):
        return [eliminate_empty(x, preserve) for x in obj if x or preserve]
    elif isinstance(obj, dict):
        return {k: eliminate_empty(v, preserve) for k, v in obj.items() if v or preserve}
    elif isinstance(obj, BaseModel):
        return eliminate_empty(obj.model_dump(), preserve)
    elif isinstance(obj, tuple):
        return [eliminate_empty(x, preserve) for x in obj]
    elif isinstance(obj, str):
        return str(obj)
    else:
        return obj


def read_text_with_fallbacks(path) -> str:
    """Read text from a file, trying various encodings to handle BOMs and common encodings."""
    data = path.read_bytes()
    if data.startswith(codecs.BOM_UTF8):
        return data.decode("utf-8-sig")
    if data.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        return data.decode("utf-16")
    if data.startswith((codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        return data.decode("utf-32")

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        pass

    preferred = locale.getpreferredencoding(False) or "utf-8"
    if preferred.lower() != "utf-8":
        try:
            return data.decode(preferred)
        except UnicodeDecodeError:
            pass

    return data.decode("latin-1")


def ensure_utf8_coding_cookie(module_src: str) -> str:
    """Ensure that the given module source code has a UTF-8 coding cookie."""
    lines = module_src.splitlines()
    for line in lines[:2]:
        if "coding" in line:
            return module_src

    cookie = "# -*- coding: utf-8 -*-"
    if lines and lines[0].startswith("#!"):
        updated = "\n".join([lines[0], cookie, *lines[1:]])
    else:
        updated = f"{cookie}\n{module_src}"
    if module_src.endswith("\n") and not updated.endswith("\n"):
        updated += "\n"
    return updated
