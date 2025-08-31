# Copyright 2025 Yunqi Inc
# SPDX-License-Identifier: Apache-2.0

from spoon_ec5fd18c._lib import hello


def test_hello():
    assert hello("Python") == "Hello Python!"
