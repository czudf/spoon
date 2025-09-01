# Copyright 2025 Yunqi Inc
# SPDX-License-Identifier: Apache-2.0

Spoon CLI

This module provides a command-line interface (CLI) for interacting with Spoon.

Available commands:
  hello  Print a greeting string.

Usage examples:
  python -m spoon_ec5fd18c.cli hello Alice
    Prints: Hello, Alice!
"""

import typer

from ._lib import hello

_cli = typer.Typer()


@_cli.command()
def _hello(name: str) -> None:
    """
    Print a greeting string.
    """
    print(hello(name))
