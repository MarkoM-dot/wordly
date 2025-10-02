"""Test configurations and helper functions."""

from __future__ import annotations

from pathlib import Path

FIXTURE_DIR = Path(__file__).parent / "fixtures"


def load_fixture(filename: str, *, fixture_dir: Path = FIXTURE_DIR) -> bytes:
    """Return fixture file from default directory."""
    return (fixture_dir / filename).read_bytes()
