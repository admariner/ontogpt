"""Tests for IO utilities."""

import codecs
from pathlib import Path

from ontogpt.io.utils import ensure_utf8_coding_cookie, read_text_with_fallbacks


def test_read_text_with_fallbacks_utf8(tmp_path: Path) -> None:
    text = "cafe \u00e9"
    path = tmp_path / "utf8.txt"
    path.write_text(text, encoding="utf-8")
    assert read_text_with_fallbacks(path) == text


def test_read_text_with_fallbacks_utf8_bom(tmp_path: Path) -> None:
    text = "cafe \u00e9"
    path = tmp_path / "utf8_bom.txt"
    path.write_bytes(codecs.BOM_UTF8 + text.encode("utf-8"))
    assert read_text_with_fallbacks(path) == text


def test_read_text_with_fallbacks_utf16_bom(tmp_path: Path) -> None:
    text = "cafe \u00e9"
    path = tmp_path / "utf16.txt"
    path.write_bytes(text.encode("utf-16"))
    assert read_text_with_fallbacks(path) == text


def test_read_text_with_fallbacks_latin1(tmp_path: Path) -> None:
    text = "cafe \u00e9"
    path = tmp_path / "latin1.txt"
    path.write_bytes(text.encode("latin-1"))
    assert read_text_with_fallbacks(path) == text


def test_ensure_utf8_coding_cookie_adds_cookie() -> None:
    src = "print('hi')\n"
    out = ensure_utf8_coding_cookie(src)
    assert out.startswith("# -*- coding: utf-8 -*-\n")
    assert out.endswith("\n")


def test_ensure_utf8_coding_cookie_with_shebang() -> None:
    src = "#!/usr/bin/env python3\nprint('hi')\n"
    out = ensure_utf8_coding_cookie(src)
    lines = out.splitlines()
    assert lines[0] == "#!/usr/bin/env python3"
    assert lines[1] == "# -*- coding: utf-8 -*-"


def test_ensure_utf8_coding_cookie_preserves_existing() -> None:
    src = "# -*- coding: latin-1 -*-\nprint('hi')\n"
    out = ensure_utf8_coding_cookie(src)
    assert out == src


def test_ensure_utf8_coding_cookie_preserves_second_line() -> None:
    src = "#!/usr/bin/env python3\n# coding: utf-8\nprint('hi')\n"
    out = ensure_utf8_coding_cookie(src)
    assert out == src
