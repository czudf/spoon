# Copyright 2025 Yunqi Inc
# SPDX-License-Identifier: Apache-2.0

"""
Usage:
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
